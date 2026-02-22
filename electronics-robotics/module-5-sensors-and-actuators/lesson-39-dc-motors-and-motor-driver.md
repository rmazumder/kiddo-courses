# Lesson 39: DC Motors and Motor Driver -- Spin Those Wheels! (L298N)

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

Circuit Explorer, last lesson you learned to move a servo to precise angles. But servos do not spin wheels -- they just wiggle back and forth. To build a robot that actually DRIVES, you need **DC motors** -- the kind that spin continuously and can power wheels, fans, and propellers. There is just one catch: DC motors are power-hungry beasts that need more current than your Arduino can safely provide. Enter the **L298N motor driver** -- a powerful sidekick that lets Arduino boss around big motors without breaking a sweat!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain why Arduino cannot drive a DC motor directly
- Identify the L298N motor driver and its key connections
- Wire a DC motor through the L298N
- Control motor direction (forward and backward)
- Control motor speed using PWM
- Use your Magic Measurement Wand to measure motor driver output voltage at different speeds

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| L298N motor driver module | 1 |
| Small DC motor (3-6V hobby motor) | 1 |
| 9V battery + clip (for motor power) | 1 |
| 10k-ohm potentiometer | 1 |
| Push button | 2 |
| Breadboard | 1 |
| Jumper wires | 12 |
| Multimeter (your Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- Why Not Just Connect the Motor to Arduino? (5 min)

> "Let me tell you a story about what happens if you try to spin a DC motor directly from an Arduino pin."

**The fire hose vs garden hose analogy:**

> "An Arduino pin can only push out about 40 milliamps of current -- that is like a garden hose trickle. A DC motor wants 200 to 800 milliamps or MORE -- that is like a fire hose. If you connect a motor directly to an Arduino pin, the motor will barely twitch, and the Arduino might get damaged from trying too hard."

> "So we need a MIDDLEMAN -- a strong helper that takes Arduino's tiny instructions and uses them to control a big, powerful flow of electricity to the motor. That middleman is the L298N motor driver."

**Show them the L298N module:**

> "This board is like a translator between Arduino's gentle whispers and the motor's need for POWER. Arduino says 'go forward at half speed' and the L298N delivers the beefy current the motor needs."

**Award: +10 XP for understanding why we need a motor driver!**

---

### Step 2: Meet the L298N Motor Driver (8 min)

**Key vocabulary:**

- **DC Motor:** A motor that spins when you give it voltage. Reverse the voltage polarity and it spins the other way!
- **Motor Driver:** A circuit that can switch high-current paths on and off, controlled by low-current signals from Arduino.
- **H-Bridge:** The circuit pattern inside the L298N that allows current to flow through the motor in either direction. Called an H-Bridge because the circuit diagram looks like the letter H.
- **ENA/ENB:** Enable pins -- these control the SPEED using PWM.
- **IN1/IN2 (and IN3/IN4):** Direction control pins -- these control which way the motor spins.

**L298N Module Layout:**

```
       Motor A         Motor B
       OUT1 OUT2       OUT3 OUT4
        |    |          |    |
  +-----|----|---------|----|-----+
  |     L298N Motor Driver Module  |
  |                                |
  |  +12V   GND   +5V             |
  |   (motor    (shared  (5V out  |
  |   power)    ground)  or input)|
  |                                |
  |  ENA  IN1  IN2  IN3  IN4  ENB |
  +--------------------------------+
    |    |    |    |    |    |
   PWM  dir  dir  dir  dir  PWM
   speed      Motor A     speed
              direction
```

**Direction control truth table for Motor A:**

| IN1 | IN2 | Motor A Action |
|-----|-----|----------------|
| HIGH | LOW | Forward (spins one way) |
| LOW | HIGH | Backward (spins the other way) |
| LOW | LOW | Stop (coast) |
| HIGH | HIGH | Brake (locked stop) |

**Award: +15 XP for understanding the L298N!**

---

### Step 3: Wiring Everything (10 min)

**Wiring diagram:**

```
  9V Battery (+) ---------> L298N +12V terminal
  9V Battery (-) ---------> L298N GND terminal
  Arduino GND    ---------> L298N GND terminal  (SHARED GROUND!)

  L298N ENA  ---------> Arduino Pin 9  (PWM for speed)
  L298N IN1  ---------> Arduino Pin 2  (direction)
  L298N IN2  ---------> Arduino Pin 3  (direction)

  DC Motor wire A ---------> L298N OUT1
  DC Motor wire B ---------> L298N OUT2

  Note: Remove the ENA jumper cap on the L298N board
  so you can control speed with PWM.
```

**Very important: shared ground!**

> "The Arduino GND and the motor battery GND MUST be connected together. This is called a shared or common ground. Without it, Arduino and the L298N cannot understand each other -- it is like trying to have a phone call with no connection!"

**Award: +20 XP for wiring the motor driver!**

---

### Step 4: Forward, Backward, Stop! (8 min)

**Basic Motor Control Code:**

```cpp
int ENA = 9;   // Speed control (PWM)
int IN1 = 2;   // Direction
int IN2 = 3;   // Direction

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  Serial.begin(9600);
  Serial.println("Motor Driver Ready!");
}

void motorForward(int speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed);  // 0-255
}

void motorBackward(int speed) {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, speed);
}

void motorStop() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);
}

void loop() {
  Serial.println("Forward at half speed...");
  motorForward(128);      // 50% speed
  delay(3000);

  Serial.println("Stopping...");
  motorStop();
  delay(1000);

  Serial.println("Backward at full speed...");
  motorBackward(255);     // 100% speed
  delay(3000);

  Serial.println("Stopping...");
  motorStop();
  delay(1000);

  Serial.println("Forward slow...");
  motorForward(80);       // ~30% speed
  delay(3000);

  motorStop();
  delay(2000);
}
```

**Watch the motor:**
- It runs forward at half speed for 3 seconds
- Stops for 1 second
- Runs backward at full speed for 3 seconds
- Stops again
- Then forward slowly

> "See how changing the number in `analogWrite()` changes the speed? 255 is full blast, 128 is half speed, and anything below about 60-80 might not be enough to overcome the motor's friction."

**Award: +25 XP for controlling motor direction and speed!**

---

### Step 5: Speed Control with Potentiometer (5 min)

Add a potentiometer to control speed in real time:

```cpp
int potPin = A0;

void loop() {
  int potValue = analogRead(potPin);
  int speed = map(potValue, 0, 1023, 0, 255);

  motorForward(speed);

  Serial.print("Pot: ");
  Serial.print(potValue);
  Serial.print("  Speed: ");
  Serial.println(speed);

  delay(50);
}
```

> "Turn the knob slowly and watch the motor speed up. You are adjusting the PWM duty cycle -- the percentage of time the motor gets power. It is like tapping the gas pedal in a car!"

**Award: +20 XP for speed control with the potentiometer!**

---

### Step 6: Wand Check -- Measure Motor Output Voltage (8 min)

> "Your Wand can show you exactly how much voltage the motor is receiving at different speeds. This is where you can SEE the PWM doing its job!"

**Wand Test -- Motor Output Voltage at Different Speeds:**

1. Set your Wand to DC Volts (20V range)
2. Touch probes to the two motor wires (or L298N OUT1 and OUT2)
3. Run the motor at different PWM speeds and record the average voltage

```
| PWM Value | Percent Speed | Expected Voltage | Your Wand Reads | Points |
|-----------|--------------|-----------------|----------------|--------|
| 0         | 0%           | ~0V             |                | +5 XP  |
| 64        | 25%          | ~2-3V           |                | +10 XP |
| 128       | 50%          | ~4-5V           |                | +10 XP |
| 192       | 75%          | ~6-7V           |                | +10 XP |
| 255       | 100%         | ~8-9V           |                | +10 XP |
```

> "Notice how the voltage goes up as you increase the PWM value? At 100% (255), you get nearly the full battery voltage. At 50% (128), you get about half. Your Wand is showing you the average voltage the motor feels -- even though the signal is actually flipping on and off super fast!"

**Award: +45 XP for measuring output voltage at 5 different speeds!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** Why can't you connect a DC motor directly to an Arduino pin?
- A) The motor is too small
- B) Arduino pins cannot provide enough current for a motor
- C) Motors only work with batteries

**(Correct: B -- +15 XP!)**

**Question 2:** What does the L298N motor driver do?
- A) Measures motor speed
- B) Uses Arduino's control signals to switch high-current power to the motors
- C) Generates electricity from the motor

**(Correct: B -- +15 XP!)**

**Question 3:** To reverse a DC motor's direction with the L298N, you:
- A) Swap the ENA and ENB pins
- B) Flip IN1 and IN2 (change which one is HIGH and which is LOW)
- C) Disconnect the GND wire

**(Correct: B -- +15 XP!)**

**Question 4:** What does `analogWrite(ENA, 128)` do to the motor speed?
- A) Runs the motor at full speed
- B) Runs the motor at approximately half speed (50% PWM duty cycle)
- C) Stops the motor

**(Correct: B -- +15 XP!)**

---

## Lesson 39 Complete!

```
  =============================================

     MOTOR MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire a DC motor through L298N driver
     [check] Control motor direction (forward/backward)
     [check] Control motor speed with PWM
     [check] Measured motor voltage at different speeds with Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- why motor drivers | 10 |
| Understanding the L298N | 15 |
| Wiring the motor driver | 20 |
| Forward/backward/stop control | 25 |
| Potentiometer speed control | 20 |
| Wand Check (5 speed levels) | 45 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **195** |

---

## Coming Up Next...

In **Lesson 40**, you will learn about **IR sensors and remote controls**. You will decode the secret signals that TV remotes send, and then use those signals to control LEDs, a servo, or even your motor! It is like giving your Arduino a remote-controlled brain!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Motor does not spin | Check that the ENA jumper is removed AND that you are sending PWM to the ENA pin |
| Motor only goes one direction | Check IN1 and IN2 wiring -- both must go to separate Arduino pins |
| Motor barely moves at low speeds | Some motors need a minimum PWM of 60-100 to overcome internal friction |
| Arduino resets when motor starts | Shared ground is missing -- connect Arduino GND to L298N GND |
| Motor gets very hot | Do not stall the motor (hold it so it cannot spin). Reduce voltage or add breaks |
| L298N gets hot | Normal for high-current loads. If too hot, reduce motor duty cycle or add a small heatsink |
| Wand reads 0V on motor outputs | Check battery connection to L298N +12V terminal. Is the battery dead? |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 38: Servo Motors -- Precision Arm Muscles](lesson-38-servo-motors.md) | [Lesson 40: IR Sensor and Remote Control -- Decoding Invisible Light →](lesson-40-ir-sensor-and-remote.md) |
