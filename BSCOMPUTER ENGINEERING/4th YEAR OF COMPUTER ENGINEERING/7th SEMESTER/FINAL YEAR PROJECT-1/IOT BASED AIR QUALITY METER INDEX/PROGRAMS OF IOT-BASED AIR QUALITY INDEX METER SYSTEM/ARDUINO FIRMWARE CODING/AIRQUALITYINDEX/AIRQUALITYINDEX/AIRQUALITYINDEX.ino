// Pin definitions
const int mq5Pin = A0;     // MQ-5 analog pin connected to A0
const int mq135Pin = A1;   // MQ-135 analog pin connected to A1
// Variables to store sensor values
int mq5Value = 0;
int mq135Value = 0;
void setup() {
  Serial.begin(9600);      // Start serial communication
  pinMode(mq5Pin, INPUT);
  pinMode(mq135Pin, INPUT);
}
void loop() {
  // Read analog values from sensors
  mq5Value = analogRead(mq5Pin);
  mq135Value = analogRead(mq135Pin);
  // Print readings to Serial Monitor
  Serial.print("MQ-5 Sensor Value: ");
  Serial.print(mq5Value);
  Serial.print(" | MQ-135 Sensor Value: ");
  Serial.println(mq135Value);
  // Delay for stable output
  delay(1000);
}