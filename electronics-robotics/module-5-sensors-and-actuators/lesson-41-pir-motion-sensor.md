# Lesson 41: PIR Motion Sensor -- Your Arduino's Security Guard

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 275 XP

---

## Your Mission Today

Circuit Explorer, imagine this: you walk into a dark hallway and the light turns on automatically. You leave, and it turns itself off. No switch, no voice command -- the hallway just KNOWS you are there. How? A tiny sensor called a **PIR motion sensor** detects your body heat as you move through the area. Today you are building your own automatic security light system!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how PIR sensors detect motion using body heat
- Wire a PIR sensor to Arduino
- Write a sketch that reacts to motion detection
- Build an automatic security light with an adjustable timer
- Combine PIR with an LDR to make a smart night-only motion light
- Use your Magic Measurement Wand to measure the PIR output pin HIGH vs LOW

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| HC-SR501 PIR motion sensor module | 1 |
| LEDs (any color) | 2 |
| 330-ohm resistors | 2 |
| Active buzzer (optional for alarm mode) | 1 |
| LDR + 10k-ohm resistor (from Lesson 36) | 1 each |
| Breadboard | 1 |
| Jumper wires | 8 |
| Multimeter (your Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Haunted Hallway (5 min)

> "Picture this: you are sneaking through a dark hallway at night, trying not to wake anyone up. Suddenly, a bright light flips on! You freeze. Did someone see you? Nope -- it was a motion sensor. It detected your body heat moving through its field of view and triggered the light."

> "PIR stands for Passive Infrared. Remember infrared from last lesson? Everything warm gives off infrared light -- including YOU! A PIR sensor does not send out any signal. It just sits there PASSIVELY watching for changes in the infrared light around it. When something warm (like a person, a pet, or even a cup of hot tea) moves across its view, it says 'I detected motion!'"

Show them the PIR module:

> "See that white dome on top? That is a special lens called a Fresnel lens (say 'freh-NEL'). It splits the PIR sensor's field of view into many little zones. When a warm body crosses from one zone to another, the sensor detects the change. If everything stays still, nothing happens."

**Award: +10 XP for learning about PIR sensors!**

---

### Step 2: How PIR Sensors Work (8 min)

**The Laser Grid Analogy:**

> "Imagine an invisible laser grid across a doorway in a spy movie. When someone walks through it, the alarm goes off because they break the beams. A PIR sensor is similar, except instead of lasers, it uses zones of infrared sensitivity. When a warm body moves from one zone to another, the sensor triggers."

**Key vocabulary:**

- **PIR (Passive Infrared):** Detects infrared radiation from warm objects. "Passive" means it does not emit anything -- it only receives.
- **Fresnel Lens:** The white plastic dome that focuses infrared onto the sensor and creates detection zones.
- **Output pin:** Goes HIGH (3.3V) when motion is detected, LOW (0V) when still.
- **Trigger modes:** The HC-SR501 has two trigger modes -- "Retriggerable" (stays HIGH as long as motion continues) and "Non-retriggerable" (goes HIGH once, then LOW, then waits).

**HC-SR501 Module:**

```
  HC-SR501 PIR Sensor (bottom view)

  +-----------------------------------+
  |                                   |
  |   [Sensitivity]   [Time delay]    |
  |    adjustment       adjustment    |
  |    (left pot)      (right pot)    |
  |                                   |
  |   VCC    OUT    GND               |
  |    |      |      |                |
  +-----------------------------------+
       |      |      |
      5V    signal   GND
```

**The two adjustment pots (on the module itself):**

| Potentiometer | What It Controls | Range |
|--------------|-----------------|-------|
| Sensitivity (left) | How far away it detects motion | ~3m to ~7m |
| Time Delay (right) | How long output stays HIGH after detecting motion | ~3 sec to ~300 sec |

**Award: +10 XP for understanding PIR internals!**

---

### Step 3: Wiring the PIR Sensor (5 min)

**Wiring diagram:**

```
  PIR Sensor         Arduino
  -----------        --------
  VCC  ------------>  5V
  OUT  ------------>  Pin 7
  GND  ------------>  GND
```

> "Just 3 wires! The PIR sensor is one of the easiest sensors to connect. Power, ground, and one signal wire."

**Important warm-up period:**

> "When you first power on the PIR, it needs about 30 to 60 seconds to 'calibrate' -- it learns the background infrared level of the room. During this time, stay very still and keep away from the sensor. After the warm-up, it is ready to detect motion!"

**Award: +10 XP for wiring the PIR sensor!**

---

### Step 4: Your First Motion Detection (8 min)

**Basic Motion Detection Code:**

```cpp
int pirPin = 7;
int ledPin = 13;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);

  Serial.println("PIR Sensor warming up...");
  Serial.println("Stay still for 30 seconds!");
  delay(30000);  // 30-second warm-up
  Serial.println("PIR Sensor READY!");
}

void loop() {
  int motionDetected = digitalRead(pirPin);

  if (motionDetected == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("*** MOTION DETECTED! ***");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("All clear...");
  }

  delay(200);
}
```

**Test it:**
1. Upload and open Serial Monitor
2. Stay very still during the 30-second warm-up
3. After "READY!" appears, wave your hand in front of the sensor
4. The LED lights up and "MOTION DETECTED!" appears!
5. Stop moving -- after the time delay (set by the module's pot), it goes back to LOW

**Try these experiments:**
- Walk across the room -- does it detect you from far away?
- Try moving just one finger close to the sensor
- Put a warm cup of water in front of it -- does it detect the heat?
- Try having a friend approach from different angles

**Award: +20 XP for detecting your first motion!**

---

### Step 5: Build the Automatic Security Light (8 min)

Add a timer and an alarm buzzer:

```cpp
int pirPin = 7;
int ledPin = 9;
int buzzerPin = 8;
unsigned long motionTime = 0;
int lightDuration = 10000;  // Keep light on for 10 seconds
bool alarmMode = false;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);

  Serial.println("Security System warming up...");
  delay(30000);
  Serial.println("SECURITY SYSTEM ACTIVE!");
}

void loop() {
  int motion = digitalRead(pirPin);

  if (motion == HIGH) {
    motionTime = millis();  // Record when motion was detected
    digitalWrite(ledPin, HIGH);
    Serial.println("ALERT: Motion detected!");

    if (alarmMode) {
      tone(buzzerPin, 2000, 500);  // Alarm sound!
    }
  }

  // Turn off LED after lightDuration milliseconds of no motion
  if (millis() - motionTime > lightDuration) {
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
  }

  delay(100);
}
```

> "Now you have a real security light! Walk past the sensor and the light stays on for 10 seconds. You can change `lightDuration` to make it longer or shorter. Set `alarmMode = true` to add a buzzer alarm!"

**Award: +25 XP for building the security light!**

---

### Step 6: Smart Night Light -- PIR + LDR Combo (5 min)

Why waste electricity turning on a light during the day? Add the LDR from Lesson 36:

```cpp
int pirPin = 7;
int ldrPin = A0;
int ledPin = 9;
int darkThreshold = 300;  // Below this = dark enough

void loop() {
  int motion = digitalRead(pirPin);
  int lightLevel = analogRead(ldrPin);

  if (motion == HIGH && lightLevel < darkThreshold) {
    // Motion detected AND it is dark!
    digitalWrite(ledPin, HIGH);
    Serial.println("Night motion -- light ON!");
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);
}
```

> "Now the light only turns on if TWO conditions are true: there is motion AND it is dark. During the day, the motion sensor still detects you, but the light stays off because the LDR says 'it is bright enough already!' This is how smart home systems work."

**Award: +25 XP for building the smart night light!**

---

### Step 7: Wand Check -- PIR Output HIGH vs LOW (5 min)

> "Let us use your Wand to see the exact voltage difference between 'motion detected' and 'no motion'. This is a clean digital signal!"

**Wand Test -- PIR Output Pin:**

1. Set your Wand to DC Volts (20V range)
2. Connect black probe to GND
3. Touch red probe to the PIR OUT pin (pin 7)

**Test both states:**

```
| Condition | Expected Voltage | Your Wand Reads | Points |
|-----------|-----------------|----------------|--------|
| No motion (all clear) | ~0V (LOW) | | +15 XP |
| Motion detected | ~3.3V (HIGH) | | +15 XP |
```

> "Unlike the analog sensors (LDR, temperature) that give a range of values, the PIR is DIGITAL -- it is either ON or OFF, HIGH or LOW, 3.3V or 0V. No in-between! That is why we use `digitalRead()` instead of `analogRead()` for this sensor."

**Bonus observation:** Watch the Wand while walking past the sensor. The voltage snaps from 0V to about 3.3V instantly, stays there for the time delay period, then snaps back to 0V.

**Award: +30 XP for measuring PIR output with your Wand!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does PIR stand for?
- A) Powered Infrared Receiver
- B) Passive Infrared
- C) Programmed Input Reader

**(Correct: B -- +15 XP!)**

**Question 2:** How does a PIR sensor detect motion?
- A) It sends out radar waves
- B) It senses changes in infrared heat patterns when a warm body moves through its field of view
- C) It uses a camera to see movement

**(Correct: B -- +15 XP!)**

**Question 3:** Why does the PIR need a 30-second warm-up period?
- A) The sensor needs to heat up
- B) It needs to learn the baseline infrared level of the room before it can detect changes
- C) The Arduino is loading software

**(Correct: B -- +15 XP!)**

**Question 4:** In our smart night light, the LED only turns on when:
- A) It is dark
- B) There is motion
- C) Both -- it is dark AND there is motion

**(Correct: C -- +15 XP!)**

---

## Lesson 41 Complete!

```
  =============================================

     MOTION GUARDIAN BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire and read a PIR motion sensor
     [check] Build an automatic security light
     [check] Combine PIR + LDR for a smart night light
     [check] Measured PIR HIGH vs LOW with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- haunted hallway | 10 |
| Understanding PIR sensors | 10 |
| Wiring the sensor | 10 |
| First motion detection | 20 |
| Security light build | 25 |
| Smart night light (PIR + LDR) | 25 |
| Wand Check (HIGH vs LOW) | 30 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **190** |

---

## Coming Up Next...

In **Lesson 42** -- the MODULE 5 GRAND FINALE -- you will combine EVERYTHING you have learned in this module to build a **Smart Room System**! Temperature monitoring, automatic lights, motion detection, distance sensing, and motor control -- all working together in one epic project. Get ready for the biggest build yet!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| PIR triggers randomly | Wait for full warm-up (60 seconds). Keep sensor away from windows, heaters, and air vents -- moving hot/cold air can trigger false alarms |
| PIR does not detect motion at all | Check wiring. Make sure the Fresnel lens dome is on top. Try adjusting the sensitivity pot on the module |
| LED stays on forever | The time delay pot on the PIR module may be turned to maximum (up to 5 minutes). Turn it counter-clockwise for shorter delay |
| PIR detects through walls or glass | PIR can sometimes detect through thin materials. Reposition the sensor |
| Smart night light never activates | Check LDR threshold -- print lightLevel to Serial Monitor and adjust darkThreshold to match your room |
| Wand reads 5V instead of 3.3V on HIGH | Some PIR modules output 5V. Either value is fine -- both read as HIGH for Arduino |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 40: IR Sensor and Remote Control -- Decoding Invisible Light](lesson-40-ir-sensor-and-remote.md) | [Lesson 42: Module 5 Project -- The Smart Room System →](lesson-42-project-smart-room.md) |
