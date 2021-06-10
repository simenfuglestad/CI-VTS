#include <OneWire.h>
#include <DallasTemperature.h>
 
// Data wire is conntec to the Arduino digital pin 4
#define ONE_WIRE_BUS 4
// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);
unsigned long currentTime = millis();
unsigned long prevTime = 0;

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
int ir_led3 = 3; //left IR LED
int ir_led6 = 6; //bottom IR LED
int ir_led5 = 5; //right side IR LED
int ir_led9 = 9; //stimulus COB LED

void setup() {
    //Thermometer sensors
  sensors.begin();
  // initialize serial:
//  setPwmFrequency(ir_leds, 1);

  Serial.begin(115200); //baudrate for serial communication
  Serial.setTimeout(5); //timeout for serial communication

  //circuit never read, only need outputs
  pinMode(ir_led3, OUTPUT);
  pinMode(ir_led6, OUTPUT);
  pinMode(ir_led5, OUTPUT);
  pinMode(ir_led9, OUTPUT);
}

void loop() {
 /*
  * Continous scan for incoming data on serial port.
  * Serial data is always a formatted string with a header and a value
  * Example: "ir330" is directed to pin 3 with a value of 30
  * Values are mapped from a percentage range to an 8-bit range (0-255)
  * Once value is written, input string is cleared and new serial data can be read
  */
  
  if(Serial.available() == 0)
  {
    if(currentTime - prevTime >= 5000) 
    {
      String temp_str = String(getTemp(),2);
      temp_str = temp_str + " Degrees Celsius.";
      Serial.write(temp_str.c_str());
      Serial.write("/r/n"); //Nødvendig? 
      prev_time = current_time;
    }
  }
  
  // print the string when a newline arrives:
 if(Serial.available()) {
    inputString = Serial.readString();
    Serial.flush();
   }
   if(inputString.startsWith("irPWM")) {
    int val = inputString.substring(5,inputString.length()).toInt();
    setPwmFrequency(ir_led3, val);
    //clear the string:
    inputString = "";
   }

    else if (inputString.startsWith("sl")) {
      int val = inputString.substring(2,inputString.length()).toInt();
      Serial.println(val);
      val = map(val, 0, 100, 0, 255);
      analogWrite(ir_led9, val);
      inputString = "";
   }

  else if (inputString.startsWith("ir3")){
    int val = inputString.substring(3,inputString.length()).toInt();
    val = map(val, 0, 100, 0, 255);
    analogWrite(ir_led3, val);
     //clear the string:
    inputString = "";
   }
  else if (inputString.startsWith("ir5")){
    int val = inputString.substring(3,inputString.length()).toInt();
    val = map(val, 0, 100, 0, 255);
    analogWrite(ir_led5, val);
     //clear the string:
    inputString = "";
   }
  else if (inputString.startsWith("ir6")){
    int val = inputString.substring(3,inputString.length()).toInt();
    val = map(val, 0, 100, 0, 255);
    analogWrite(ir_led6, val);
     //clear the string:
    inputString = "";
   }
 }

void setPwmFrequency(int pin, int divisor) {
  /*
   * Alter internal register of Arduino device to upscale frequency of PWM
   * Not intended for frequent use
   */

  byte mode;
  if(pin == 5 || pin == 6 || pin == 9 || pin == 10) {
    switch(divisor) {
      case 1: mode = 0x01; break;
      case 8: mode = 0x02; break;
      case 64: mode = 0x03; break;
      case 256: mode = 0x04; break;
      case 1024: mode = 0x05; break;
      default: return;
    }
    if(pin == 5 || pin == 6) {
      TCCR0B = TCCR0B & 0b11111000 | mode;
    } else {
      TCCR1B = TCCR1B & 0b11111000 | mode;
    }
  } else if(pin == 3 || pin == 11) {
    switch(divisor) {
      case 1: mode = 0x01; break;
      case 8: mode = 0x02; break;
      case 32: mode = 0x03; break;
      case 64: mode = 0x04; break;
      case 128: mode = 0x05; break;
      case 256: mode = 0x06; break;
      case 1024: mode = 0x07; break;
      default: return;
    }
    TCCR2B = TCCR2B & 0b11111000 | mode;
  }
}
float getTemp()
{
  sensors.requestTemperatures(); 
  float temp = sensors.getTempCByIndex(0);
  return temp;
  
}
