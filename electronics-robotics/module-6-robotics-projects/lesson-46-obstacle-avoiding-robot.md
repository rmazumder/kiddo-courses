# Lesson 46: Obstacle-Avoiding Robot

**Module:** 6 -- Robotics Projects
**Difficulty:** Star-5 Expert
**Session Time:** 50--60 minutes
**Age:** 6--12 years
**XP Available:** 350 XP

---

## Your Mission Today

Robot Navigator, your robot can follow a line -- but what happens when something is in the way? Today you are going to give your robot the power of **echolocation** -- just like a bat! You will mount an ultrasonic distance sensor on the front and use a servo to scan left and right. When the robot sees an obstacle, it will stop, look around, and choose the best path -- all by itself. This is **autonomous obstacle avoidance**, and it is one of the most important skills in all of robotics!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how ultrasonic distance sensors measure distance
- Mount the HC-SR04 sensor and scanning servo on the robot
- Write an obstacle-avoidance algorithm
- Build an obstacle course and test your robot
- Use your Magic Measurement Wand to measure ultrasonic sensor VCC and trigger pin voltages

---

## What You Need

| Item | Qty |
|------|-----|
| Your assembled robot from Lessons 43-44 | 1 |
| HC-SR04 ultrasonic distance sensor | 1 |
| SG90 servo motor | 1 |
| Servo sensor mounting bracket (or cardboard + hot glue) | 1 |
| Jumper wires | 8 |
| Cardboard boxes or books (for obstacles) | 5+ |
| Multimeter (your Magic Measurement Wand!) | 1 |
| USB cable (for programming) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Bat Robot (5 min)

> "Close your eyes and try to walk across the room without bumping into anything."

(Let the kid try -- gently guide them away from real danger.)

> "Hard, right? Now imagine doing that using SOUND. Bats do this every night! They send out a high-pitched squeak, and when the sound bounces back from a wall or a tree, the bat knows how far away it is. This is called ECHOLOCATION."

Hold up the HC-SR04 sensor:

> "This sensor does the EXACT same thing! It sends out an ultrasonic pulse -- a sound so high that humans cannot hear it -- and listens for the echo. The longer it takes for the echo to come back, the farther away the object is. Your robot is about to become a bat!"

```
  How Ultrasonic Sensing Works:

  SENSOR ))))))))  ---------> WALL
                               |
  SENSOR ((((((((  <--------- ECHO

  Time between send and receive = distance!
  Distance = (time x speed of sound) / 2
```

**Award: +10 XP for understanding echolocation!**

---

### Step 2: Mounting the Sensor and Servo (10 min)

**The scanning system:**

The HC-SR04 sensor is mounted on top of the servo motor. The servo can rotate the sensor left and right to scan for obstacles in different directions.

```
  Scanning System (Side View):

       [HC-SR04]         <-- ultrasonic sensor (eyes)
          |
       [Servo]           <-- rotates the sensor
          |
   =================     <-- robot chassis
   O               O     <-- wheels
```

**Assembly:**
1. Attach the servo horn (arm) to the servo motor
2. Mount the HC-SR04 on the servo horn using a bracket, or make one from cardboard:

```
  DIY Sensor Mount:

  +-------[HC-SR04]-------+
  |                        |
  +---+              +---+
      |              |
      +---[HORN]---+
           |
        [SERVO]
```

3. Mount the servo on the FRONT of the robot chassis (centered)
4. Make sure the sensor faces forward when the servo is at 90 degrees

**Wiring:**

```
  HC-SR04:                    Servo:
  VCC ---> Arduino 5V         Red   ---> Arduino 5V
  GND ---> Arduino GND        Brown ---> Arduino GND
  Trig --> Arduino Pin 11     Signal --> Arduino Pin 6
  Echo --> Arduino Pin 12
```

**Award: +20 XP for mounting the scanning system!**

---

### Step 3: Testing the Distance Sensor (5 min)

First, let us make sure the sensor works:

```cpp
// Lesson 46: Distance Sensor Test
int trigPin = 11;
int echoPin = 12;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  Serial.println("Distance Sensor Test");
}

void loop() {
  // Send ultrasonic pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read echo
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(200);
}
```

**Test it:**
- Hold your hand in front of the sensor and move it closer/farther
- Check that the Serial Monitor readings match the actual distance (roughly)
- Try measuring a wall, a book, your hand

> "If the readings jump around wildly, make sure nothing is blocking the sensor's path and that the two 'eyes' (transmitter and receiver) are clean."

**Award: +20 XP for getting accurate distance readings!**

---

### Step 4: Testing the Servo Scan (5 min)

```cpp
// Servo scan test
#include <Servo.h>
Servo scanServo;

void setup() {
  scanServo.attach(6);
  Serial.begin(9600);
}

void loop() {
  Serial.println("Looking LEFT");
  scanServo.write(0);     // Look left
  delay(1000);

  Serial.println("Looking CENTER");
  scanServo.write(90);    // Look center
  delay(1000);

  Serial.println("Looking RIGHT");
  scanServo.write(180);   // Look right
  delay(1000);

  Serial.println("Looking CENTER");
  scanServo.write(90);    // Back to center
  delay(1000);
}
```

> "Watch your sensor head turn left, center, right, center. Like a robot looking around the room! This is exactly what the robot will do when it finds an obstacle."

**Award: +10 XP for testing the servo scan!**

---

### Step 5: The Obstacle-Avoidance Algorithm (12 min)

Here is the FULL autonomous obstacle-avoidance code:

```cpp
// Lesson 46: Obstacle-Avoiding Robot
#include <Servo.h>

// Motor pins
int leftENA = 9;
int leftIN1 = 2;
int leftIN2 = 3;
int rightENB = 10;
int rightIN3 = 4;
int rightIN4 = 5;

// Ultrasonic sensor pins
int trigPin = 11;
int echoPin = 12;

// Servo
Servo scanServo;
int servoPin = 6;

// Settings
int driveSpeed = 170;
int turnSpeed = 180;
int dangerDistance = 25;  // cm -- stop if closer than this

void setup() {
  // Motor pins
  pinMode(leftENA, OUTPUT);
  pinMode(leftIN1, OUTPUT);
  pinMode(leftIN2, OUTPUT);
  pinMode(rightENB, OUTPUT);
  pinMode(rightIN3, OUTPUT);
  pinMode(rightIN4, OUTPUT);

  // Sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Servo
  scanServo.attach(servoPin);
  scanServo.write(90);  // Start looking forward

  Serial.begin(9600);
  Serial.println("Obstacle Avoider Ready!");
  delay(2000);
}

void loop() {
  int distance = getDistance();

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > dangerDistance) {
    // Path is clear -- drive forward!
    forward(driveSpeed);
  } else {
    // OBSTACLE DETECTED! Stop and scan.
    Serial.println("OBSTACLE! Scanning...");
    stopRobot();
    delay(300);

    // Look LEFT
    scanServo.write(10);
    delay(500);
    int leftDist = getDistance();
    Serial.print("Left distance: ");
    Serial.println(leftDist);

    // Look RIGHT
    scanServo.write(170);
    delay(500);
    int rightDist = getDistance();
    Serial.print("Right distance: ");
    Serial.println(rightDist);

    // Look back to CENTER
    scanServo.write(90);
    delay(300);

    // Choose the direction with MORE space
    if (leftDist > rightDist && leftDist > dangerDistance) {
      Serial.println("Turning LEFT -- more space");
      turnLeft(turnSpeed);
      delay(500);
    } else if (rightDist > dangerDistance) {
      Serial.println("Turning RIGHT -- more space");
      turnRight(turnSpeed);
      delay(500);
    } else {
      // Both sides blocked! Back up and try again
      Serial.println("TRAPPED! Backing up...");
      backward(driveSpeed);
      delay(800);
      turnRight(turnSpeed);  // Turn around
      delay(700);
    }
    stopRobot();
    delay(200);
  }

  delay(50);
}

// === DISTANCE FUNCTION ===
int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);  // 30ms timeout
  if (duration == 0) return 999;  // No echo = very far
  return duration * 0.034 / 2;
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
}
```

**Walk through the logic:**

```
  Obstacle Avoidance Flowchart:

  START
    |
    v
  Measure distance ahead
    |
    v
  Distance > 25cm? ---YES---> Drive Forward
    |                              |
    NO                             |
    |                              |
    v                              |
  STOP!                            |
    |                              |
    v                              |
  Scan LEFT -- record distance     |
  Scan RIGHT -- record distance    |
    |                              |
    v                              |
  Left > Right?                    |
    YES --> Turn LEFT              |
    NO ---> Turn RIGHT             |
    |                              |
    v                              |
  Both blocked?                    |
    YES --> Back up + turn around  |
    |                              |
    +------------------------------+
```

**Award: +40 XP for uploading the obstacle-avoidance code!**

---

### Step 6: Build the Obstacle Course (5 min)

Set up an obstacle course using cardboard boxes, books, or other objects:

```
  Example Obstacle Course:

  START
    |
    v
  +---+        +---+
  |BOX|        |BOX|
  +---+   +    +---+
          |
       +--+---+
       | BOOK  |
       +-------+
                     +---+
            +---+    |BOX|
            |BOX|    +---+
            +---+
                        ^
                        |
                      FINISH
```

**Tips:**
- Leave enough space between obstacles for the robot to fit through
- Start with wide gaps and make them tighter as the robot improves
- Use objects that the ultrasonic sensor can detect (solid surfaces, not fabric)

**Award: +20 XP for building an obstacle course!**

---

### Step 7: Tuning and Testing (5 min)

Let the robot run through the course! Adjust these values:

| Parameter | Effect | Try This |
|-----------|--------|----------|
| dangerDistance | How close before stopping | 15--30 cm |
| driveSpeed | How fast it drives | 140--200 |
| Turn delay | How much it turns | 300--700 ms |
| Backup delay | How far it reverses | 500--1000 ms |

> "Your robot is making DECISIONS. It sees an obstacle, thinks about which way has more space, and chooses the best path. This is the beginning of artificial intelligence!"

**Award: +20 XP for a successful obstacle-course run!**

---

### Step 8: Wand Check -- Ultrasonic Sensor Voltages (8 min)

> "Time for your Magic Measurement Wand to check the sensor signals!"

Set the Wand to **DC Volts**.

**Measurement 1: Sensor Power**

```
| Measurement             | Expected | Your Reading |
|-------------------------|---------|-------------|
| HC-SR04 VCC pin         | 5.0V     |             |
| HC-SR04 GND pin         | 0V       |             |
| Servo VCC (red wire)    | 5.0V     |             |
```

**Measurement 2: Trigger Pin Voltage**

The Trig pin sends a quick pulse. With the robot running, measure the Trig pin. You might see a fluctuating reading since the pulse is very fast:

```
| Measurement                | Expected    | Your Reading |
|----------------------------|------------|-------------|
| Trig pin (idle)            | ~0V         |             |
| Trig pin (while measuring) | Flickers 0-5V |           |
```

> "The trigger pulse is only 10 microseconds long -- that is 10 MILLIONTHS of a second! Your Wand might not catch it perfectly because it is SO fast, but you should see it flicker. This is one of the fastest signals you have measured!"

**Measurement 3: Servo Signal Wire**

Measure the voltage on the servo signal wire while it moves:

```
| Servo Position | Signal Voltage (approx) |
|----------------|------------------------|
| 0 degrees      |                        |
| 90 degrees     |                        |
| 180 degrees    |                        |
```

> "The servo signal is also a PWM pulse -- your Wand will show an average voltage that changes with the position. Pretty cool!"

**Award: +50 XP for all Wand measurements!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** How does the HC-SR04 ultrasonic sensor measure distance?

- A) It uses a camera to see objects
- B) It sends a sound pulse and measures how long the echo takes to return
- C) It measures temperature changes

**(Correct: B -- +20 XP!)**

**Question 2:** Why does the robot use a servo to rotate the ultrasonic sensor?

- A) To make the sensor spin faster
- B) To scan left and right and find which direction has more open space
- C) To make the robot look cool

**(Correct: B -- +20 XP!)**

**Question 3:** The robot detects an obstacle 15cm ahead. Left scan reads 50cm. Right scan reads 10cm. Which way should it turn?

- A) Left -- because 50cm is more space
- B) Right -- because 10cm is closer
- C) Straight ahead

**(Correct: A -- +20 XP!)**

---

## Lesson 46 Complete!

```
  =============================================

     OBSTACLE NAVIGATOR BADGE UNLOCKED!

     Skills unlocked:
     [check] Mounted ultrasonic sensor + servo
     [check] Wrote distance measurement function
     [check] Programmed obstacle-avoidance logic
     [check] Built and tested obstacle course
     [check] Measured sensor voltages with Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook (echolocation) | 10 |
| Mounting scanning system | 20 |
| Distance sensor test | 20 |
| Servo scan test | 10 |
| Obstacle-avoidance code | 40 |
| Build obstacle course | 20 |
| Successful course run | 20 |
| Wand Check (all measurements) | 50 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 47**, your robot gets a PERSONALITY! You will add LEDs for eyes and a buzzer for a voice. Your robot will flash its lights when turning, beep when it spots an obstacle, and play a startup melody when it powers on. Get ready to make your robot come alive!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Distance readings are 0 or 999 | Check Trig and Echo pin connections |
| Sensor always reads very short distances | Something blocking sensor face -- check mounting |
| Servo jitters or does not move | Check 5V power -- servo might need more current |
| Robot crashes into obstacles | Increase dangerDistance or reduce driveSpeed |
| Robot gets stuck in corners | Increase backup time in the "TRAPPED" section of code |
| Wand reads 3.5V on HC-SR04 VCC | Power supply weak -- check batteries |
