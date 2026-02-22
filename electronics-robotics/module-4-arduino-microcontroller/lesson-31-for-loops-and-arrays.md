# Lesson 31: For Loops and Arrays -- Control an LED Army

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, controlling one LED is cool, but controlling SIX LEDs that dance back and forth? That is AWESOME. Today you will learn two of the most powerful programming tools: **for loops** (repeat code a set number of times) and **arrays** (store a whole list of values in one variable). By the end, you will build the famous **Knight Rider** LED chaser -- a light that scans back and forth across a row of LEDs, just like the car from the TV show!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Use a `for` loop to repeat code a specific number of times
- Create an array to store a list of pin numbers
- Wire 6 LEDs on a breadboard and control them all with code
- Build a Knight Rider scanning LED effect
- Modify loop speed and patterns

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| Breadboard | 1 |
| LEDs (any color, matching is nice) | 6 |
| 330-ohm resistors | 6 |
| Jumper wires | 8 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Copy-Paste Nightmare (3 min)

> "Imagine you want to blink 6 LEDs one after another. You could write this:"

```cpp
// The BAD way -- so much repeated code!
digitalWrite(3, HIGH); delay(100); digitalWrite(3, LOW);
digitalWrite(5, HIGH); delay(100); digitalWrite(5, LOW);
digitalWrite(6, HIGH); delay(100); digitalWrite(6, LOW);
digitalWrite(9, HIGH); delay(100); digitalWrite(9, LOW);
digitalWrite(10, HIGH); delay(100); digitalWrite(10, LOW);
digitalWrite(11, HIGH); delay(100); digitalWrite(11, LOW);
```

> "That is 18 lines just to scan 6 LEDs! And what if you wanted to change the delay? You would have to change it in 6 places. There MUST be a better way..."

> "There is. It is called a FOR LOOP."

**Award: +10 XP for seeing why loops are needed!**

---

### Step 2: What is a For Loop? (8 min)

**A for loop repeats code a set number of times.**

```cpp
for (int i = 0; i < 6; i++) {
  Serial.println(i);
}
```

This prints: 0, 1, 2, 3, 4, 5

**Breaking It Down:**

| Part | Meaning | Analogy |
|------|---------|---------|
| `int i = 0` | Start counting at 0 | "Start at the first step" |
| `i < 6` | Keep going while i is less than 6 | "Stop after 6 steps" |
| `i++` | Add 1 to i each time | "Move to the next step" |

> "It is like climbing stairs. Start at stair 0, climb one at a time, stop when you reach stair 5 (which is 6 stairs total)."

**Try This Code:**

```cpp
void setup() {
  Serial.begin(9600);

  Serial.println("Counting up:");
  for (int i = 1; i <= 10; i++) {
    Serial.print("Step ");
    Serial.println(i);
  }

  Serial.println("Counting down:");
  for (int i = 10; i >= 1; i--) {
    Serial.print("Step ");
    Serial.println(i);
  }
  Serial.println("LIFTOFF!");
}

void loop() {
  // Nothing here -- just the setup demo
}
```

**Award: +20 XP for understanding for loops!**

---

### Step 3: What is an Array? (5 min)

**An array is a list of values stored in one variable.**

> "Remember variables from Lesson 27? A variable is one labeled box. An array is a ROW of labeled boxes."

```cpp
// One variable holds ONE value:
int ledPin = 3;

// An array holds MANY values:
int leds[] = {3, 5, 6, 9, 10, 11};
```

**Accessing Array Items:**

```
leds[0] = 3    (first item -- arrays start at 0!)
leds[1] = 5
leds[2] = 6
leds[3] = 9
leds[4] = 10
leds[5] = 11
```

> "Arrays start counting at 0, not 1. The first item is leds[0], not leds[1]. This is a little weird at first, but all programming languages work this way."

**Award: +10 XP for understanding arrays!**

---

### Step 4: Build the 6-LED Circuit (10 min)

**Wiring Diagram:**

```
  Arduino Pins          Breadboard
  +-----------+
  | Pin 3  (~)|----[330 ohm]----LED 1----GND
  | Pin 5  (~)|----[330 ohm]----LED 2----GND
  | Pin 6  (~)|----[330 ohm]----LED 3----GND
  | Pin 9  (~)|----[330 ohm]----LED 4----GND
  | Pin 10 (~)|----[330 ohm]----LED 5----GND
  | Pin 11 (~)|----[330 ohm]----LED 6----GND
  | GND       |----[common GND rail on breadboard]
  +-----------+

  Breadboard Layout (top view):
  GND rail: ================================

  Row 5:  [330R]--LED1--GND    (pin 3)
  Row 10: [330R]--LED2--GND    (pin 5)
  Row 15: [330R]--LED3--GND    (pin 6)
  Row 20: [330R]--LED4--GND    (pin 9)
  Row 25: [330R]--LED5--GND    (pin 10)
  Row 30: [330R]--LED6--GND    (pin 11)
```

**Steps:**

1. Place 6 LEDs in a row on the breadboard (leave 5 rows between each)
2. Connect a 330-ohm resistor from each Arduino pin to the LED's long leg (+)
3. Connect all LED short legs (-) to the GND rail
4. Connect the GND rail to Arduino GND

> "Take your time with this one. Six LEDs means 12 component legs plus 7 jumper wires. Neat wiring makes debugging easier!"

**Award: +30 XP for wiring all 6 LEDs!**

---

### Step 5: Knight Rider Code (8 min)

**The Full Code:**

```cpp
// Lesson 31: Knight Rider LED Chaser

int leds[] = {3, 5, 6, 9, 10, 11};  // Array of 6 LED pins
int numLeds = 6;                      // How many LEDs
int delayTime = 100;                  // Speed of the scan

void setup() {
  // Use a for loop to set ALL pins as outputs
  for (int i = 0; i < numLeds; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.println("Knight Rider Ready!");
}

void loop() {
  // Scan LEFT to RIGHT
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(leds[i], HIGH);   // Turn this LED on
    delay(delayTime);
    digitalWrite(leds[i], LOW);    // Turn it off
  }

  // Scan RIGHT to LEFT
  for (int i = numLeds - 1; i >= 0; i--) {
    digitalWrite(leds[i], HIGH);
    delay(delayTime);
    digitalWrite(leds[i], LOW);
  }
}
```

**Upload and watch the magic!**

> "The light scans left, then right, then left again -- just like Knight Rider! And you did it with a for loop and an array. Without those tools, this code would be 4 times longer."

**Award: +30 XP for the Knight Rider effect!**

---

### Step 6: Challenges and Variations (5 min)

**Challenge 1 -- Speed Control:**
Change `delayTime` to `50` for super fast, or `300` for slow and dramatic.

**Challenge 2 -- All On, All Off:**

```cpp
void loop() {
  // Turn ALL on
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(leds[i], HIGH);
  }
  delay(500);

  // Turn ALL off
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(leds[i], LOW);
  }
  delay(500);
}
```

**Challenge 3 -- Stack Effect (LEDs light up one by one and stay on):**

```cpp
void loop() {
  // Light up one by one
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(leds[i], HIGH);
    delay(200);
  }
  delay(500);
  // Turn off one by one
  for (int i = numLeds - 1; i >= 0; i--) {
    digitalWrite(leds[i], LOW);
    delay(200);
  }
  delay(500);
}
```

**Award: +20 XP for completing at least one challenge!**

---

### Step 7: Wand Check -- Quick Pin Verification (3 min)

> "With 6 LEDs, it is easy to make a wiring mistake. Use the Wand to quickly verify that each pin outputs 5V when HIGH."

1. Set Wand to **DC Voltage**
2. Pause the scanning by uploading a simple "all on" sketch
3. Measure each pin to GND -- all should show ~5V

**Award: +20 XP for verifying all 6 pins!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does `leds[0]` refer to in the array `int leds[] = {3, 5, 6, 9, 10, 11}`?
- A) The number 0
- B) The number 3 (the first item in the array)
- C) The number 11 (the last item)

**(Correct: B -- +20 XP!)**

**Question 2:** How many times does this loop run? `for (int i = 0; i < 5; i++)`
- A) 4 times
- B) 5 times
- C) 6 times

**(Correct: B -- +20 XP!)**

**Question 3:** What does `i++` mean?
- A) i equals positive
- B) Add 1 to i
- C) i is very important

**(Correct: B -- +20 XP!)**

---

## Lesson 31 Complete!

```
  =============================================

     LOOP LEGEND BADGE UNLOCKED!

     Skills unlocked:
     [check] Write for loops
     [check] Create and use arrays
     [check] Wire 6 LEDs
     [check] Build the Knight Rider effect
     [check] Create custom LED patterns

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook discussion | 10 |
| For loop concept | 20 |
| Array concept | 10 |
| Wire 6 LEDs | 30 |
| Knight Rider code | 30 |
| Pattern challenges | 20 |
| Wand Check (6 pins) | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 32**, you are going to make some NOISE! You will connect a **piezo buzzer** and use the `tone()` function to play musical notes. By the end, you will have programmed your own melody. Time to give your Arduino a musical voice!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Some LEDs do not light up | Check wiring for each LED individually; make sure long leg goes to the resistor |
| LEDs light in wrong order | Check that the wire from each pin goes to the correct LED position |
| Code does not compile | Check for missing semicolons or curly braces; array syntax must have commas between values |
| Only some LEDs scan | Make sure all 6 pins are listed in the array AND that numLeds equals 6 |
| Knight Rider effect looks odd at the ends | The basic code pauses briefly at each end -- this is normal; you can adjust the pattern |
