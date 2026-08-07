#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#define GPS_RX_PIN 4
#define GPS_TX_PIN 3
#define RF_RX_PIN 5
#define RF_TX_PIN 6
#define SERVO_PIN 9
#define SPEED_SENSOR_PIN 2
#define SPEED_LIMIT_URBAN 50
#define SPEED_LIMIT_HIGHWAY 100
#define UPDATE_INTERVAL 1000
TinyGPSPlus gps;
SoftwareSerial gpsSerial(GPS_RX_PIN, GPS_TX_PIN);
SoftwareSerial rfSerial(RF_RX_PIN, RF_TX_PIN);
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo throttleServo;
float currentSpeed = 0.0;
float targetSpeed = 0.0;
unsigned long lastUpdate = 0;
volatile unsigned long pulseCount = 0;
bool isControlEnabled = true;
void speedPulse() {
  pulseCount++;
}
void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600);
  rfSerial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.clear();
  throttleServo.attach(SERVO_PIN);
  throttleServo.write(0);
  pinMode(SPEED_SENSOR_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(SPEED_SENSOR_PIN), speedPulse, RISING);
  lcd.setCursor(0, 0);
  lcd.print("Speed: ");
  lcd.setCursor(0, 1);
  lcd.print("Target: ");
}
void loop() {
  if (millis() - lastUpdate >= UPDATE_INTERVAL) {
    updateSpeed();
    processGPS();
    checkRFCommands();
    updateDisplay();
    controlSpeed();
    lastUpdate = millis();
    pulseCount = 0;
  }
}
void updateSpeed() {
  currentSpeed = (pulseCount * 2.25 * 3600) / 1000.0;
}
void processGPS() {
  while (gpsSerial.available() > 0) {
    if (gps.encode(gpsSerial.read())) {
      if (gps.location.isValid()) {
        if (isUrbanArea(gps.location.lat(), gps.location.lng())) {
          targetSpeed = SPEED_LIMIT_URBAN;
        } else {
          targetSpeed = SPEED_LIMIT_HIGHWAY;
        }
      }
    }
  }
}
bool isUrbanArea(float lat, float lng) {
  return true;
}
void checkRFCommands() {
  if (rfSerial.available()) {
    char command = rfSerial.read();
    switch (command) {
      case 'E':
        isControlEnabled = true;
        break;
      case 'D':
        isControlEnabled = false;
        throttleServo.write(0);
        break;
      case 'S':
        if (rfSerial.available() >= 2) {
          targetSpeed = rfSerial.parseInt();
        }
        break;
    }
  }
}
void updateDisplay() {
  lcd.setCursor(7, 0);
  lcd.print("     ");
  lcd.setCursor(7, 0);
  lcd.print(currentSpeed, 1);
  lcd.setCursor(8, 1);
  lcd.print("     ");
  lcd.setCursor(8, 1);
  lcd.print(targetSpeed, 1);
}
void controlSpeed() {
  if (!isControlEnabled) return;
  float speedError = targetSpeed - currentSpeed;
  int throttlePosition = map(constrain(speedError, -10, 10), -10, 10, 0, 180);
  throttleServo.write(throttlePosition);
}