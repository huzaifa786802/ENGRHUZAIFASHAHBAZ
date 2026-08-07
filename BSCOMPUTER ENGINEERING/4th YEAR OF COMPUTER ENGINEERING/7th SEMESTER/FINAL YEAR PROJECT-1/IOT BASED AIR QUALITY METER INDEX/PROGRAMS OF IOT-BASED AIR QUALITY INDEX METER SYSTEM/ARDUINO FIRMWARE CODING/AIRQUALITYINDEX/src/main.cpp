#include <Arduino.h>
// Pin definitions for MQ sensors
#define MQ5_PIN A0     // MQ-5 sensor analog pin
#define MQ135_PIN A1   // MQ-135 sensor analog pin
void setup() {
    // Initialize USB serial communication (for debugging on PC)
    Serial.begin(9600);
    Serial.println("System is starting...");
    // Set MQ sensor pins as input (optional since analog pins are input by default)
    pinMode(MQ5_PIN, INPUT);
    pinMode(MQ135_PIN, INPUT);
    Serial.println("Setup complete.");
}
void loop() {
    // Read analog values from MQ-5 and MQ-135 sensors
    int mq5Value = analogRead(MQ5_PIN);
    int mq135Value = analogRead(MQ135_PIN);
    // Convert analog values to gas concentration percentage (arbitrary scaling)
    float mq5Concentration = (mq5Value / 1023.0) * 100.0;   // Scale to percentage
    float mq135Concentration = (mq135Value / 1023.0) * 100.0; // Scale to percentage
    // Print sensor values to the Serial Monitor (via USB)
    Serial.print("MQ-5 Gas Level: ");
    Serial.print(mq5Concentration);
    Serial.println(" %");
    Serial.print("MQ-135 Gas Level: ");
    Serial.print(mq135Concentration);
    Serial.println(" %");
    // Add a delay to avoid overwhelming serial communication
    delay(1000); // 1-second delay
}