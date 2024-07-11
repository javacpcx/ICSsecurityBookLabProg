#ifdef ESP8266
#include <ESP8266WiFi.h>
#else //ESP32
#include <WiFi.h>
#endif
#include <ModbusIP_ESP8266.h>
const int LED_COIL = 100; //Modbus Registers Offsets
int ledPin = 2; //Used Pins, 2 = D4 = GPIO2 
const char* ssid = "talin5801-6F";
const char* password = "qwe-123456";
WiFiServer server(8080);
ModbusIP mb; //ModbusIP object
void setup() {
  Serial.begin(115200);
  mb.server();
  pinMode(ledPin, OUTPUT);
  mb.addCoil(LED_COIL);
  delay(10);
  Serial.println(); // Connect to WiFi network  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  server.begin();  // Start the server
  Serial.println("Server started");
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());   // Print the IP address
  Serial.println("/");
}
void loop() {
  mb.task();   //Call once inside loop() - all magic here
  digitalWrite(LED_BUILTIN, mb.Coil(LED_COIL));  //Attach ledPin to LED_COIL register
  WiFiClient client = server.available();  // Check if a client has connected
  if (!client) { // Wait until the client sends some data
    return;
  }
  Serial.println("new client");  
  while (!client.available()) {
    delay(1);
  }
  String request = client.readStringUntil('\r');   // Read the first line of the request
  Serial.println(request);
  client.flush();   // Match the request
  int value = HIGH;
  if (request.indexOf("/LED=ON") != -1)  {
    digitalWrite(ledPin, HIGH);
    value = HIGH;
  }
  if (request.indexOf("/LED=OFF") != -1)  {
    digitalWrite(ledPin, LOW);
    value = LOW;
  }
  client.println("HTTP/1.1 200 OK");   // Return the response
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.print("LED pin is now: ");
  if (value == LOW) {
    client.print("Off");
  } else {
    client.print("On");
  }
  client.println("<br><br>");
  client.println("<a href=\"/LED=ON\"\"><button>Turn On </button></a>");
  client.println("<a href=\"/LED=OFF\"\"><button>Turn Off </button></a><br />");
  client.println("</html>");
  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");
}
