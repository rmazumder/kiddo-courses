# Lesson 30: PWM -- Dimming LEDs and Controlling Speed

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, so far your LED has been either ON or OFF. But have you noticed how phone screens can dim smoothly? Or how fans can spin at different speeds? Today you will learn the Arduino's secret trick: **PWM (Pulse Width Modulation)**. It switches the pin on and off SO FAST that your eyes see a smooth dim or bright effect. You will fade an LED like a sunset and use the Wand to catch the trick in action!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what PWM means and why it works
- Identify which Arduino pins support PWM (the ones marked with ~)
- Use `analogWrite()` to set brightness from 0 to 255
- Build a smooth LED fade-in and fade-out effect
- Control LED brightness with a potentiometer
- Measure PWM average voltage with the Wand at different levels

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| Breadboard | 1 |
| LED (any color) | 1 |
| 330-ohm resistor | 1 |
| 10k-ohm potentiometer | 1 |
| Jumper wires | 5 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Flickering Trick (3 min)

> "Wave your hand really fast in front of your face. Can you see your fingers clearly? No! They blur together. Your eyes cannot keep up with fast movement."

> "The Arduino uses the same trick with electricity. Instead of truly dimming an LED, it turns the LED on and off HUNDREDS of times per second. Your eyes blur the flashes together and it LOOKS dimmer. The faster the blinks, the brighter it appears. This trick is called PWM -- Pulse Width Modulation."

**The Key Insight:**

```
  Full brightness (255):  ON ON ON ON ON ON ON ON ON ON
  Half brightness (127):  ON -- ON -- ON -- ON -- ON --
  Quarter brightness (64): ON -- -- -- ON -- -- -- ON --
  Off (0):                -- -- -- -- -- -- -- -- -- --
```

> "The LED is never ACTUALLY dimmer. It is just spending more or less time turned ON."

**Award: +10 XP for understanding the PWM trick!**

---

### Step 2: PWM Pins on the Arduino (5 min)

Not all Arduino pins can do PWM. Only the ones marked with a **~** (tilde) on the board:

```
  PWM Pins on Arduino Uno:
  ~3   ~5   ~6   ~9   ~10   ~11

  These 6 pins can use analogWrite()
  The other digital pins can ONLY do HIGH or LOW
```

> "Look at your Arduino board. See the tiny ~ symbol next to some pin numbers? Those are the PWM pins. Today we will use pin 9."

**The Command:**

| Command | What It Does | Range |
|---------|-------------|-------|
| `analogWrite(pin, 0)` | Completely OFF | Minimum |
| `analogWrite(pin, 127)` | Half brightness | Middle |
| `analogWrite(pin, 255)` | Full brightness | Maximum |

> "analogWrite goes from 0 (always off) to 255 (always on). 127 is roughly half."

**Award: +10 XP for identifying PWM pins!**

---

### Step 3: Build the Fade Circuit (5 min)

**Move your LED to a PWM pin!**

```
  Arduino Uno                    Breadboard
  +---------+
  | Pin ~9  |----[wire]---[330-ohm]---LED(+)---LED(-)---GND
  +---------+

  (Same circuit as before, but using pin 9 instead of pin 7)
```

**Steps:**
1. Move the wire from pin 7 to **pin 9** (a PWM pin marked with ~)
2. Keep the 330-ohm resistor and LED wired the same way

**Award: +10 XP for rewiring to a PWM pin!**

---

### Step 4: The Fade Code (10 min)

**Smooth Fade In and Out:**

```cpp
// Lesson 30: LED Fade with PWM

int ledPin = 9;  // Must be a PWM pin (~)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== PWM Fade Started! ===");
}

void loop() {
  // Fade IN: 0 to 255
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);
    delay(10);  // Small delay so you can see the fade
  }

  Serial.println("Full brightness!");

  // Fade OUT: 255 to 0
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);
    delay(10);
  }

  Serial.println("Faded to dark.");
  delay(500);  // Pause before repeating
}
```

**Upload and watch the LED!**

> "It fades in slowly like a sunrise, then fades out like a sunset. But the LED is not really dimming -- it is blinking on and off at 490 times per second, spending more and more time ON during the fade-in."

**How the For Loop Works:**

> "The `for` loop is like a counter. It starts at 0, adds 1 each time, and keeps going until it reaches 255. Each step, it sets the LED brightness to the current count."

```
for (start; keep going while true; change each time)
for (int brightness = 0; brightness <= 255; brightness++)
```

**Award: +30 XP for a smooth LED fade!**

---

### Step 5: Potentiometer-Controlled Brightness (5 min)

**Add the potentiometer from Lesson 29:**

```cpp
int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(A0);              // 0 to 1023
  int brightness = potValue / 4;              // Scale to 0 to 255

  analogWrite(ledPin, brightness);

  Serial.print("Pot: ");
  Serial.print(potValue);
  Serial.print("  Brightness: ");
  Serial.println(brightness);

  delay(50);
}
```

> "Now twist the knob and watch the LED smoothly dim and brighten! You just built a real dimmer switch -- the same technology used in your house lights."

**Why divide by 4?**

> "analogRead gives 0 to 1023 (1024 steps). analogWrite needs 0 to 255 (256 steps). 1024 / 4 = 256. So dividing by 4 scales it perfectly."

**Award: +20 XP for building a real dimmer!**

---

### Step 6: Wand Check -- The PWM Voltage Trick (10 min)

> "Here is the really cool part. The Arduino is not ACTUALLY putting out less voltage. It is switching between 5V and 0V super fast. But your Wand will show you the AVERAGE voltage. Let us test it!"

**Setup:**
1. Use the potentiometer-controlled brightness sketch
2. Set the Wand to **DC Voltage**
3. Black probe on **GND**, red probe on **pin 9**

**The Experiment:**

Set the potentiometer to different positions and record the Wand reading:

```
| analogWrite Value | Expected Average Voltage | Wand Reads |
|-------------------|-------------------------|------------|
| 0 (knob at min)   | 0.0V                    |            |
| 64 (quarter)      | ~1.25V                  |            |
| 127 (half)        | ~2.50V                  |            |
| 191 (three-quarter)| ~3.75V                 |            |
| 255 (knob at max) | ~5.0V                   |            |
```

**The Math:**

> "Average voltage = (analogWrite value / 255) * 5V"
>
> "So 127/255 * 5V = 2.49V. The Wand reads about 2.5V. But the pin is NOT actually putting out 2.5V -- it is rapidly switching between 5V and 0V, spending about 50% of the time at 5V. The Wand just averages it out!"

**This is the key PWM insight:**

```
  analogWrite(pin, 127) does NOT output 2.5V

  It actually does this 490 times per second:
  [5V][0V][5V][0V][5V][0V][5V][0V]...
  ON   OFF ON  OFF ON  OFF ON  OFF

  Average = 2.5V (which is what the Wand shows)
```

**Award: +50 XP for measuring PWM voltage at 5 different levels!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does PWM stand for?
- A) Power With Magnets
- B) Pulse Width Modulation
- C) Pin Wire Module

**(Correct: B -- +20 XP!)**

**Question 2:** What is the range of `analogWrite()`?
- A) 0 to 1023
- B) HIGH or LOW
- C) 0 to 255

**(Correct: C -- +20 XP!)**

**Question 3:** If you set `analogWrite(pin, 127)`, what average voltage does the Wand show?
- A) About 0V
- B) About 2.5V
- C) About 5V

**(Correct: B -- +20 XP!)**

---

## Lesson 30 Complete!

```
  =============================================

     PWM WIZARD BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand PWM and duty cycle
     [check] Use analogWrite() for brightness control
     [check] Build a smooth LED fade
     [check] Control brightness with a potentiometer
     [check] Measured PWM average voltage with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- PWM trick concept | 10 |
| Identify PWM pins | 10 |
| Rewire to PWM pin | 10 |
| Fade code and for loop | 30 |
| Potentiometer dimmer | 20 |
| Wand Check (5 PWM levels) | 50 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 31**, you will learn about **for loops** and **arrays** -- powerful programming tools that let you control LOTS of LEDs with just a few lines of code. You will build a **Knight Rider** LED chaser with 6 LEDs that scan back and forth. Get six LEDs ready!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LED does not fade, just stays on or off | Make sure the LED is on a PWM pin (3, 5, 6, 9, 10, or 11), not pin 7 |
| Fade is jerky, not smooth | Try reducing the delay in the for loop to 5 or even 3 |
| Potentiometer dimmer does not work | Check that the pot is wired to A0 and the LED is on a PWM pin |
| Wand shows jumping numbers | This is normal with fast PWM -- try reading slowly and let the Wand settle |
| analogWrite value seems wrong | Remember: analogRead returns 0-1023, but analogWrite needs 0-255; divide by 4 to convert |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 29: Analog Inputs -- Reading the In-Between](lesson-29-analog-inputs.md) | [Lesson 31: For Loops and Arrays -- Control an LED Army →](lesson-31-for-loops-and-arrays.md) |
