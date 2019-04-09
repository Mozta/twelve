#include "Adafruit_TCS34725.h"

//descomentar para usar el monitor serial de Arduino 
//#define serial_arduino

#define TCAADDR 0x70

Adafruit_TCS34725 ColorSensor = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

//declaración e inicializacion de variables
bool error_flag = 0, system_activated = 0;
int top_color = 0, mid_color = 0, bott_color = 0;//1-blue, 2-red, 3-yellow
int sensor_pos = 0;
byte motor_speed = 1;
int error_count = 0;
String command = "";

int read_speed = 1;
float tActual;
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

bool chkTime(float referenceTime, float umbralTime)
{
    float diffT = (millis() - referenceTime); // medimos la diferencia de tiempo entre la entrada de una ficha y el tiempo actual
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
        float timer = 1000 / read_speed;
        float tWait = 2500 / read_speed;


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
                    //Serial.println("Esperando Ficha, estado : "+String(estado)+ "Aciertos = "+String(success_count));
                estado = lectura(0, top_color); // obtenemos el estado de S1
                if (estado == 2 || estado == 1)
                { // por la lógica de fichas, si existe una ficha, ya sea correcta o no.
                    sensor_pos = 1; // pasamos al estado 1
                }
                break;

            case 1: // estado 1, leyendo sensor 1
                    //Serial.println("Case 1 , estado : "+String(estado)+", color por leer : "+String(top_color)+ "Aciertos = "+String(success_count));
                estado = lectura(0, top_color); // obtenemos el estado de S1
                if (estado == 1)
                { // por la lógica de fichas, si existe una ficha y es la ficha esperada
                   // Serial.println("Acierto en pos 1");
                    sensor_pos = 2;// pasamos al estado 2
                    tActual = millis(); // tomamos el tiempo de inicio de entrada del conjunto de fichas
                    checkTime = true; // activamos el checador de tiempo
                    delay(timer);
                }
                else if (estado == 2)
                {
                    //Serial.println("Falla en pos 1");
                    sensor_pos = 4;
                }
                break;

            case 2: // estado 2, leyendo sensor 2
                   // Serial.println("Case 2 , estado : "+String(estado)+", color por leer : "+String(mid_color)+ "Aciertos = "+String(success_count));
                estado = lectura(1, mid_color); // obtenemos el estado de S2
                if (estado == 1)
                { // por la lógica de fichas, si existe una ficha y es la ficha esperada
                   // Serial.println("Acierto en pos 2");
                    sensor_pos = 3;// pasamos al estado 3
                                   //estado=false;
                    delay(timer);
                }
                else if (estado == 2)
                {
                    //Serial.println("Falla en pos 2");
                    sensor_pos = 4;
                }
                break;

            case 3: // estado 3, leyendo sensor 3  
                   // Serial.println("Case 3 , estado : "+String(estado)+", color por leer : "+String(bott_color)+ "Aciertos = "+String(success_count)); 
                estado = lectura(2, bott_color); // obtenemos el estado de S2
                if (estado == 1)
                { // por la lógica de fichas, si existe una ficha y es la ficha esperada
                    //Serial.println("Acierto en pos 3");
                    sensor_pos = 5;// pasamos al estado 5
                                   //estado=false;
                }
                else if (estado == 2)
                {
                    //Serial.println("Falla en pos 3");
                    sensor_pos = 4;
                }
                break;

            case 4: // estado 4, contador de errores
                error_count += 1;
                sensor_pos = 0;
                checkTime = true; // activamos el checador de tiempo
                tActual = millis();
                while (checkTime)
                { // si el checador está activo
                    checkTime = chkTime(tActual, tWait);
                }
                break;

            case 5: //estado 5, contador de aciertos
                success_count += 1;
                sensor_pos = 0;
                checkTime = true; // activamos el checador de tiempo
                tActual = millis();
                while (checkTime)
                { // si el checador está activo
                    checkTime = chkTime(tActual, tWait);
                }

        }
        //lee comnado
        read_command();

        if (!system_activated)
        {
            Serial.print(success_count);
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


uint16_t GetMax(uint16_t r, uint16_t g, uint16_t b)
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
    uint16_t r, g, b, c; // declaramos variables para rojo 'r', verde 'g' y azul 'b'
    ColorSensor.getRawData(&r, &g, &b, &c); // obtenemos los valores RGB con formato de 16bits
    //Serial.println("rojo : " + String(r) + "  verde : " + String(g) + " azul : " + String(b)+ " clear : " + String(c));
    uint16_t Max = GetMax(r, g, b); // obtenemos el color más grande entre los tres

    if (Max >= 500) // si el máximo es mayor o igual a 2 significa que hay un cambio en los colores, de otro modo no hay color presente y todos valen 1
    {
        if (Max == r)// si el mayor es el rojo
        {
            if (g >= r*.6) // preguntamos si la suma del verde y el azul es mayor al rojo, de ser cierto significa que el color es amarillo (combinación de rojo y verde)
            {
                //Serial.println("Es Amarillo");
                return 3;
            }
            else // de otro modo, al g+b no ser mayores que r, significa que el color es completamente rojo
            {
                //Serial.println("Es Rojo");
                return 2;
            }
        }
        //else if(Max==g) // si el mayor es verde
        //
        else if (Max == b) // si el mayor es azul
        {
            //Serial.println("Es Azul");
            return 1;
        }
        else // de otro modo el mayor es verde
        {    
          //Serial.println("Es Verde");
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

# ifdef serial_arduino
        Serial.println(command);
        Serial.print("RPM:");
        Serial.print(motor_speed);
        Serial.print(" Top:");
        Serial.println(top_color);
        Serial.print(" Mid:");
        Serial.println(mid_color);
        Serial.print(" Bot:");
        Serial.println(bott_color);
        Serial.print(" State:");
        Serial.println(system_activated);
#endif
    }
}
