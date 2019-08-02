#include "Adafruit_TCS34725.h"
#include <avr/wdt.h>

//descomentar para usar el monitor serial de Arduino 
//#define serial_arduino

#define TCAADDR 0x70

Adafruit_TCS34725 ColorSensor = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

//declaración e inicializacion de variables
bool error_flag=0, system_activated=0, serial_flag=0;
byte s1_color=0, s2_color=0, s3_color=0, top_color=0, mid_color=0, bott_color=0;//1-blue, 2-red, 3-yellow
byte motor_speed=1, sensor_pos=1;
int error_count=0;
unsigned int sen[4];
String command = "", time_check= "060";
unsigned long serial_prev_time = 0, serial_curr_time = 0, serial_interval = 60000;
;

/*byte gammatable[256];
uint16_t blu[4]={570, 1200, 2000, 3855};
uint16_t red[4]={350, 650, 650, 5320};
uint16_t yel[4]={6300, 4880, 2000, 13585};*/

void setup() {
    timerConfig();
    
    Wire.begin();
    Serial.begin(9600);

    pinMode(3, OUTPUT);
    wdt_enable(WDTO_2S);
}
 
void loop() {
  //resetea el conteo de errores y apaga el motor
  error_count=0;
  timerOff();

  //lee comunicacion serial hasta que pida activar
  while(!system_activated) {
    TCNT2 = 0;
    error_flag = 0;
    sensor_pos = 1;
    read_command();
    wdt_reset();
  }

  //enciende el motor con RPM = motor_speed
  timerInit(motor_speed);

  //funciona hasta que se pida desactivar
  while(system_activated) {
    wdt_reset();
    //lee el color del sensor correspondiente
    if(sensor_pos == 1)
      s1_color = colorSense(1);
    else if(sensor_pos == 2)
      s2_color = colorSense(1);
    else if(sensor_pos == 3)
      s3_color = colorSense(2);

    //si el color leido coincide con el color requerido por el comando
    //comienza a leer el siguiente sensor y no cuenta un error
    if(s1_color == top_color && sensor_pos == 1) {
      sensor_pos = 2;
      s1_color = 0;
      #ifdef serial_arduino
      Serial.print("\tOK ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }
    //si no coinciden comienza a leer el siguiente sensor y cuenta un error
    else if(s1_color != 0 && s1_color != top_color && sensor_pos == 1) {
      sensor_pos = 2;
      s1_color = 0;
      error_count++;
      error_flag = 1;
      #ifdef serial_arduino
      Serial.print("\tNO ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }

    //si el color leido coincide con el color requerido por el comando
    //comienza a leer el siguiente sensor y no cuenta un error
    if(s2_color == mid_color && sensor_pos == 2) {
      sensor_pos = 3;
      s2_color = 0;
      #ifdef serial_arduino
      Serial.print("\tOK ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }
    //si no coinciden comienza a leer el siguiente sensor y
    //si no hubo un error previo, cuenta un error
    else if(s2_color != 0 && s2_color != mid_color && sensor_pos == 2) {
      sensor_pos = 3;
      s2_color = 0;
      if(!error_flag) {
        error_count++;
        error_flag = 1;
      }
      #ifdef serial_arduino
      Serial.print("\tNO ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }

    //si el color leido coincide con el color requerido por el comando
    //comienza a leer el siguiente sensor y no cuenta un error
    if(s3_color == bott_color && sensor_pos == 3) {
      sensor_pos = 1;
      s3_color = 0;
      #ifdef serial_arduino
      Serial.print("\tOK ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }
    //si no coinciden comienza a leer el siguiente sensor y
    //si no hubo un error previo, cuenta un error
    else if(s3_color!=0 && s3_color!=bott_color && sensor_pos==3) {
      sensor_pos=1;
      s3_color=0;
      if(!error_flag) {
        error_count++;
        error_flag = 1;
      }
      #ifdef serial_arduino
      Serial.print("\tNO ");
      Serial.print("pos:");
      Serial.println(sensor_pos);
      #endif
    }
    
    //lee comnado
    read_command();
    
    if(!system_activated) {
      Serial.println(error_count);
    }
  }
}

void timerConfig() {
  TCCR2A = 0b00100011; //fast PWM, OC2B(pin3)
  TCCR2B = 0b00001000; //top = OCRA
}

void timerOff() {
  TCCR2B &= ~(1 << CS22 | 1 << CS21 | 1 << CS20);
}

void timerInit(uint8_t opc) {
  TCNT2 = 0;
  switch (opc){
    case 1:
      TCCR2B |= 0b111;//prescalador
      OCR2A = 255;//top
      OCR2B = 127;//compare
    break;
    case 2:
      TCCR2B |= 0b111;
      OCR2A = 146;
      OCR2B = 72;
    break;
    case 3:
      TCCR2B |= 0b111;
      OCR2A = 97;
      OCR2B = 48;
    break;
    case 4:
      TCCR2B |= 0b111;
      OCR2A = 72;
      OCR2B = 35;
    break;
    case 5:
      TCCR2B |= 0b110;
      OCR2A = 235;
      OCR2B = 117;
    break;
  }
}

int colorSense(byte x) {///funcion sensado color
  byte color = 0;
  if (x > 7)
    return 0;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << x);
  Wire.endTransmission();  
  
  ColorSensor.getRawData(&sen[0], &sen[1], &sen[2], &sen[3]);
  for(int i=0; i<3; i++)
  {
    if(sen[i]>1000)
    {
      color++;
    }
    if(sen[i]>3000)
    {
      color=color+2;
    }
    if(sen[i]>5000)
    {
      color=color+3;
    }
  }
  switch (color) {
    case 2:
      #ifdef serial_arduino
      Serial.print("Blue");
      #endif
      return 1;
    case 3:
      #ifdef serial_arduino
      Serial.print("Red");
      #endif
      return 2;
    case 13:
      #ifdef serial_arduino
      Serial.print("Yellow");
      #endif
      return 3;
    default:
      return 0;
  }
}

void read_command() {
  if(Serial.available()) {
    serial_flag = 0;
    command = Serial.readString();
    if(command.length() == 7) {
      command.setCharAt(5, '0');
      command.setCharAt(6, '6');
      command += "0";
    }
    else if (command.length() > 7 && command.length() < 10) {
      command.setCharAt(5, '0');
      command.setCharAt(6, '6');
      command.setCharAt(7, '0');
    }
    motor_speed = command.charAt(0) - '0';
    top_color = command.charAt(1) - '0';
    mid_color = command.charAt(2) - '0';
    bott_color = command.charAt(3) - '0';
    system_activated = command.charAt(4) - '0';
    time_check.setCharAt(0, command.charAt(5));
    time_check.setCharAt(1, command.charAt(6));
    time_check.setCharAt(2, command.charAt(7));
    serial_interval = (unsigned long)(time_check.toInt()*1000) + 3000;
    
    #ifdef serial_arduino
    Serial.println(command);
    Serial.print("RPM:");
    Serial.print(motor_speed);
    Serial.print(" Top:");
    Serial.print(top_color);
    Serial.print(" Mid:");
    Serial.print(mid_color);
    Serial.print(" Bot:");
    Serial.print(bott_color);
    Serial.print(" State:");
    Serial.println(system_activated);
    #endif
  }
  else {
    if(system_activated) {
      if(!serial_flag) {
        serial_prev_time = millis();
        serial_flag = 1;
      }
      if(millis() - serial_prev_time > serial_interval) {
        while(1);
      }
    }
  }
}
