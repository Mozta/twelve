#include <Adafruit_TCS34725.h>

//descomentar para usar el monitor serial de Arduino 
//#define serial_arduino
//#define serial_color
//#define serial_color_porciento
//#define serial_acierto
//#define serial_success
//#define serial_falla

#define TCAADDR 0x70

Adafruit_TCS34725 ColorSensor = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

//declaración e inicializacion de variables
bool error_flag = 0, system_activated = 0, last_color_sense = 0;
int top_color = 0, mid_color = 0, bott_color = 0;//1-blue, 2-red, 3-yellow
int sensor_pos = 0;
byte motor_speed = 1;
int error_count = 0;
String command = "";

int read_speed = 1;
//float tActual;
unsigned long tActual;
int estado;
int success_count = 0;
bool checkTime;
/*byte gammatable[256];
uint16_t blu[4]={570, 1200, 2000, 3855};
uint16_t red[4]={350, 650, 650, 5320};
uint16_t yel[4]={6300, 4880, 2000, 13585};*/

void setup()
{
    timerConfig();

    Wire.begin();
    Serial.begin(9600);
    pinMode(3, OUTPUT);

    for (int i = 0; i <= 2; i++)
    { // de 0 a 2
        SensorPicker(i); // marco como activo al sensor con puerto i del multiplexor
        ColorSensor.begin(); // inicializo dicho sensor con .begin()
    }
}

/* Logica del sensor
 *  Si regresa un 0 entonces no hay ficha
 *  Si regresa un 1 entonces hay ficha y es del color esperado
 *  Si regresa un 2 entonces hay ficha y no es del color esperado
 */

int lectura(int sensorToRead, int colorToCompare)
{
    int s_color = colorSense(sensorToRead); // leemos color del sensor
    if (s_color != 0) // si el color es distinto de cero (rojo, azul o amarillo)
    {
        if (s_color == colorToCompare) // si el color es el mismo que el predefinido
        {
            return 1; // regresamos un 1
        }
        else // de otro modo
        {
            return 2; // regresamos un 2
        }
    }
    else // de otro modo
        return 0; // regresamos un 0
}

bool chkTime(unsigned long referenceTime, unsigned long umbralTime)
{
    unsigned long diffT = (millis() - referenceTime); // medimos la diferencia de tiempo entre la entrada de una ficha y el tiempo actual
                                              //Serial.println(diffT);
    if (diffT >= umbralTime) // si la diferencia es mayor a 3.5 segundos
        return false; // desactivamos el checador de tiempo
    else
        return true;
}

void loop()
{
    //resetea el conteo de errores y apaga el motor
    error_count = 0;
    success_count = 0;
    timerOff();

    //lee comunicacion serial hasta que pida activar
    while (!system_activated)
    {
        TCNT2 = 0;
        error_flag = 0;
        sensor_pos = 0;
        read_command();
    }

    //enciende el motor con RPM = motor_speed
    timerInit(motor_speed);

    //funciona hasta que se pida desactivar
    while (system_activated)
    {
        unsigned long timer = 970 / read_speed;
        unsigned long tWait = 3000 / read_speed;
        
        if (checkTime)
        { // si el checador está activo
            checkTime = chkTime(tActual, tWait);
            if (!checkTime)
                sensor_pos = 0;  // forzamos volver al estado 0
        }
        
        /*Logica de estados*/
        switch (sensor_pos)
        {
            case 0: // estado 0, esperando ficha
                estado = lectura(0, top_color); // obtenemos el estado de S1
                if (estado == 2 || estado == 1)
                { // por la lógica de fichas, si existe una ficha, ya sea correcta o no.
                    sensor_pos = 1; // pasamos al estado 1
                    delay(10);
                }
                break;

            case 1: // estado 1, leyendo sensor 1
                estado = lectura(0, top_color); // obtenemos el estado de S1
                if (estado == 1)
                { // por la lógica de fichas, si existe una ficha y es la ficha esperada
                    #ifdef serial_acierto 
                    Serial.println("Acierto en pos 1");
                    #endif
                    sensor_pos = 2;// pasamos al estado 2
                    tActual = millis(); // tomamos el tiempo de inicio de entrada del conjunto de fichas
                    checkTime = true; // activamos el checador de tiempo por ser el primer sensor
                    delay(timer);
                }
                else if (estado == 2)
                {// por la lógica de fichas, si existe una ficha pero NO es la ficha esperada
                    #ifdef serial_falla 
                    Serial.println("Falla en pos 1");
                    #endif
                    sensor_pos = 4; // pasamos al estado 4
                }
                break;

            case 2: //estado 2, leyendo sensor 2
                estado = lectura(1, mid_color); // obtenemos el estado de S2
                if (estado == 1)
                { //por la lógica de fichas, si existe una ficha y es la ficha esperada
                    #ifdef serial_acierto 
                    Serial.println("Acierto en pos 2");
                    #endif
                    sensor_pos = 3;// pasamos al estado 3
                    delay(timer);
                }
                else if (estado == 2)
                { //por la lógica de fichas, si existe una ficha pero NO es la ficha esperada
                    #ifdef serial_falla 
                    Serial.println("Falla en pos 2");
                    #endif
                    sensor_pos = 4; // pasamos al estado 4
                }
                break;

            case 3: //estado 3, leyendo sensor 3  
                estado = lectura(2, bott_color); // obtenemos el estado de S2
                if (estado == 1)
                {// por la lógica de fichas, si existe una ficha y es la ficha esperada
                    #ifdef serial_acierto 
                    Serial.println("Acierto en pos 3");
                    #endif
                    sensor_pos = 5;// pasamos al estado 5
                }
                else if (estado == 2)
                {// por la lógica de fichas, si existe una ficha pero NO es la ficha esperada
                    #ifdef serial_falla
                    Serial.println("Falla en pos 3");
                    #endif
                    sensor_pos = 4; // pasamos al estado 4
                }
                break;

            case 4: //estado 4, contador de errores
                error_count += 1; //incrementamos el contador de errores
                #ifdef serial_success 
                Serial.println("Error numero : " + String(error_count)); 
                #endif
                sensor_pos = 0; //pasamos al estado 0 para esperar nueva ficha
                checkTime = true; //activamos el checador de tiempo
                tActual = millis(); //definimos el tiempo actual para compararlo
                while (checkTime)
                { //esperaremos aqui mientras el tiempo de lectura de fichas no haya llegado al definido (2500/velocidad del motor)
                    checkTime = chkTime(tActual, tWait);
                }
                break;
                
            case 5: //estado 5, contador de aciertos
                success_count += 1; //incrementamos el contador de aciertos
                #ifdef serial_success
                Serial.println("Exito numero : " + String(success_count)); 
                #endif
                sensor_pos = 0;
                checkTime = true; //activamos el checador de tiempo
                tActual = millis(); //definimos el tiempo actual para compararlo
                while (checkTime)
                { //esperaremos aqui mientras el tiempo de lectura de fichas no haya llegado al definido (2500/velocidad del motor)
                    checkTime = chkTime(tActual, tWait);
                }
        }
        //lee comando solo cuando el estado esta en 0
        if(!sensor_pos)
          read_command();
          
        if (!system_activated)
        {
            Serial.println(success_count);
        }
    }
}

void timerConfig()
{
    TCCR2A = 0b00100011; //fast PWM, OC2B(pin3)
    TCCR2B = 0b00001000; //top = OCRA
}

void timerOff()
{
    TCCR2B &= ~(1 << CS22 | 1 << CS21 | 1 << CS20);
}

void timerInit(uint8_t opc)
{
    TCNT2 = 0;
    switch (opc)
    {
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


float GetMax(float r, float g, float b)
{
    float maxx = r;

    if (g > maxx)
        maxx = g;
    if (b > maxx)
        maxx = b;

    return maxx;
}
void SensorPicker(byte x)
{
    if (x > 7)
        return;
    Wire.beginTransmission(TCAADDR);
    Wire.write(1 << x);
    Wire.endTransmission();
}
int colorSense(byte x) ///funcion sensado color
{
    SensorPicker(x);
    float r, g, b, c; // declaramos variables para rojo 'r', verde 'g' y azul 'b'.                    //r       g         b       c
    ColorSensor.getRGB(&r,&g,&b);
    #ifdef serial_color_porciento 
    Serial.println("rojo : " + String(r) + "  verde : " + String(g) + " azul : " + String(b)+ " clear : " + String(c));
    #endif
    float Max = GetMax(r, g, b); // obtenemos el color más grande entre los tres

    if (Max >= 90) // si el máximo es mayor o igual a 2 significa que hay un cambio en los colores, de otro modo no hay color presente y todos valen 1
    {
        if (Max == r)// si el mayor es el rojo
        {
            if (g >= ((r*.9)-(motor_speed*motor_speed))) // preguntamos si la suma del verde y el azul es mayor al rojo, de ser cierto significa que el color es amarillo (combinación de rojo y verde)
            {
              #ifdef serial_color 
              Serial.println("Es Amarillo"); 
              #endif
              return 3;
            }
            else // de otro modo, al g+b no ser mayores que r, significa que el color es completamente rojo
            {
              #ifdef serial_color 
              Serial.println("Es Rojo"); 
              #endif
              return 2;
            }
        }
        //else if(Max==g){}// si el mayor es verde
        //
        else if (Max == b) // si el mayor es azul
        {
          #ifdef serial_color 
          Serial.println("Es Azul"); 
          #endif
          return 1;
        }
        else // de otro modo el mayor es verde
        {    
          #ifdef serial_color 
          //Serial.println("Es Verde"); 
          #endif
          return 0;
        }
    }
    else
        return 0;
}

void read_command()
{
    if (Serial.available())
    {
        command = Serial.readString();
        motor_speed = command.charAt(0) - '0';
        top_color = command.charAt(1) - '0';
        mid_color = command.charAt(2) - '0';
        bott_color = command.charAt(3) - '0';
        system_activated = command.charAt(4) - '0';
        read_speed = motor_speed;

        //Serial.println(String(command) + "\n RPM:" + String(motor_speed) + "\n Top:" + String (top_color) + "\n Mid:" + String(mid_color) + "\n Bot:" + String(bott_color) + "\n State:" + String(system_activated));
    }
}
