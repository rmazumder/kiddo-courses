# Lesson 40: IR Sensor and Remote Control -- Decoding Invisible Light

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 275 XP

---

## Your Mission Today

Circuit Explorer, today you are going to decode INVISIBLE LIGHT. Every time you press a button on a TV remote, it blasts out a secret coded message using infrared (IR) light -- light your eyes cannot see, but a tiny sensor can detect. You are going to capture those codes, figure out what each button sends, and then program your Arduino to respond to remote control commands. By the end, you will have a remote-controlled LED system!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what infrared (IR) light is and how remote controls use it
- Wire an IR receiver module to Arduino
- Decode button codes from any IR remote control
- Write a sketch that responds to specific remote buttons
- Build a remote-controlled LED or servo system

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| IR receiver module (VS1838B or similar) | 1 |
| Any IR remote control (TV, DVD, or a small Arduino remote) | 1 |
| LEDs (red, green, blue) | 1 each |
| 330-ohm resistors | 3 |
| SG90 servo motor (optional, from Lesson 38) | 1 |
| Breadboard | 1 |
| Jumper wires | 8 |
| Multimeter (your Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Invisible Flashlight (5 min)

> "Point your TV remote at your phone camera and press any button. What do you see?"

If they try it, the phone camera will show a faint purple/white flashing light from the front of the remote -- invisible to the naked eye but visible to the camera sensor!

> "That is infrared light! Your remote control is actually a tiny flashlight that blinks in a secret pattern. Each button blinks a DIFFERENT pattern -- that is how the TV knows which button you pressed. It is like Morse code, but with invisible light instead of sound!"

> "Today you are going to be a code-breaker. You will capture those invisible signals and decode them."

**Fun fact:**
> "The word 'infrared' means 'below red.' It is light with a wavelength longer than red light -- just past what our eyes can detect. Your body radiates infrared light too -- that is how thermal cameras see you in the dark!"

**Award: +10 XP for discovering infrared light!**

---

### Step 2: How IR Remote Control Works (5 min)

**The Flashlight Morse Code Analogy:**

> "Imagine you and a friend are on opposite sides of a dark field. You have a flashlight. To send the number '1', you flash: ON-OFF-ON. For '2', you flash: ON-ON-OFF-OFF. For '3', you flash: ON-OFF-ON-OFF. Each number has a unique pattern. That is EXACTLY what an IR remote does, except the flashing is 38,000 times per second!"

**The process:**

1. You press a button on the remote
2. The remote sends a specific pattern of IR light pulses
3. The IR receiver module on the other end detects the pulses
4. It converts them into an electrical signal Arduino can read
5. Arduino decodes the signal into a number (the button code)

**IR Receiver Module (VS1838B) Pinout:**

```
  IR Receiver (front view -- dome faces you)

       +---+
      /     \
     |  dome  |
      \     /
       +---+
       | | |
       S G V
       i N C
       g D C
       n
       a
       l

  Signal (left) -> Arduino pin 11
  GND (middle)  -> Arduino GND
  VCC (right)   -> Arduino 5V
```

> "The dome on the front filters out regular visible light and only lets infrared through. Smart!"

**Award: +10 XP for understanding IR communication!**

---

### Step 3: Installing the IRremote Library (3 min)

1. Open Arduino IDE
2. Go to Sketch > Include Library > Manage Libraries
3. Search for "IRremote" by shirriff, z3t0, ArminJo
4. Install the latest version

> "This library does the hard work of decoding those super-fast IR pulses into numbers we can use."

**Award: +5 XP for installing the library!**

---

### Step 4: Decode Your Remote Buttons (10 min)

**IR Decoder Sketch:**

```cpp
#include <IRremote.hpp>

int irPin = 11;

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(irPin);
  Serial.println("IR Receiver Ready!");
  Serial.println("Point your remote and press buttons...");
  Serial.println("-----------------------------------");
}

void loop() {
  if (IrReceiver.decode()) {
    Serial.print("Button code: 0x");
    Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);

    Serial.print("Protocol: ");
    Serial.println(IrReceiver.decodedIRData.protocol);

    Serial.println("---");

    IrReceiver.resume();  // Ready for next signal
  }
}
```

**Activity -- Decode at least 5 buttons:**

Point the remote at the IR receiver and press buttons one at a time. Write down the code for each:

```
| Button | Code (hex) | What I Will Use It For |
|--------|-----------|----------------------|
| Power  |           |                      |
| 1      |           |                      |
| 2      |           |                      |
| 3      |           |                      |
| Vol Up |           |                      |
| Vol Down |         |                      |
| Ch Up  |           |                      |
```

> "Every remote is different! Your TV remote will have different codes than someone else's. That is why you need to decode YOUR specific remote. It is like cracking a personal cipher!"

**Tip:** If a button shows the same code every time, great! Some remotes send slightly different codes if you hold the button -- just use quick presses.

**Award: +25 XP for decoding at least 5 buttons!**

---

### Step 5: Build a Remote-Controlled LED System (10 min)

Now use those codes to control LEDs:

```cpp
#include <IRremote.hpp>

int irPin = 11;
int redLED = 5;
int greenLED = 6;
int blueLED = 7;

// Replace these with YOUR remote's codes!
#define BUTTON_1  0xE916FF00   // Button 1 on your remote
#define BUTTON_2  0xE619FF00   // Button 2
#define BUTTON_3  0xF20DFF00   // Button 3
#define BUTTON_PWR 0xBA45FF00  // Power button

bool redOn = false;
bool greenOn = false;
bool blueOn = false;

void setup() {
  IrReceiver.begin(irPin);
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Remote Control LED System Ready!");
}

void loop() {
  if (IrReceiver.decode()) {
    unsigned long code = IrReceiver.decodedIRData.decodedRawData;

    if (code == BUTTON_1) {
      redOn = !redOn;  // Toggle red
      digitalWrite(redLED, redOn ? HIGH : LOW);
      Serial.println("Red toggled!");
    }
    else if (code == BUTTON_2) {
      greenOn = !greenOn;  // Toggle green
      digitalWrite(greenLED, greenOn ? HIGH : LOW);
      Serial.println("Green toggled!");
    }
    else if (code == BUTTON_3) {
      blueOn = !blueOn;  // Toggle blue
      digitalWrite(blueLED, blueOn ? HIGH : LOW);
      Serial.println("Blue toggled!");
    }
    else if (code == BUTTON_PWR) {
      // All off
      redOn = false; greenOn = false; blueOn = false;
      digitalWrite(redLED, LOW);
      digitalWrite(greenLED, LOW);
      digitalWrite(blueLED, LOW);
      Serial.println("All LEDs OFF!");
    }

    IrReceiver.resume();
  }
}
```

> "Now you have a REMOTE CONTROL for your LEDs! Press 1 for red, 2 for green, 3 for blue, and power to turn them all off. You could add more buttons to make patterns, fade effects, or even control a servo!"

**Award: +30 XP for building the remote-controlled LED system!**

---

### Step 6: Wand Check -- IR Receiver Signal (5 min)

> "Let us use your Wand to peek at what the IR receiver is doing electrically."

**Wand Test -- IR Receiver Output:**

1. Set your Wand to DC Volts
2. Connect black probe to GND
3. Touch red probe to the IR receiver signal pin (pin 11)

**When no button is pressed:**
- The signal pin should read approximately 5V (pulled HIGH by default)

**When you hold a button on the remote:**
- The average voltage drops because the pin is pulsing LOW during the signal
- Your Wand might show 3-4V average while you hold a button

```
| Condition | Expected Voltage | Your Wand Reads |
|-----------|-----------------|----------------|
| No button pressed (idle) | ~4.5-5.0V | |
| Button held down | ~3.0-4.5V (average) | |
```

> "When no signal is coming in, the receiver holds the output at HIGH (5V). When it detects IR pulses, it pulls the line LOW in a pattern matching the remote's code. Your Wand shows the average of those highs and lows!"

**Award: +25 XP for measuring IR receiver signals!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What type of light does a TV remote use?
- A) Ultraviolet light
- B) Infrared light (invisible to human eyes)
- C) Green laser light

**(Correct: B -- +15 XP!)**

**Question 2:** Why does each button on a remote send a different code?
- A) Each button has a different battery
- B) Each button creates a unique pattern of IR light pulses that the receiver decodes
- C) The remote randomly generates numbers

**(Correct: B -- +15 XP!)**

**Question 3:** What does `IrReceiver.resume()` do in our code?
- A) Turns off the IR receiver
- B) Tells the receiver it is ready to listen for the next signal
- C) Sends a signal back to the remote

**(Correct: B -- +15 XP!)**

**Question 4:** If you point the remote but nothing happens, what should you check first?
- A) The color of the LED
- B) That the IR receiver dome is facing the remote and there is a clear line of sight
- C) The humidity in the room

**(Correct: B -- +15 XP!)**

---

## Lesson 40 Complete!

```
  =============================================

     IR CODE BREAKER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire an IR receiver module
     [check] Decode IR remote button codes
     [check] Build a remote-controlled LED system
     [check] Measured IR receiver signal with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- invisible flashlight | 10 |
| Understanding IR communication | 10 |
| Installing the library | 5 |
| Decoding 5+ buttons | 25 |
| Remote-controlled LED system | 30 |
| Wand Check (receiver signal) | 25 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **165** |

---

## Coming Up Next...

In **Lesson 41**, you will learn about the **PIR motion sensor** -- a sensor that detects when someone (or something) moves nearby by sensing their body heat! You will build an automatic security light that turns on when motion is detected. Your Wand will measure the HIGH and LOW output voltages!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| No codes show in Serial Monitor | Make sure the IR receiver dome faces the remote. Check wiring (signal to pin 11, VCC to 5V, GND to GND) |
| Getting 0xFFFFFFFF or weird codes | You are holding the button too long -- the receiver gets a repeat code. Use quick, short presses |
| Same code for every button | Some very old remotes are flaky. Try a different remote |
| LEDs do not respond to remote | Double-check that the codes in #define match YOUR decoded values exactly |
| Works only from very close | Replace the remote batteries. Also check for bright sunlight shining on the receiver -- sunlight contains IR and can interfere |
| Library install fails | Make sure you have the latest Arduino IDE. Try "IRremote" by shirriff/ArminJo |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 39: DC Motors and Motor Driver -- Spin Those Wheels! (L298N)](lesson-39-dc-motors-and-motor-driver.md) | [Lesson 41: PIR Motion Sensor -- Your Arduino's Security Guard →](lesson-41-pir-motion-sensor.md) |
