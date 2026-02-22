# Lesson 48: Remote-Controlled Robot (Bluetooth)

**Module:** 6 -- Robotics Projects
**Difficulty:** Star-5 Expert
**Session Time:** 50--60 minutes
**Age:** 6--12 years
**XP Available:** 350 XP

---

## Your Mission Today

Robot Commander, up until now your robot has been running on its own -- following lines and dodging obstacles. Today, YOU take the controls! You are going to add a **Bluetooth module** to your robot so you can drive it from your phone. Send commands wirelessly -- forward, backward, left, right, stop -- and watch your robot obey from across the room. This is wireless remote control, and it is incredibly cool!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how Bluetooth communication works (in simple terms)
- Wire the HC-05 Bluetooth module to Arduino
- Pair a smartphone with the HC-05
- Write code to receive Bluetooth commands and control the robot
- Switch between manual (phone) and autonomous (obstacle-avoidance) modes
- Use your Magic Measurement Wand to measure HC-05 TX/RX pin voltages

---

## What You Need

| Item | Qty |
|------|-----|
| Your robot from Lessons 43-47 | 1 |
| HC-05 Bluetooth module | 1 |
| Jumper wires (female-to-male) | 4 |
| 1k-ohm resistor | 1 |
| 2k-ohm resistor (or two 1k-ohm in series) | 1 |
| Smartphone with Bluetooth | 1 |
| Bluetooth controller app (free) | 1 |
| Multimeter (your Magic Measurement Wand!) | 1 |
| USB cable (for programming) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- Wireless Magic (5 min)

> "Your robot has been amazing -- following lines, dodging obstacles, flashing lights. But what if you could control it from your PHONE? Like a video game, but the character is REAL and driving around your room?"

> "Bluetooth is the same technology that connects your wireless headphones to your phone. Instead of sending music, we are going to send COMMANDS. When you press a button on your phone, it sends a letter -- F for forward, B for backward, L for left, R for right, S for stop. Your Arduino reads the letter and makes the robot move. It is like sending text messages to your robot!"

```
  How Bluetooth Control Works:

  [Your Phone]                    [HC-05 Module]         [Arduino]
      |                              |                      |
      |--- "F" (forward) --------->  |--- serial data ---> |
      |                              |                      |
      |                              |                      +--> forward(200)
      |                              |                      |
      |--- "S" (stop) ----------->   |--- serial data ---> |
      |                              |                      |
      |                              |                      +--> stopRobot()
```

**Award: +10 XP for understanding Bluetooth communication!**

---

### Step 2: Wiring the HC-05 Module (10 min)

The HC-05 module communicates using serial (TX/RX) just like the USB connection, but wirelessly!

**IMPORTANT:** The HC-05 runs at 3.3V logic but has a 5V tolerant VCC pin. The TX pin from Arduino is 5V, but the HC-05 RX pin needs 3.3V. We use a **voltage divider** to protect it!

**Wiring Diagram:**

```
  HC-05 Pin    Connection
  ---------    ----------
  VCC    -----> Arduino 5V
  GND    -----> Arduino GND
  TXD    -----> Arduino Pin 7 (SoftwareSerial RX)
  RXD    <----- Voltage Divider from Arduino Pin 8

  Voltage Divider for RXD:

  Arduino Pin 8 ---[1k ohm]---+---[2k ohm]--- GND
                               |
                          HC-05 RXD

  This converts 5V down to ~3.3V to protect the HC-05!
```

**Why SoftwareSerial?**

> "Arduino only has one hardware serial port (pins 0 and 1), and we need that for the USB connection to upload code. So we use a library called SoftwareSerial to create a SECOND serial port on any pins we choose. It is like adding an extra phone line to your house!"

> "IMPORTANT: Disconnect the HC-05 RXD and TXD wires when uploading code via USB! They can interfere with programming."

**Award: +20 XP for wiring the HC-05 with voltage divider!**

---

### Step 3: The Bluetooth Controller App (5 min)

**On an Android phone:**
1. Search the app store for "Arduino Bluetooth Controller" or "Bluetooth RC Controller"
2. Install a free app that lets you send single character commands

**On an iPhone:**
- Note: HC-05 works with Android. For iPhone, you need an HM-10 (BLE) module instead.
- Apps: "LightBlue" or "BLE Terminal" work with HM-10

**Pairing:**
1. Turn on the robot (power the HC-05)
2. The HC-05 LED will blink rapidly -- it is waiting to pair
3. On your phone, go to Bluetooth settings
4. Find "HC-05" in the list (default password: 1234 or 0000)
5. Pair with it
6. Open the controller app and connect to HC-05
7. The HC-05 LED will blink slowly -- it is now connected!

> "When the LED on the HC-05 blinks FAST, it is lonely and looking for a friend. When it blinks SLOW, it found your phone and they are talking!"

**Award: +10 XP for successfully pairing your phone with the HC-05!**

---

### Step 4: Bluetooth Control Code (12 min)

```cpp
// Lesson 48: Bluetooth Remote-Controlled Robot
#include <SoftwareSerial.h>

// Bluetooth serial on pins 7 (RX) and 8 (TX)
SoftwareSerial bluetooth(7, 8);  // RX, TX

// Motor pins (same as before)
int leftENA = 9;
int leftIN1 = 2;
int leftIN2 = 3;
int rightENB = 10;
int rightIN3 = 4;
int rightIN4 = 5;

// LED and buzzer pins
int greenLeft = A1;
int greenRight = A2;
int redLeft = A3;
int redRight = A4;
int blueStatus = 13;
int buzzerPin = A5;

int driveSpeed = 200;

void setup() {
  // Motor pins
  pinMode(leftENA, OUTPUT);
  pinMode(leftIN1, OUTPUT);
  pinMode(leftIN2, OUTPUT);
  pinMode(rightENB, OUTPUT);
  pinMode(rightIN3, OUTPUT);
  pinMode(rightIN4, OUTPUT);

  // LED pins
  pinMode(greenLeft, OUTPUT);
  pinMode(greenRight, OUTPUT);
  pinMode(redLeft, OUTPUT);
  pinMode(redRight, OUTPUT);
  pinMode(blueStatus, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  // Start both serial connections
  Serial.begin(9600);
  bluetooth.begin(9600);  // HC-05 default baud rate

  Serial.println("Bluetooth Robot Ready!");
  Serial.println("Waiting for connection...");

  // Startup blink
  for (int i = 0; i < 3; i++) {
    digitalWrite(blueStatus, HIGH);
    delay(200);
    digitalWrite(blueStatus, LOW);
    delay(200);
  }
}

void loop() {
  if (bluetooth.available()) {
    char command = bluetooth.read();

    // Show command on Serial Monitor too
    Serial.print("Received: ");
    Serial.println(command);

    // Process command
    switch (command) {
      case 'F':  // Forward
      case 'f':
        forward(driveSpeed);
        digitalWrite(greenLeft, HIGH);
        digitalWrite(greenRight, HIGH);
        digitalWrite(redLeft, LOW);
        digitalWrite(redRight, LOW);
        break;

      case 'B':  // Backward
      case 'b':
        backward(driveSpeed);
        digitalWrite(greenLeft, LOW);
        digitalWrite(greenRight, LOW);
        digitalWrite(redLeft, HIGH);
        digitalWrite(redRight, HIGH);
        break;

      case 'L':  // Turn Left
      case 'l':
        turnLeft(driveSpeed);
        digitalWrite(greenLeft, HIGH);
        digitalWrite(greenRight, LOW);
        break;

      case 'R':  // Turn Right
      case 'r':
        turnRight(driveSpeed);
        digitalWrite(greenLeft, LOW);
        digitalWrite(greenRight, HIGH);
        break;

      case 'S':  // Stop
      case 's':
        stopRobot();
        digitalWrite(greenLeft, LOW);
        digitalWrite(greenRight, LOW);
        digitalWrite(redLeft, LOW);
        digitalWrite(redRight, LOW);
        digitalWrite(blueStatus, HIGH);
        break;

      case 'H':  // Horn!
      case 'h':
        tone(buzzerPin, 800, 300);
        delay(350);
        noTone(buzzerPin);
        break;

      case '1':  // Speed: Slow
        driveSpeed = 120;
        Serial.println("Speed: SLOW");
        break;

      case '2':  // Speed: Medium
        driveSpeed = 180;
        Serial.println("Speed: MEDIUM");
        break;

      case '3':  // Speed: Fast
        driveSpeed = 240;
        Serial.println("Speed: FAST");
        break;
    }
  }
}

// === MOVEMENT FUNCTIONS ===
void forward(int speed) {
  digitalWrite(leftIN1, HIGH);
  digitalWrite(leftIN2, LOW);
  digitalWrite(rightIN3, HIGH);
  digitalWrite(rightIN4, LOW);
  analogWrite(leftENA, speed);
  analogWrite(rightENB, speed);
}

void backward(int speed) {
  digitalWrite(leftIN1, LOW);
  digitalWrite(leftIN2, HIGH);
  digitalWrite(rightIN3, LOW);
  digitalWrite(rightIN4, HIGH);
  analogWrite(leftENA, speed);
  analogWrite(rightENB, speed);
}

void turnLeft(int speed) {
  digitalWrite(leftIN1, LOW);
  digitalWrite(leftIN2, HIGH);
  digitalWrite(rightIN3, HIGH);
  digitalWrite(rightIN4, LOW);
  analogWrite(leftENA, speed);
  analogWrite(rightENB, speed);
}

void turnRight(int speed) {
  digitalWrite(leftIN1, HIGH);
  digitalWrite(leftIN2, LOW);
  digitalWrite(rightIN3, LOW);
  digitalWrite(rightIN4, HIGH);
  analogWrite(leftENA, speed);
  analogWrite(rightENB, speed);
}

void stopRobot() {
  digitalWrite(leftIN1, LOW);
  digitalWrite(leftIN2, LOW);
  digitalWrite(rightIN3, LOW);
  digitalWrite(rightIN4, LOW);
  analogWrite(leftENA, 0);
  analogWrite(rightENB, 0);
}
```

**Command Reference Card:**

```
+------+------------------+
| Key  | Action           |
+------+------------------+
| F    | Forward          |
| B    | Backward         |
| L    | Turn Left        |
| R    | Turn Right       |
| S    | Stop             |
| H    | Horn (beep!)     |
| 1    | Slow speed       |
| 2    | Medium speed     |
| 3    | Fast speed       |
+------+------------------+
```

**Award: +40 XP for uploading and testing Bluetooth control!**

---

### Step 5: Test Drive! (5 min)

> "Time to take your robot for a spin! Open the Bluetooth app on your phone, connect to HC-05, and start driving!"

**Test Checklist:**

```
| Test                     | Works? |
|--------------------------|--------|
| Forward command (F)      |        |
| Backward command (B)     |        |
| Turn Left (L)            |        |
| Turn Right (R)           |        |
| Stop (S)                 |        |
| Horn (H)                 |        |
| Speed change (1, 2, 3)   |        |
| Green LEDs on forward    |        |
| Red LEDs on backward     |        |
```

> "Drive it around the room! Try navigating around furniture. Can you drive it into the kitchen and back?"

**Award: +30 XP for a successful Bluetooth test drive!**

---

### Step 6: Bonus -- Dual Mode (Bluetooth + Autonomous) (5 min)

What if your robot could switch between phone control and autonomous mode?

```cpp
// Add this to your code:
bool autonomousMode = false;

// In the loop(), add these commands:
case 'A':  // Switch to Autonomous mode
case 'a':
  autonomousMode = true;
  Serial.println("AUTONOMOUS MODE!");
  tone(buzzerPin, 1000, 200);
  break;

case 'M':  // Switch to Manual mode
case 'm':
  autonomousMode = false;
  stopRobot();
  Serial.println("MANUAL MODE!");
  tone(buzzerPin, 500, 200);
  break;

// At the top of loop():
if (autonomousMode) {
  // Run obstacle-avoidance code here
  // (from Lesson 46)
  return;  // Skip Bluetooth command reading
}
```

> "Now press A on your phone and the robot drives itself! Press M to take back control. You just built a robot with TWO brain modes!"

**Award: +20 XP for implementing dual mode!**

---

### Step 7: Wand Check -- HC-05 Voltages (8 min)

> "Let us use your Magic Measurement Wand to peek at the Bluetooth communication signals!"

Set the Wand to **DC Volts**.

**Measurement 1: HC-05 Power**

```
| Measurement       | Expected | Your Reading |
|-------------------|---------|-------------|
| HC-05 VCC pin     | 5.0V     |             |
| HC-05 GND pin     | 0V       |             |
```

**Measurement 2: TX/RX Pin Voltages**

```
| Measurement                 | Expected     | Your Reading |
|-----------------------------|-------------|-------------|
| HC-05 TXD pin (idle)       | ~3.3V        |             |
| HC-05 RXD pin (idle)       | ~3.3V        |             |
| Voltage divider output     | ~3.0--3.4V    |             |
| Arduino Pin 8 (before divider) | ~5.0V    |             |
```

> "Look at that! The Arduino sends 5V, but our voltage divider drops it to 3.3V before it reaches the HC-05. Without that voltage divider, we could damage the HC-05. Your Wand just confirmed the protection is working!"

**Measurement 3: During Communication**

Send a few commands from your phone and watch the Wand readings on the TXD pin:

> "When data is being sent, the voltage on the TX pin flickers rapidly between 0V and 3.3V. Each flicker is a binary digit -- a 1 or a 0 -- that makes up the letter you sent. Your Wand is seeing digital data in real time!"

**Award: +50 XP for all Bluetooth Wand measurements!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** Why do we need a voltage divider between Arduino TX and HC-05 RX?

- A) To make the signal louder
- B) To drop 5V to 3.3V so we do not damage the HC-05
- C) To make the robot go faster

**(Correct: B -- +20 XP!)**

**Question 2:** What does the HC-05 LED blinking pattern tell you?

- A) Fast blink = connected, slow blink = searching
- B) Fast blink = searching for connection, slow blink = connected
- C) Blinking means the battery is low

**(Correct: B -- +20 XP!)**

**Question 3:** What library lets us create extra serial ports on Arduino?

- A) Servo.h
- B) SoftwareSerial.h
- C) Bluetooth.h

**(Correct: B -- +20 XP!)**

**Question 4:** What is the default pairing password for most HC-05 modules?

- A) password
- B) 1234
- C) bluetooth

**(Correct: B -- +20 XP!)**

---

## Lesson 48 Complete!

```
  =============================================

     WIRELESS COMMANDER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wired HC-05 with voltage divider
     [check] Paired phone with Bluetooth
     [check] Controlled robot wirelessly
     [check] Added speed control and horn
     [check] Implemented dual mode (manual/auto)
     [check] Measured Bluetooth voltages with Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook (Bluetooth understanding) | 10 |
| HC-05 wiring with voltage divider | 20 |
| Phone pairing | 10 |
| Bluetooth control code | 40 |
| Successful test drive | 30 |
| Dual mode bonus | 20 |
| Wand Check (all measurements) | 50 |
| Quiz (4 questions) | 80 |
| **TOTAL POSSIBLE** | **260** |

---

## Coming Up Next...

In **Lesson 49**, you are going to build a **robot arm**! Using servo motors and popsicle sticks, you will create a 3-joint arm that can pick up and move small objects. You will control each joint with a potentiometer -- like a joystick for a crane!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Cannot find HC-05 in phone Bluetooth list | Make sure HC-05 is powered on (LED blinking fast) |
| Wrong password | Try both 1234 and 0000 |
| Connected but no response to commands | Check RX/TX wires are not swapped |
| Robot moves erratically | Check baud rate matches (9600 in both code and module) |
| Cannot upload code with HC-05 connected | Disconnect HC-05 TX/RX wires during upload |
| HC-05 LED does not blink | Check VCC and GND connections |
| Voltage divider reads wrong voltage | Check resistor values -- 1k and 2k (or two 1k in series) |
