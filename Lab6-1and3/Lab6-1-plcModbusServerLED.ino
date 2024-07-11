#ifdef ESP8266
 #include <ESP8266WiFi.h>
#else //ESP32
 #include <WiFi.h>
#endif
#include <ModbusIP_ESP8266.h>

//Modbus Registers Offsets
const int LED_COIL_R = 0;
const int LED_COIL_G = 5;
const int LED_COIL_Y = 9;
//Used Pins
const int ledPinR = 16; //GPIO16
const int ledPinY = 12; //GPIO12
const int ledPinG = 13; //GPIO13
const int LED_BUILTIN = 2; //ledBink
const int addHREG1 = 0;
const int addHREG2 = 6;

//ModbusIP object
ModbusIP mb;
  
void setup() {
  Serial.begin(115200);
  WiFi.begin("talin5801-6F", "qwe-123456");
   while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  mb.server();
  pinMode(ledPinR, OUTPUT);
  pinMode(ledPinY, OUTPUT);
  pinMode(ledPinG, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  mb.addCoil(LED_COIL_R,1); //設定線圈位址LED_COIL_R為TRUE
  mb.addCoil(LED_COIL_Y,1); //設定線圈位址LED_COIL_Y為TRUE
  mb.addCoil(LED_COIL_G,1); //設定線圈位址LED_COIL_G為TRUE 
  mb.addHreg(addHREG1, 0xAB); 
//設定暫存器位址addREG1為16進位AB等於十進位171
  mb.addHreg(addHREG2, 0x99); 
//設定暫存器位址addREG2為16進位99等於十進位153
}
 
void loop() {
   //Call once inside loop() - all magic here
   mb.task();
   //Attach ledPin to LED_COIL register
   digitalWrite(ledPinR, mb.Coil(LED_COIL_R));
   digitalWrite(ledPinY, mb.Coil(LED_COIL_Y));
   digitalWrite(ledPinG, mb.Coil(LED_COIL_G));
   digitalWrite(LED_BUILTIN, HIGH);//在ESP32上的二極體電位高   
   delay(1000); //延遲1秒,1秒=1000
   digitalWrite(LED_BUILTIN, LOW);//在ESP32上的二極體電位低
   digitalWrite(ledPinR, LOW);
   digitalWrite(ledPinY, LOW);
   digitalWrite(ledPinG, LOW);
   delay(1000);
   Serial.println(LED_COIL_R);
   Serial.println(mb.Coil(LED_COIL_R));
}
