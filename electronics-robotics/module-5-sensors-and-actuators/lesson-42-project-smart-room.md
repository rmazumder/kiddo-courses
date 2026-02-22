# Lesson 42: Module 5 Project -- The Smart Room System

**Module:** 5 -- Sensors and Actuators (FINAL PROJECT)
**Difficulty:** Star-4 Advanced
**Session Time:** 60--75 minutes (longer -- it is a project!)
**Age:** 6--12 years
**XP Available:** 500 XP (the biggest XP haul of the module!)

---

## Your Mission Today

This is it, Circuit Explorer -- the GRAND FINALE of Module 5! You have spent 7 lessons learning about sensors that see, feel, and hear, and actuators that move and spin. Now you are going to bring them ALL together into one epic project: a **Smart Room System** that monitors temperature, detects motion, measures distance, and reacts automatically. When you are done, you will have a miniature smart home sitting on your desk!

---

## Learning Objectives

This project brings together everything from Module 5:
- Sensors: DHT11 (temperature/humidity), LDR (light), HC-SR04 (distance), PIR (motion)
- Actuators: Servo motor, LEDs, buzzer
- Display: 16x2 LCD with I2C
- Coding: Combining multiple sensor inputs to control multiple outputs
- Wand skills: System-wide voltage and signal verification

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| DHT11 temperature sensor | 1 |
| LDR + 10k-ohm resistor | 1 each |
| HC-SR04 ultrasonic sensor | 1 |
| PIR motion sensor (HC-SR501) | 1 |
| SG90 servo motor | 1 |
| LEDs (green, yellow, red) | 1 each |
| 330-ohm resistors | 3 |
| Active buzzer | 1 |
| 16x2 LCD with I2C backpack | 1 |
| 10k-ohm resistor (DHT11 pull-up) | 1 |
| Breadboard (830-point recommended) | 1 |
| Jumper wires | 20+ |
| Multimeter (Magic Measurement Wand) | 1 |

---

## Smart Room System Features

Your Smart Room will have 4 smart features:

```
  +==================================================+
  |           SMART ROOM SYSTEM v1.0                  |
  |                                                   |
  |  Feature 1: CLIMATE MONITOR                       |
  |  - DHT11 reads temp and humidity                  |
  |  - LCD displays current readings                  |
  |  - Red LED warns if too hot (>28 C)               |
  |                                                   |
  |  Feature 2: AUTO NIGHT LIGHT                      |
  |  - PIR detects motion                             |
  |  - LDR checks if it is dark                       |
  |  - Green LED turns on only at night + motion      |
  |                                                   |
  |  Feature 3: PROXIMITY ALERT                       |
  |  - HC-SR04 measures distance                      |
  |  - Buzzer beeps when object < 15 cm               |
  |  - Yellow LED shows "something nearby"            |
  |                                                   |
  |  Feature 4: SERVO GATE                            |
  |  - Servo acts as a gate or barrier                |
  |  - Opens (90 degrees) when motion detected        |
  |  - Closes (0 degrees) after 5 seconds             |
  |                                                   |
  +==================================================+
```

---

## How to Build It

### Phase 1: Plan and Wire All Sensors (15 min)

**Master wiring plan:**

```
  Component         Arduino Pin       Notes
  ---------         -----------       -----
  DHT11 Signal      Pin 2             + 10k pull-up to 5V
  PIR OUT           Pin 4
  HC-SR04 Trig      Pin 9
  HC-SR04 Echo      Pin 10
  Servo Signal      Pin 6             PWM pin
  Buzzer            Pin 8
  Red LED           Pin 13            Too hot warning
  Yellow LED        Pin 12            Proximity alert
  Green LED         Pin 11            Night light
  LDR               A0                With 10k voltage divider
  LCD SDA           A4                I2C
  LCD SCL           A5                I2C

  Power:
  All VCC ----------> Arduino 5V
  All GND ----------> Arduino GND (use breadboard power rail)
```

**Wire one sensor at a time.** Test each one individually before connecting the next. This makes debugging MUCH easier.

> "Professional engineers never build an entire system at once. They build and test one piece, then add the next. If something breaks, they know exactly which piece caused the problem."

**Award: +40 XP for wiring all sensors and actuators!**

---

### Phase 2: Build Feature 1 -- Climate Monitor (10 min)

Start with the temperature display:

```cpp
#include <DHT.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

// --- Pin Definitions ---
#define DHTPIN 2
#define DHTTYPE DHT11
#define PIR_PIN 4
#define TRIG_PIN 9
#define ECHO_PIN 10
#define SERVO_PIN 6
#define BUZZER_PIN 8
#define RED_LED 13
#define YELLOW_LED 12
#define GREEN_LED 11
#define LDR_PIN A0

// --- Objects ---
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo gateServo;

// --- Settings ---
float hotThreshold = 28.0;    // Celsius
int darkThreshold = 300;       // LDR value below this = dark
int proximityThreshold = 15;   // cm
unsigned long gateOpenTime = 0;
int gateDuration = 5000;       // 5 seconds

void setup() {
  // Initialize serial
  Serial.begin(9600);

  // Initialize sensors
  dht.begin();

  // Initialize LCD
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Smart Room v1.0");
  lcd.setCursor(0, 1);
  lcd.print("Starting up...");

  // Initialize pins
  pinMode(PIR_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  // Initialize servo
  gateServo.attach(SERVO_PIN);
  gateServo.write(0);  // Gate closed

  // PIR warm-up
  Serial.println("PIR warming up... (30 sec)");
  delay(30000);

  lcd.clear();
  Serial.println("Smart Room ACTIVE!");
}
```

> "This setup block initializes EVERYTHING at once. Notice how we give the PIR 30 seconds to warm up before the system goes active."

**Award: +30 XP for building the climate monitor!**

---

### Phase 3: Build All Four Features in the Loop (15 min)

```cpp
void loop() {
  // ======= FEATURE 1: Climate Monitor =======
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();

  if (!isnan(temp) && !isnan(humid)) {
    // Display on LCD (top row)
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temp, 1);
    lcd.print("C H:");
    lcd.print(humid, 0);
    lcd.print("%  ");

    // Hot warning
    if (temp > hotThreshold) {
      digitalWrite(RED_LED, HIGH);
    } else {
      digitalWrite(RED_LED, LOW);
    }
  }

  // ======= FEATURE 2: Auto Night Light =======
  int motion = digitalRead(PIR_PIN);
  int lightLevel = analogRead(LDR_PIN);

  if (motion == HIGH && lightLevel < darkThreshold) {
    digitalWrite(GREEN_LED, HIGH);
  } else {
    digitalWrite(GREEN_LED, LOW);
  }

  // ======= FEATURE 3: Proximity Alert =======
  int distance = getDistance();

  lcd.setCursor(0, 1);
  lcd.print("Dist:");
  lcd.print(distance);
  lcd.print("cm ");

  if (distance < proximityThreshold && distance > 0) {
    digitalWrite(YELLOW_LED, HIGH);
    tone(BUZZER_PIN, 2000, 100);
    lcd.setCursor(12, 1);
    lcd.print("NEAR");
  } else {
    digitalWrite(YELLOW_LED, LOW);
    noTone(BUZZER_PIN);
    lcd.setCursor(12, 1);
    lcd.print("    ");
  }

  // ======= FEATURE 4: Servo Gate =======
  if (motion == HIGH) {
    gateServo.write(90);   // Open gate
    gateOpenTime = millis();
    Serial.println("Gate OPEN -- motion detected!");
  }

  if (millis() - gateOpenTime > gateDuration) {
    gateServo.write(0);    // Close gate after 5 seconds
  }

  // ======= Status Report to Serial =======
  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print("C | Humid: ");
  Serial.print(humid);
  Serial.print("% | Light: ");
  Serial.print(lightLevel);
  Serial.print(" | Dist: ");
  Serial.print(distance);
  Serial.print("cm | Motion: ");
  Serial.println(motion ? "YES" : "no");

  delay(500);
}

// ======= Helper Function: Get Distance =======
int getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);  // 30ms timeout
  if (duration == 0) return 999;  // No echo = far away
  return duration * 0.034 / 2;
}
```

**Test each feature:**
1. **Climate:** Check LCD shows temperature and humidity. Breathe on DHT11 -- values should change
2. **Night light:** Cover the LDR (make it dark) and wave your hand near PIR -- green LED lights up
3. **Proximity:** Move your hand toward the HC-SR04 -- buzzer beeps when close
4. **Gate:** Walk past the PIR -- servo opens and closes after 5 seconds

**Award: +50 XP for getting all 4 features working!**

---

### Phase 4: Wand Check -- System-Wide Verification (10 min)

> "You built a complex system with 4 sensors and multiple outputs. Now it is time for a full Wand inspection -- just like an engineer would check every subsystem before shipping a product!"

**Wand Test -- Full System Check:**

```
| Test | How | Expected | Your Reading | Points |
|------|-----|----------|-------------|--------|
| Arduino 5V rail | DC Volts: 5V pin to GND | ~4.8-5.2V | | +10 XP |
| DHT11 VCC | DC Volts: DHT11 VCC to GND | ~4.8-5.0V | | +10 XP |
| PIR output (no motion) | DC Volts: PIR OUT to GND | ~0V | | +10 XP |
| PIR output (motion) | DC Volts: PIR OUT while waving | ~3.3V | | +10 XP |
| HC-SR04 VCC | DC Volts: sensor VCC to GND | ~4.8-5.0V | | +10 XP |
| LDR voltage (bright) | DC Volts: A0 pin to GND | ~3-5V | | +10 XP |
| LDR voltage (dark) | DC Volts: A0 pin to GND (covered) | ~0.5-2V | | +10 XP |
```

> "You just did what real engineers call a 'systems integration test.' Every subsystem gets checked with an instrument to make sure it is operating within specifications. If any reading is off, you know exactly where to look for the problem!"

**Award: +70 XP for the full system Wand check!**

---

### Phase 5: Customize and Decorate (10 min)

**Make it your own:**

- Adjust `hotThreshold` to a temperature that makes sense for your room
- Change `darkThreshold` based on your LDR readings
- Modify `proximityThreshold` for closer or farther detection
- Change `gateDuration` for a longer or shorter gate open time
- Add more features: a second buzzer tone, flashing LEDs, custom LCD messages

**Decoration ideas:**
- Build a small cardboard "room" around your project
- Label each sensor with what it does
- Add a project title card: "Smart Room by [Your Name]"
- Take a photo or video to show family!

**Award: +30 XP for customizing your Smart Room!**

---

### Phase 6: Final Demo Checklist (5 min)

Walk through each feature and demonstrate it to a parent, friend, or teacher:

```
| Feature | Demo Action | Expected Result | Works? |
|---------|------------|-----------------|--------|
| Climate Monitor | Read LCD | Shows temp and humidity | |
| Hot Warning | Hold DHT11 or breathe on it | Red LED turns on if >28C | |
| Night Light | Cover LDR + wave at PIR | Green LED turns on | |
| Proximity Alert | Move hand toward HC-SR04 | Yellow LED + buzzer | |
| Servo Gate | Walk past PIR | Servo opens and closes | |
| LCD Display | Watch it | Shows all readings | |
```

> "You built a REAL smart home system! This is the exact same LOGIC (not scale) that companies like Nest, Ring, and Philips use in their smart home products. They just use fancier parts and WiFi -- the thinking is the same."

**Award: +50 XP for completing the full demo!**

---

## Module 5 Final Assessment

After building the Smart Room, answer these (no looking at notes!):

**Sensor Knowledge:**
1. "Name 4 sensors you used in this module and what each one detects."
2. "What is the difference between a digital sensor (PIR) and an analog sensor (LDR)?"
3. "How does the ultrasonic sensor calculate distance?"

**Actuator Knowledge:**
4. "What is the difference between a servo motor and a DC motor?"
5. "Why do DC motors need a motor driver but servos do not?"

**Wand Skills:**
> "Measure the 5V rail for me." (Hand them the Wand)
> "Show me the PIR output when motion is detected vs not detected."

**Award: +50 XP for completing the final assessment!**

---

## Module 5 Complete -- Grand Finale!

```
  ======================================================

     MODULE 5 CHAMPION BADGE UNLOCKED!

     _____________________ has mastered
        Sensors and Actuators

     [check] Temperature Sensor (DHT11)
     [check] Light Sensor (LDR)
     [check] Ultrasonic Distance Sensor (HC-SR04)
     [check] Servo Motors
     [check] DC Motors and Motor Driver (L298N)
     [check] IR Sensor and Remote Control
     [check] PIR Motion Sensor
     [check] Built the Smart Room System!

  ======================================================
```

**Lesson 42 XP Breakdown:**
| Activity | XP |
|----------|-----|
| Wiring all sensors/actuators | 40 |
| Climate monitor feature | 30 |
| All 4 features working | 50 |
| Full system Wand check (7 tests) | 70 |
| Customization | 30 |
| Final demo | 50 |
| Final assessment | 50 |
| **TOTAL POSSIBLE** | **320** |

---

## Module 5 Total XP Summary

| Lesson | Title | Max XP |
|--------|-------|--------|
| 35 | Temperature Sensor (DHT11) | 210 |
| 36 | Light Sensor (LDR) | 190 |
| 37 | Ultrasonic Distance Sensor (HC-SR04) | 185 |
| 38 | Servo Motors | 185 |
| 39 | DC Motors and Motor Driver (L298N) | 195 |
| 40 | IR Sensor and Remote Control | 165 |
| 41 | PIR Motion Sensor | 190 |
| 42 | Smart Room Project | 320 |
| **MODULE TOTAL** | | **1,640** |

**XP Ranks for Module 5:**
- 0--400 XP: Sensor Apprentice
- 401--800 XP: Sensor Explorer
- 801--1,200 XP: Sensor Specialist
- 1,201--1,500 XP: Sensor Engineer
- 1,501--1,640 XP: Sensor Champion!

---

## All Badges Earned in Module 5

| Badge | Lesson |
|-------|--------|
| Weather Wizard | 35 |
| Light Detective | 36 |
| Echo Master | 37 |
| Servo Commander | 38 |
| Motor Master | 39 |
| IR Code Breaker | 40 |
| Motion Guardian | 41 |
| Module 5 Champion | 42 |

---

## Reflection Questions (Talk Through Together)

> "What was the most surprising sensor to work with?"
> "Which feature of the Smart Room is your favorite?"
> "If you could add one more sensor or feature, what would it be?"
> "Which Magic Measurement Wand check taught you the most?"
> "Do you think you could build a robot now?"

---

## What's Next -- Module 6 Preview

> "You can now sense the world AND make things move. In Module 6, we are going FULL ROBOT! You will build a chassis with wheels, program movement patterns, and teach your robot to follow lines and avoid obstacles on its own. Everything you learned about sensors, motors, and coding comes together to build a REAL autonomous robot!"

---

## Parent/Instructor Notes

- This project takes longer than a regular lesson -- plan for 60--75 minutes or split across two sessions.
- Phase 1 (wiring) is the most error-prone. Encourage methodical, one-sensor-at-a-time testing.
- The Wand check phase is extremely valuable -- it teaches systematic debugging and verification.
- If the full system is overwhelming, it is perfectly fine to implement only 2 or 3 features and add the rest later.
- The complete code can be shared as a reference after the child has attempted it themselves.
- Consider having the child demonstrate the Smart Room to another family member and explain each feature -- teaching solidifies learning.
- The XP totals across all 8 lessons can be tallied on a poster or whiteboard. Many kids become deeply motivated by seeing their cumulative score rise.
- This project naturally leads into Module 6 (Robotics) -- the sensors and motor skills transfer directly to building mobile robots.
