void setup() {
  for (int pin = 2; pin <= 9; pin++) {
    pinMode(pin, OUTPUT);  // Set pins 2 to 9 as outputs
  }
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'B') {  // Command to blink all LEDs
      for (int pin = 2; pin <= 9; pin++) {
        digitalWrite(pin, HIGH);
      }
      delay(500);  // Keep LEDs ON for 500ms
      for (int pin = 2; pin <= 9; pin++) {
        digitalWrite(pin, LOW);
      }
      delay(500);  // Keep LEDs OFF for 500ms
    }
  }
}