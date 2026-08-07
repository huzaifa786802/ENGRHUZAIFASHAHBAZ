#include <Arduino.h>
#include <WiFi.h>            // Use <ESP8266WiFi.h> for ESP8266
#include <BlynkSimpleEsp8266.h> // Use <BlynkSimpleEsp8266.h> for ESP8266
// Blynk credentials
#define BLYNK_TEMPLATE_ID "TMPL6QkR1xiMt"
#define BLYNK_DEVICE_NAME "AIRQULAITYINDEX"
#define BLYNK_AUTH_TOKEN "aCW4BGaSVWaLGuM6qncZy1qQpoXD_6nj"
// Wi-Fi credentials
char ssid[] = "HUZAIFASHAHBAZ";
char pass[] = "huzaf12345786";
// Pin definitions
const int MQ5_PIN = 34;    // GPIO34 for MQ-5
const int MQ135_PIN = 35;  // GPIO35 for MQ-135
void setup() {
    Serial.begin(115200);
    Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass); // Connect to Blynk Cloud
}
void loop() {
    // Read sensor values
    int mq5_value = analogRead(MQ5_PIN);      // Read MQ-5 value
    int mq135_value = analogRead(MQ135_PIN); // Read MQ-135 value
    // Print to Serial Monitor
    Serial.print("MQ-5 Value: ");
    Serial.println(mq5_value);
    Serial.print("MQ-135 Value: ");
    Serial.println(mq135_value);
    // Send data to Blynk
    Blynk.virtualWrite(V1, mq5_value);  // Send MQ-5 data to Virtual Pin V1
    Blynk.virtualWrite(V2, mq135_value); // Send MQ-135 data to Virtual Pin V2
    Blynk.run(); // Keep Blynk connected
}