# Electronics to Robotics: A Course for Kids (Ages 8–14)

## Overview

This course takes kids on a hands-on journey from understanding basic electronic components all the way to building their own robots. No prior experience is needed. Every module builds on the last, with safe, fun experiments and real projects.

**Target Age Range:** 8–14 years
**Total Modules:** 6
**Total Estimated Lessons:** ~50 lessons (30–45 min each)
**Format:** Hands-on experiments + short concept sessions

---

## Course Roadmap

| Module | Topic | Lessons | Difficulty |
|--------|-------|---------|------------|
| 1 | Electronic Components Basics | 8 | ⭐ Beginner |
| 2 | Building Simple Circuits | 8 | ⭐⭐ Easy |
| 3 | Integrated Circuits (ICs) | 8 | ⭐⭐⭐ Intermediate |
| 4 | Arduino Microcontroller | 10 | ⭐⭐⭐ Intermediate |
| 5 | Sensors & Actuators | 8 | ⭐⭐⭐⭐ Advanced |
| 6 | Robotics Projects | 8 | ⭐⭐⭐⭐⭐ Expert |

---

## Safety Rules (Read First!)

> Teach these before touching any components.

1. **Never connect circuits to wall power (mains).** Use only batteries (AA, 9V) or USB-powered boards (Arduino).
2. **Always double-check wiring** before powering on.
3. **Don't touch components** while the circuit is powered unless you know it's safe.
4. **Keep water away** from all electronics.
5. **Handle components gently** — they can break or short-circuit if mishandled.
6. **Adult supervision** required for soldering (Module 3+).
7. If something **smells hot or smokes**, unplug immediately.

---

## Module 1: Electronic Components Basics

**Prerequisites:** None
**Lessons:** 8
**Difficulty:** ⭐ Beginner

### Learning Objectives
- Identify common electronic components by sight and name
- Understand what each component does in simple terms
- Read basic component markings (resistor color bands, capacitor values)

---

### Lesson 1: What is Electricity?

**Concepts:**
- Electricity = flow of electrons (like water flowing in a pipe)
- **Voltage (V):** pressure that pushes electrons (like water pressure)
- **Current (A):** how much electricity flows (like water flow rate)
- **Circuit:** a complete loop electricity travels through

**Analogy for Kids:**
> Imagine a garden hose. The water pump = battery, water pressure = voltage, water flow = current. If the hose has a kink (open circuit), water stops flowing.

**Hands-on Activity:**
- Use a 9V battery + LED + wire to light up an LED (with a resistor!)
- Show what happens when you break the circuit (LED goes off)

**Materials:** 9V battery, battery clip, 1x LED, 1x 330Ω resistor, 2x jumper wires

---

### Lesson 2: Resistors

**Concepts:**
- Resistors **limit current** — like squeezing a hose to slow water
- Unit: **Ohms (Ω)**
- Higher resistance = less current
- **Color bands** encode the resistance value

**Color Code Chart:**

| Color | Value |
|-------|-------|
| Black | 0 |
| Brown | 1 |
| Red | 2 |
| Orange | 3 |
| Yellow | 4 |
| Green | 5 |
| Blue | 6 |
| Violet | 7 |
| Gray | 8 |
| White | 9 |

**Hands-on Activity:**
- Read 5 different resistors using the color code
- Use a multimeter to verify the values
- Build a circuit: swap different resistors with an LED — observe brightness change

**Materials:** Assorted resistors (100Ω, 330Ω, 1kΩ, 10kΩ), LED, 9V battery, multimeter

---

### Lesson 3: Capacitors

**Concepts:**
- Capacitors **store electrical charge** — like a tiny rechargeable battery
- Unit: **Farads (F)** — most common: microfarads (µF), nanofarads (nF)
- Two types: **Ceramic** (no polarity) and **Electrolytic** (has + and – legs)
- Used for: filtering noise, timing circuits, energy storage

**Analogy for Kids:**
> A capacitor is like a water balloon — fill it up (charge), then let it go (discharge).

**Hands-on Activity:**
- Charge a large capacitor (1000µF) with a 9V battery
- Disconnect battery and use the capacitor to briefly light an LED
- Observe how quickly it discharges

**Materials:** 1000µF electrolytic capacitor, 9V battery, LED, 330Ω resistor

> ⚠️ **Safety:** Always connect electrolytic capacitors with correct polarity (+ to +). A reversed large capacitor can fail dangerously.

---

### Lesson 4: Diodes & LEDs

**Concepts:**
- **Diode:** one-way valve for electricity — current flows only one direction
- **Anode (+)**, **Cathode (–)** — longer leg is +
- **LED (Light Emitting Diode):** a diode that emits light
- **Forward voltage:** LEDs need ~2–3V to turn on
- Different LED colors = different voltages

**LED Color vs Forward Voltage:**

| Color | Forward Voltage |
|-------|----------------|
| Red | ~1.8–2.0V |
| Yellow | ~2.0–2.2V |
| Green | ~2.0–3.0V |
| Blue | ~3.0–3.4V |
| White | ~3.0–3.4V |

**Hands-on Activity:**
- Test LEDs in forward and reverse direction
- Build a 4-LED traffic light circuit with resistors

**Materials:** 4x LEDs (red, yellow, green, blue), 4x 330Ω resistors, 9V battery

---

### Lesson 5: Transistors

**Concepts:**
- Transistors = **electronic switches** (or amplifiers)
- 3 legs: **Base (B), Collector (C), Emitter (E)**
- Small current at base controls large current at collector
- **NPN type:** most common for beginners
- Used in almost every electronic device ever made!

**Analogy for Kids:**
> A transistor is like a faucet. A small turn of the handle (base signal) controls a large flow of water (collector current).

**Hands-on Activity:**
- Build a transistor switch: press a button → small current → transistor turns on → LED lights up
- This shows how microcontrollers can control high-power devices

**Materials:** 1x 2N2222 NPN transistor, 1x LED, 1x 10kΩ resistor, 1x 330Ω resistor, push button, 9V battery

---

### Lesson 6: Other Components — Switches, Buttons, Potentiometers

**Concepts:**
- **Push button:** momentary switch (on only while pressed)
- **Toggle switch:** stays on or off when flipped
- **Potentiometer:** variable resistor — twist to change resistance (0 to max Ω)

**Hands-on Activity:**
- Build a dimmer: potentiometer + LED — twist knob to change brightness
- Add a button to turn the circuit on/off

**Materials:** 10kΩ potentiometer, push button, LED, 330Ω resistor, 9V battery

---

### Lesson 7: Buzzers & Speakers

**Concepts:**
- **Passive buzzer:** needs a signal (AC) to make sound
- **Active buzzer:** has built-in oscillator, just needs power
- Sound = rapid vibration of a membrane

**Hands-on Activity:**
- Power an active buzzer with a battery
- Build a simple door alarm: button press = buzzer sounds

**Materials:** 1x active buzzer, 1x push button, 9V battery

---

### Lesson 8: Module 1 Project — Component ID Challenge & Quiz Board

**Project:** Build a "Quiz Board" where touching two wires completes a circuit and lights an LED to show a correct match.

**Materials:** Cardboard, 5x LEDs, 5x 330Ω resistors, jumper wires, 9V battery

**Assessment:**
- Name 10 components from a mixed pile
- Read 3 resistor values using color code
- Explain what a capacitor does in their own words

---

## Module 2: Building Simple Circuits

**Prerequisites:** Module 1
**Lessons:** 8
**Difficulty:** ⭐⭐ Easy

### Learning Objectives
- Understand Ohm's Law and use it to calculate resistor values
- Build series and parallel circuits
- Use a breadboard confidently
- Use a multimeter to measure voltage, current, and resistance

---

### Lesson 9: The Breadboard

**Concepts:**
- A breadboard lets you build circuits **without soldering**
- Rows are connected horizontally; power rails run vertically
- Component legs and wires plug into holes

**Breadboard Layout:**
```
  + - + - + - + - + - (power rails)
  [ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ]   ← connected in rows of 5
  [ ][ ][ ][ ][ ]
  + - + - + - + - + - (power rails)
```

**Hands-on Activity:**
- Build the LED circuit from Lesson 1 on a breadboard
- Rearrange components and rebuild

**Materials:** Breadboard, LED, 330Ω resistor, 9V battery, jumper wires

---

### Lesson 10: Ohm's Law

**Concepts:**
- **Ohm's Law:** V = I × R (Voltage = Current × Resistance)
- Rearranged: I = V/R, R = V/I
- Use this to calculate what resistor to use with an LED

**LED Resistor Calculation:**
```
Battery = 9V
LED forward voltage = 2V
Desired current = 20mA = 0.02A

R = (9V - 2V) / 0.02A = 7V / 0.02A = 350Ω → use 330Ω (nearest standard)
```

**Hands-on Activity:**
- Calculate correct resistors for 3 different LED colors
- Build the circuits and verify with a multimeter

---

### Lesson 11: Series Circuits

**Concepts:**
- In a **series circuit**, components are in a single loop
- Same current flows through all components
- Voltage is shared (divided) among components
- If one component fails, the whole circuit stops

**Hands-on Activity:**
- Wire 3 LEDs in series with one resistor
- Measure voltage across each LED with multimeter
- Remove one LED — observe what happens

---

### Lesson 12: Parallel Circuits

**Concepts:**
- In a **parallel circuit**, components share the same voltage
- Current is split between branches
- If one component fails, others keep working
- This is how home wiring works!

**Hands-on Activity:**
- Wire 3 LEDs in parallel, each with its own resistor
- Measure brightness vs series circuit
- Remove one LED — others stay on

---

### Lesson 13: Voltage Dividers

**Concepts:**
- Two resistors in series create an **output voltage** between them
- Formula: Vout = Vin × R2 / (R1 + R2)
- Used to scale voltages down and read sensors

**Hands-on Activity:**
- Build a voltage divider from 9V to 4.5V using two equal resistors
- Verify output with multimeter
- Build one that outputs 3V from 9V

---

### Lesson 14: Using a Multimeter

**Concepts:**
- **Voltmeter mode:** measure voltage (in parallel)
- **Ammeter mode:** measure current (in series)
- **Ohmmeter mode:** measure resistance (power off!)
- **Continuity mode:** beeps if circuit is complete

**Hands-on Activity:**
- Measure: battery voltage, LED voltage, resistor value
- Use continuity mode to test wires and switches

---

### Lesson 15: Power Sources

**Concepts:**
- **Batteries:** portable, limited energy (AA = 1.5V, 9V block, 18650 = 3.7V)
- **USB power:** 5V, good for Arduino
- **Battery holder vs barrel jack:** different connectors
- Batteries in **series** add voltage; in **parallel** add capacity

**Hands-on Activity:**
- Measure different battery voltages
- Wire 2x AA batteries in series to get 3V

---

### Lesson 16: Module 2 Project — Lighthouse Circuit

**Project:** Build a lighthouse using a blinking LED circuit with a capacitor and resistor timing network (simple RC blinker using a transistor).

**Circuit Concept:**
- Capacitor charges through resistor → triggers transistor → LED on → capacitor discharges → LED off → repeat
- Adjust blink speed by changing resistor value

**Materials:** Breadboard, 2x transistors (2N2222), 2x LEDs, 2x 100µF capacitors, 2x 10kΩ resistors, 2x 470Ω resistors, 9V battery

**Assessment:**
- Calculate resistor for a green LED from a 5V supply
- Explain the difference between series and parallel circuits
- Build a circuit from a simple schematic diagram

---

## Module 3: Integrated Circuits (ICs)

**Prerequisites:** Module 2
**Lessons:** 8
**Difficulty:** ⭐⭐⭐ Intermediate

### Learning Objectives
- Understand what an IC is and why they exist
- Use the 555 timer IC to build timing circuits
- Understand basic logic gates
- Read IC datasheets (simplified)

---

### Lesson 17: What is an Integrated Circuit?

**Concepts:**
- An IC = many transistors, resistors, capacitors on a tiny chip
- A 555 timer chip contains 23 transistors!
- ICs have **pins** — each pin has a specific function
- **DIP package:** two rows of pins (easy for breadboard)
- **Datasheet:** the manual for every IC

**Hands-on Activity:**
- Examine a 555 timer under magnifying glass
- Look at a simplified 555 datasheet together
- Identify pin numbers and names

---

### Lesson 18: The 555 Timer — Blinker Mode (Astable)

**Concepts:**
- **Astable mode:** 555 oscillates — output switches on/off repeatedly
- Timing set by: R1, R2, and C values
- **Frequency formula:** f ≈ 1.44 / ((R1 + 2×R2) × C)

**555 Astable Circuit:**
```
         +9V
          |
         [R1] ← 1kΩ
          |
         [R2] ← 10kΩ
          |-----> Pin 7 (Discharge)
          |
         [C1] ← 47µF     555
    GND --+              ┌────┐
                    Pin1─┤GND │
              Pin4,8─┤RST,VCC
              Pin2,6─┤TRG,THR
                Pin7─┤DIS │
                Pin3─┤OUT ├──> LED ──[330Ω]── GND
                    └────┘
```

**Hands-on Activity:**
- Build 555 blinker circuit
- Change R2 or C1 to change blink speed
- Calculate expected frequency, verify visually

**Materials:** 555 timer IC, resistors (1kΩ, 10kΩ), 47µF capacitor, LED, 330Ω resistor, breadboard

---

### Lesson 19: The 555 Timer — One-Shot Mode (Monostable)

**Concepts:**
- **Monostable mode:** one trigger → one timed pulse
- Used for: delays, debouncing buttons, timed events
- Time period: T = 1.1 × R × C

**Hands-on Activity:**
- Build a "touch-to-light" circuit: press button → LED stays on for 5 seconds
- Change R and C to get 10 seconds, then 1 second

---

### Lesson 20: Logic Gates — AND, OR, NOT

**Concepts:**
- Logic gates process **binary signals** (1 = high/on, 0 = low/off)
- **NOT gate:** output is opposite of input
- **AND gate:** output is 1 only if ALL inputs are 1
- **OR gate:** output is 1 if ANY input is 1
- **Truth tables** show all possible input/output combinations

**Truth Table — AND:**

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Hands-on Activity:**
- Use a 7408 AND gate IC (or simulate with switches and transistors)
- Build all 4 combinations and verify with an LED

---

### Lesson 21: Logic Gates — NAND, NOR, XOR

**Concepts:**
- **NAND:** AND then NOT (most universal gate)
- **NOR:** OR then NOT
- **XOR:** output is 1 only when inputs are **different**

**Hands-on Activity:**
- Use 7400 NAND gate IC to build a NOT gate (connect both inputs together)
- Build a half adder using XOR + AND gates

---

### Lesson 22: IC 7-Segment Display

**Concepts:**
- A 7-segment display has 7 LED segments labeled a–g
- **BCD to 7-segment decoder IC (7447):** converts binary number to display segments
- Used in digital clocks, calculators

**Hands-on Activity:**
- Wire a 7-segment display directly (manually control each segment)
- Then use 7447 decoder IC with 4 switches to display digits 0–9

---

### Lesson 23: Building a Simple Counter

**Concepts:**
- **555 + 4017 counter IC:** 555 provides pulses, 4017 counts them
- Each pulse activates next output pin (10 outputs)

**Hands-on Activity:**
- Build a "chaser" circuit: 10 LEDs light up one at a time in sequence
- Adjust 555 speed to make chaser faster/slower

**Materials:** 555 timer, 4017 decade counter IC, 10x LEDs, 10x 330Ω resistors

---

### Lesson 24: Module 3 Project — Digital Dice

**Project:** Build an electronic dice using a 555 timer (fast counter) and LEDs arranged in a dice pattern. Press a button to "roll" — LED pattern shows 1–6.

**Materials:** 555 timer, 4017 counter IC, 6x LEDs, resistors, push button, 9V battery

**Assessment:**
- Explain what an IC is
- Draw the truth table for an AND gate
- Calculate 555 timing for a 1Hz blink

---

## Module 4: Arduino Microcontroller

**Prerequisites:** Module 3
**Lessons:** 10
**Difficulty:** ⭐⭐⭐ Intermediate

### Learning Objectives
- Understand what a microcontroller is
- Set up Arduino IDE and upload first program
- Control digital outputs (LEDs, buzzers)
- Read digital inputs (buttons)
- Use analog inputs and PWM outputs
- Understand basic programming concepts (variables, loops, conditions)

---

### Lesson 25: What is a Microcontroller?

**Concepts:**
- A microcontroller = CPU + memory + I/O on one chip
- **Arduino:** beginner-friendly microcontroller board
- Arduino Uno has 14 digital pins, 6 analog pins, USB connection
- Programs are called **sketches**

**Arduino Uno Key Parts:**
```
┌─────────────────────────────────────┐
│  USB Port   [Reset]   Power LED     │
│                                     │
│  Digital Pins 0-13                  │
│  [0][1][2][3][4][5][6][7][8]...    │
│                                     │
│         ATmega328P                  │
│           (chip)                    │
│                                     │
│  Analog Pins A0-A5                  │
│  Power Pins: 5V, 3.3V, GND         │
└─────────────────────────────────────┘
```

**Hands-on Activity:**
- Install Arduino IDE on computer
- Connect Arduino via USB
- Upload the built-in "Blink" example sketch

---

### Lesson 26: Your First Sketch — Blink

**Concepts:**
- `setup()`: runs once at start
- `loop()`: runs forever
- `pinMode(pin, OUTPUT)`: configure a pin
- `digitalWrite(pin, HIGH/LOW)`: set pin on or off
- `delay(ms)`: wait in milliseconds

**Code:**
```cpp
void setup() {
  pinMode(13, OUTPUT);  // Built-in LED is pin 13
}

void loop() {
  digitalWrite(13, HIGH);  // LED on
  delay(1000);             // Wait 1 second
  digitalWrite(13, LOW);   // LED off
  delay(1000);             // Wait 1 second
}
```

**Hands-on Activity:**
- Upload blink sketch
- Modify delay to 200ms — observe faster blink
- Add an external LED on pin 7

---

### Lesson 27: Variables and Serial Monitor

**Concepts:**
- **Variables:** store values (int, float, bool, String)
- **Serial.begin(9600):** start communication with computer
- **Serial.println():** print text to Serial Monitor
- Serial Monitor = window to "talk" to your Arduino

**Code:**
```cpp
int blinkSpeed = 500;  // variable: delay in ms

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino is ready!");
}

void loop() {
  digitalWrite(13, HIGH);
  delay(blinkSpeed);
  digitalWrite(13, LOW);
  delay(blinkSpeed);
  Serial.println("Blink!");
}
```

**Hands-on Activity:**
- Print "Hello World!" to Serial Monitor
- Print a counter that increases every second

---

### Lesson 28: Reading Digital Inputs — Buttons

**Concepts:**
- `pinMode(pin, INPUT_PULLUP)`: button pin with internal pull-up resistor
- `digitalRead(pin)`: reads HIGH or LOW
- **If statement:** make decisions in code

**Code:**
```cpp
int buttonPin = 2;
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {  // pressed = LOW with pullup
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

**Hands-on Activity:**
- Build LED on/off button circuit
- Add a second button to control a second LED
- Make button toggle LED (on/off with each press)

---

### Lesson 29: Analog Inputs

**Concepts:**
- Analog pins read 0–5V and return values **0–1023**
- `analogRead(pin)`: read analog value
- Used with: potentiometers, light sensors, temperature sensors

**Code:**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(A0);        // read potentiometer
  float voltage = value * (5.0 / 1023.0);  // convert to volts
  Serial.print("Value: ");
  Serial.print(value);
  Serial.print("  Voltage: ");
  Serial.println(voltage);
  delay(100);
}
```

**Hands-on Activity:**
- Connect potentiometer to A0
- Print value and voltage to Serial Monitor
- Turn knob and observe values change

---

### Lesson 30: PWM — Dimming LEDs and Controlling Speed

**Concepts:**
- **PWM (Pulse Width Modulation):** rapidly switching on/off to simulate analog output
- Pins marked with `~` on Arduino support PWM (3, 5, 6, 9, 10, 11)
- `analogWrite(pin, 0-255)`: 0 = always off, 255 = always on, 127 = 50% brightness
- Used for: LED dimming, motor speed control

**Code:**
```cpp
int ledPin = 9;  // PWM pin

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Fade in
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
  // Fade out
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
}
```

**Hands-on Activity:**
- Build LED fade in/out circuit
- Control LED brightness with a potentiometer

---

### Lesson 31: For Loops and Arrays

**Concepts:**
- **for loop:** repeat code a set number of times
- **Arrays:** store multiple values in one variable
- Useful for controlling multiple LEDs

**Code:**
```cpp
int leds[] = {3, 5, 6, 9, 10, 11};  // 6 LED pins
int numLeds = 6;

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  // Knight Rider effect
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(leds[i], HIGH);
    delay(100);
    digitalWrite(leds[i], LOW);
  }
  for (int i = numLeds - 1; i >= 0; i--) {
    digitalWrite(leds[i], HIGH);
    delay(100);
    digitalWrite(leds[i], LOW);
  }
}
```

**Hands-on Activity:**
- Build Knight Rider LED chaser with 6 LEDs
- Modify to change speed

---

### Lesson 32: Piezo Buzzer and Tones

**Concepts:**
- `tone(pin, frequency, duration)`: play a tone on a buzzer
- `noTone(pin)`: stop tone
- Musical notes have specific frequencies (A4 = 440Hz)

**Note Frequencies:**
```
C4 = 262 Hz    D4 = 294 Hz    E4 = 330 Hz    F4 = 349 Hz
G4 = 392 Hz    A4 = 440 Hz    B4 = 494 Hz    C5 = 523 Hz
```

**Code:**
```cpp
int buzzerPin = 8;

void setup() {
  // Play a simple tune: C D E F G
  tone(buzzerPin, 262, 300); delay(350);  // C
  tone(buzzerPin, 294, 300); delay(350);  // D
  tone(buzzerPin, 330, 300); delay(350);  // E
  tone(buzzerPin, 349, 300); delay(350);  // F
  tone(buzzerPin, 392, 300); delay(350);  // G
  noTone(buzzerPin);
}

void loop() {}
```

**Hands-on Activity:**
- Play "Happy Birthday" or "Twinkle Twinkle Little Star"
- Build a piano with 8 buttons, each playing a note

---

### Lesson 33: LCD Display (16x2)

**Concepts:**
- LCD = Liquid Crystal Display
- 16x2 LCD has 2 rows, 16 characters each
- Use with **I2C adapter** for easy 4-wire connection
- Library: `LiquidCrystal_I2C`

**Wiring (I2C):**
```
LCD VCC  → Arduino 5V
LCD GND  → Arduino GND
LCD SDA  → Arduino A4
LCD SCL  → Arduino A5
```

**Code:**
```cpp
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Hello World!");
  lcd.setCursor(0, 1);
  lcd.print("Arduino Rocks!");
}

void loop() {}
```

**Hands-on Activity:**
- Display name and age on LCD
- Build a countdown timer displayed on LCD

---

### Lesson 34: Module 4 Project — Digital Piano + Display

**Project:** Build a piano with 8 buttons. Each button plays a musical note. The LCD shows the note name being played.

**Materials:** Arduino Uno, breadboard, 8x push buttons, piezo buzzer, 16x2 LCD (I2C), resistors, jumper wires, USB cable

**Assessment:**
- Write a sketch from scratch that blinks an LED 5 times then stops
- Explain what `loop()` does
- Read a potentiometer and control LED brightness

---

## Module 5: Sensors & Actuators

**Prerequisites:** Module 4
**Lessons:** 8
**Difficulty:** ⭐⭐⭐⭐ Advanced

### Learning Objectives
- Interface common sensors with Arduino
- Control servo motors and DC motors
- Understand how to convert sensor data into actions
- Build sensor-driven interactive projects

---

### Lesson 35: Temperature Sensor (DHT11/DHT22)

**Concepts:**
- DHT11 measures temperature (0–50°C) and humidity (20–90%)
- Communicates digitally — one wire data
- Library: `DHT.h`

**Code:**
```cpp
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  Serial.print("Temp: "); Serial.print(temp); Serial.print("°C  ");
  Serial.print("Humidity: "); Serial.print(humid); Serial.println("%");
  delay(2000);
}
```

**Hands-on Activity:**
- Display temperature on Serial Monitor and LCD
- Turn on a fan (motor) if temperature > 28°C

---

### Lesson 36: Light Sensor (LDR — Light Dependent Resistor)

**Concepts:**
- LDR changes resistance based on light — bright = low resistance
- Used in voltage divider to give analog reading
- `map(value, in_min, in_max, out_min, out_max)`: rescale values

**Code:**
```cpp
void loop() {
  int lightVal = analogRead(A0);
  int brightness = map(lightVal, 0, 1023, 0, 255);
  analogWrite(9, brightness);  // LED brightness follows light level
  delay(50);
}
```

**Hands-on Activity:**
- Build auto night light: dim when bright, bright when dark
- Measure sunrise/sunset effect by covering LDR

---

### Lesson 37: Ultrasonic Distance Sensor (HC-SR04)

**Concepts:**
- Sends ultrasonic pulse, measures echo time to calculate distance
- Range: 2cm – 400cm, accuracy ±3mm
- Pins: VCC, GND, Trig (send), Echo (receive)
- Distance formula: `distance = (duration × 0.034) / 2`

**Code:**
```cpp
int trigPin = 9, echoPin = 10;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW); delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;
  Serial.print("Distance: "); Serial.print(distance); Serial.println(" cm");
  delay(100);
}
```

**Hands-on Activity:**
- Display distance on LCD
- Buzzer beeps faster as object gets closer (like car parking sensor)

---

### Lesson 38: Servo Motors

**Concepts:**
- Servo = small motor with position control (0°–180°)
- 3 wires: VCC (red), GND (brown/black), Signal (yellow/orange)
- Library: `Servo.h`
- `servo.write(angle)`: moves to angle

**Code:**
```cpp
#include <Servo.h>
Servo myServo;

void setup() {
  myServo.attach(9);
}

void loop() {
  for (int angle = 0; angle <= 180; angle += 10) {
    myServo.write(angle);
    delay(100);
  }
  for (int angle = 180; angle >= 0; angle -= 10) {
    myServo.write(angle);
    delay(100);
  }
}
```

**Hands-on Activity:**
- Build a servo-powered door opener controlled by a button
- Control servo angle with a potentiometer

**Materials:** SG90 servo motor, potentiometer, Arduino, breadboard

---

### Lesson 39: DC Motors and Motor Driver (L298N)

**Concepts:**
- DC motors need more current than Arduino can provide
- **L298N motor driver:** H-bridge IC, controls speed and direction
- PWM controls motor speed; digital pins control direction
- Can drive 2 motors independently

**Wiring:**
```
L298N → Arduino
IN1   → Pin 2  (direction)
IN2   → Pin 3  (direction)
ENA   → Pin 9  (PWM speed)
VCC   → Motor battery (7-12V)
GND   → Common GND
```

**Code:**
```cpp
int IN1 = 2, IN2 = 3, ENA = 9;

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // Forward
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  analogWrite(ENA, 200);  // 78% speed
  delay(2000);
  // Backward
  digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH);
  analogWrite(ENA, 150);
  delay(2000);
  // Stop
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
  delay(1000);
}
```

**Hands-on Activity:**
- Control motor forward, backward, speed
- Build a fan with adjustable speed using potentiometer

---

### Lesson 40: IR Sensor and Remote Control

**Concepts:**
- IR (infrared) sensor detects IR light pulses from remotes
- TV remotes, A/C remotes use IR signals
- Library: `IRremote.h`
- Each button has a unique code

**Hands-on Activity:**
- Decode button codes from an old TV remote
- Build: press remote button → control LED or servo

---

### Lesson 41: PIR Motion Sensor

**Concepts:**
- PIR = Passive Infrared sensor
- Detects movement by sensing heat (body heat)
- Output: HIGH when motion detected, LOW when still
- Used in: security lights, alarms, automatic doors

**Code:**
```cpp
int pirPin = 7, ledPin = 13;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (digitalRead(pirPin) == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Motion detected!");
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(100);
}
```

**Hands-on Activity:**
- Build automatic night light: PIR + LDR + LED
  - Light only turns on if: motion detected AND it's dark

---

### Lesson 42: Module 5 Project — Smart Room System

**Project:** Build a "Smart Room" that:
1. Shows temperature and humidity on LCD
2. Automatically turns on a fan if temperature > threshold
3. Turns on a light (LED) when motion detected at night (LDR check)
4. Displays distance of nearest object (ultrasonic)

**Materials:** Arduino, DHT11, LDR, PIR sensor, HC-SR04, DC motor + L298N, LED, 16x2 LCD (I2C)

**Assessment:**
- Connect and read 3 different sensors
- Control a servo with sensor input
- Explain how ultrasonic distance measurement works

---

## Module 6: Robotics Projects

**Prerequisites:** Module 5
**Lessons:** 8
**Difficulty:** ⭐⭐⭐⭐⭐ Expert

### Learning Objectives
- Understand robot chassis and drive systems
- Build and program a line-following robot
- Build an obstacle-avoiding robot
- Understand basic autonomous decision-making
- Complete a final capstone robot project

---

### Lesson 43: Robot Basics — Chassis, Motors, Power

**Concepts:**
- **Chassis:** the body/frame of the robot
- **Differential drive:** 2 motors, steer by varying speed/direction
  - Both forward = straight
  - Left fast, right slow = turn right
  - Left forward, right backward = spin in place
- **Power:** separate battery for motors (don't power motors from Arduino 5V!)

**Hands-on Activity:**
- Assemble 2-wheel robot chassis kit
- Wire 2x DC motors to L298N motor driver
- Power Arduino from USB or separate 9V battery
- Test: drive forward, backward, turn left, turn right

**Materials:**
- 2WD robot chassis kit (with 2x DC motors, wheels, caster wheel)
- L298N motor driver
- Arduino Uno
- 4x AA battery holder (for motors)
- 9V battery (for Arduino)
- Jumper wires

---

### Lesson 44: Robot Movement Functions

**Concepts:**
- Write reusable **functions** for robot movement
- Functions make code readable and easy to change

**Code:**
```cpp
// Motor pins
int leftIN1 = 2, leftIN2 = 3, leftENA = 9;
int rightIN1 = 4, rightIN2 = 5, rightENB = 10;

void forward(int speed) {
  digitalWrite(leftIN1, HIGH);  digitalWrite(leftIN2, LOW);
  digitalWrite(rightIN1, HIGH); digitalWrite(rightIN2, LOW);
  analogWrite(leftENA, speed);  analogWrite(rightENB, speed);
}

void backward(int speed) {
  digitalWrite(leftIN1, LOW);  digitalWrite(leftIN2, HIGH);
  digitalWrite(rightIN1, LOW); digitalWrite(rightIN2, HIGH);
  analogWrite(leftENA, speed); analogWrite(rightENB, speed);
}

void turnLeft(int speed) {
  digitalWrite(leftIN1, LOW);   digitalWrite(leftIN2, HIGH);
  digitalWrite(rightIN1, HIGH); digitalWrite(rightIN2, LOW);
  analogWrite(leftENA, speed);  analogWrite(rightENB, speed);
}

void stopRobot() {
  digitalWrite(leftIN1, LOW);  digitalWrite(leftIN2, LOW);
  digitalWrite(rightIN1, LOW); digitalWrite(rightIN2, LOW);
}

void loop() {
  forward(180); delay(2000);
  turnLeft(180); delay(600);
  forward(180); delay(2000);
  stopRobot(); delay(1000);
}
```

**Hands-on Activity:**
- Drive robot in a square path
- Drive robot in a figure-8

---

### Lesson 45: Line-Following Robot

**Concepts:**
- **IR line sensor:** detects black line on white surface (or vice versa)
- White reflects IR → sensor reads HIGH
- Black absorbs IR → sensor reads LOW
- Use 2 sensors (left and right) for steering

**Line Following Logic:**
```
Left  Right  → Action
HIGH  HIGH   → Both on line: go forward
LOW   HIGH   → Left off line: turn left
HIGH  LOW    → Right off line: turn right
LOW   LOW    → Lost line: stop or search
```

**Code:**
```cpp
int leftSensor = 7, rightSensor = 8;

void loop() {
  int L = digitalRead(leftSensor);
  int R = digitalRead(rightSensor);

  if (L == HIGH && R == HIGH) forward(180);
  else if (L == LOW && R == HIGH) turnLeft(150);
  else if (L == HIGH && R == LOW) turnRight(150);
  else stopRobot();
}
```

**Hands-on Activity:**
- Make a track with black electrical tape on white cardboard
- Tune sensor height and motor speed for smooth following
- Try curved tracks vs sharp corners

**Materials:** 2x IR line sensor modules, black electrical tape, white cardboard/poster

---

### Lesson 46: Obstacle-Avoiding Robot

**Concepts:**
- Mount HC-SR04 ultrasonic sensor on front of robot
- If obstacle < 20cm: stop, look around, choose direction
- Servo rotates ultrasonic sensor to scan left and right

**Code:**
```cpp
#include <Servo.h>
Servo scanServo;
int trigPin = 11, echoPin = 12;

int getDistance() {
  digitalWrite(trigPin, LOW); delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long dur = pulseIn(echoPin, HIGH);
  return dur * 0.034 / 2;
}

void loop() {
  int dist = getDistance();

  if (dist > 20) {
    forward(180);
  } else {
    stopRobot();
    delay(300);

    scanServo.write(0);  delay(500);
    int leftDist = getDistance();

    scanServo.write(180); delay(500);
    int rightDist = getDistance();

    scanServo.write(90);  delay(300);

    if (leftDist > rightDist) turnLeft(180);
    else turnRight(180);
    delay(400);
  }
}
```

**Hands-on Activity:**
- Set up obstacle course with cardboard boxes
- Test robot navigating the course autonomously
- Adjust thresholds for tighter spaces

**Materials:** HC-SR04 sensor, SG90 servo (for scanning), servo mount bracket

---

### Lesson 47: Adding a Buzzer and LEDs — Robot Personality

**Concepts:**
- Good robots give feedback: lights and sounds
- Add LED "eyes" that react to robot state
- Buzzer plays sounds for: start, obstacle, turning

**Hands-on Activity:**
- Red LEDs flash when reversing
- Buzzer beeps when obstacle detected
- Green LED on when driving forward
- Add a startup "boot sequence" with lights and sound

---

### Lesson 48: Remote-Controlled Robot (Bluetooth)

**Concepts:**
- **HC-05 Bluetooth module:** adds wireless serial communication
- Connect phone app (e.g., "Arduino Bluetooth Controller") to send commands
- Commands are single characters: F (forward), B (backward), L (left), R (right), S (stop)

**Code:**
```cpp
#include <SoftwareSerial.h>
SoftwareSerial bluetooth(10, 11);  // RX, TX

void loop() {
  if (bluetooth.available()) {
    char cmd = bluetooth.read();
    if (cmd == 'F') forward(200);
    else if (cmd == 'B') backward(200);
    else if (cmd == 'L') turnLeft(180);
    else if (cmd == 'R') turnRight(180);
    else if (cmd == 'S') stopRobot();
  }
}
```

**Hands-on Activity:**
- Pair phone with HC-05
- Drive robot around the room with phone
- Build obstacle course and try to navigate it

**Materials:** HC-05 Bluetooth module, smartphone with Bluetooth controller app

---

### Lesson 49: Robot Arm Introduction (Servo-Based)

**Concepts:**
- Robot arm uses multiple servo motors for joints
- **Degrees of freedom (DOF):** number of independent movements
- 3-DOF arm: base rotation, shoulder, elbow
- Control each joint with a potentiometer

**Hands-on Activity:**
- Build 3-servo arm from cardboard/popsicle sticks
- Control each servo with one potentiometer
- Try to pick up a small object (attach cardboard gripper)

**Materials:** 3x SG90 servo motors, 3x potentiometers, popsicle sticks, hot glue gun (adult use)

---

### Lesson 50: Final Capstone Project — Your Robot Challenge

**Choose one (or combine!):**

#### Option A: The Maze Solver
Build a robot that can navigate through a cardboard maze using ultrasonic sensing and follow the "left wall" algorithm.

#### Option B: The Delivery Bot
Robot follows a line track, stops at marked stations, and makes a "beep" to signal delivery. Uses IR line sensors + IR color markers.

#### Option C: The Security Bot
Patrols a route autonomously, uses PIR sensor to detect intruders, flashes lights and sounds alarm when triggered.

#### Option D: The Robot Arm Game
Control a servo arm with joystick (2x potentiometers), try to pick up objects and move them to target zones within a time limit.

---

**Final Project Requirements:**
- Robot must use at least 3 different sensors or modules
- Must have autonomous behavior (not just remote control)
- Must display status information (LCD or Serial)
- Present and demonstrate to family/friends
- Explain how it works (what each component does)

---

## Complete Materials List

### Starter Kit (Modules 1–2)
| Item | Quantity | Approx. Cost |
|------|----------|-------------|
| Assorted resistors (pack) | 1 | $3 |
| Assorted capacitors | 1 | $3 |
| LEDs (red, green, blue, yellow) | 5 each | $3 |
| 2N2222 NPN transistors | 10 | $2 |
| Push buttons | 10 | $2 |
| 10kΩ potentiometers | 3 | $2 |
| Active buzzers | 2 | $2 |
| 830-point breadboard | 2 | $6 |
| Jumper wires (pack) | 1 | $4 |
| 9V batteries + clips | 4 | $6 |
| Digital multimeter | 1 | $12 |

### IC Kit (Module 3)
| Item | Quantity | Approx. Cost |
|------|----------|-------------|
| 555 timer ICs | 5 | $3 |
| 7400 NAND gate IC | 2 | $2 |
| 4017 decade counter IC | 2 | $2 |
| 7-segment display | 2 | $3 |
| 7447 BCD decoder IC | 2 | $2 |

### Arduino Kit (Modules 4–5)
| Item | Quantity | Approx. Cost |
|------|----------|-------------|
| Arduino Uno | 1 | $20 |
| USB A-to-B cable | 1 | $3 |
| 16x2 LCD with I2C backpack | 1 | $8 |
| DHT11 temperature sensor | 1 | $3 |
| LDR (light sensor) | 2 | $1 |
| HC-SR04 ultrasonic sensor | 2 | $4 |
| SG90 servo motor | 3 | $9 |
| L298N motor driver | 1 | $4 |
| PIR motion sensor | 1 | $3 |

### Robotics Kit (Module 6)
| Item | Quantity | Approx. Cost |
|------|----------|-------------|
| 2WD robot chassis kit | 1 | $12 |
| IR line sensors | 2 | $4 |
| HC-05 Bluetooth module | 1 | $6 |
| 4x AA battery holder | 2 | $3 |
| Servo bracket/mount | 1 | $3 |

**Estimated Total: ~$125–$150**

> Many items can be bought in starter kits for less. Amazon, AliExpress, and Adafruit are good sources.

---

## Tips for Parents & Instructors

### Teaching Ages 8–10
- Focus on Modules 1–2 first, spending extra time on each
- Use lots of analogies (water, cars, switches)
- Let them experiment and make mistakes safely
- Celebrate every lit LED!
- Skip math details — just use the formulas as recipes

### Teaching Ages 11–12
- Can handle Modules 1–4 at normal pace
- Introduce basic math (Ohm's Law, frequency formulas)
- Start explaining *why* things work, not just *how*
- Encourage them to modify examples and break things (safely!)

### Teaching Ages 13–14
- Can handle the full course
- Challenge them to modify projects beyond the instructions
- Introduce reading datasheets independently
- Encourage them to search Arduino forums and fix bugs
- Consider entering a school science fair or robotics competition

### General Tips
- **30–45 min sessions** work best for kids
- Always start with "why does this matter?" — real-world examples
- **Let them struggle** a bit before helping — problem-solving is the skill
- Document progress with photos/videos — kids love seeing their projects
- Join local maker spaces or robotics clubs for community
- YouTube channels: Paul McWhorter (Arduino), Great Scott, Andreas Spiess

---

## Progression Checkpoints

| After Module | Kid Should Be Able To... |
|-------------|--------------------------|
| 1 | Name 8 components, read resistor color codes, build LED circuits |
| 2 | Use Ohm's Law, build series/parallel circuits, use a multimeter |
| 3 | Build a 555 timer circuit, explain logic gates, read IC pinouts |
| 4 | Write Arduino sketches, control LEDs/buzzers, read buttons & sensors |
| 5 | Interface 4+ sensors, control servos & DC motors, build sensor-driven projects |
| 6 | Build autonomous robots, write movement logic, complete a capstone robot |

---

*Happy building! The best part of this journey is watching kids go from "what is a resistor?" to having a robot they built themselves navigate a room on its own.*
