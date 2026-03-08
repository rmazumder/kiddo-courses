# Lesson 33: LCD Display (16x2) -- Give Your Arduino a Screen

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, your Arduino has been talking to you through the Serial Monitor on your computer. But what if the Arduino is not plugged into a computer? It needs its OWN screen! Today you will connect a **16x2 LCD display** -- a tiny screen that can show 2 rows of 16 characters each. By the end, your Arduino will display messages, show sensor readings, and even run a countdown timer. This is how real gadgets display information!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what an LCD is and how the I2C adapter simplifies wiring
- Wire a 16x2 LCD to the Arduino using I2C (just 4 wires!)
- Install and use the LiquidCrystal_I2C library
- Display text, numbers, and variables on the LCD
- Build a live countdown timer on the display

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| 16x2 LCD display with I2C backpack | 1 |
| Jumper wires (female-to-male) | 4 |
| 10k-ohm potentiometer (optional, for non-I2C) | 1 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- Screens Are Everywhere (3 min)

> "Look around you. How many screens can you see? TV, phone, tablet, microwave clock, car dashboard... Screens are EVERYWHERE in electronics. Today your Arduino gets one too!"

**LCD stands for Liquid Crystal Display.** These are the simplest screens:
- **16x2** means 16 characters wide, 2 rows tall
- That is 32 characters total -- enough for short messages, numbers, and readings
- They use very little power and are easy to read

> "It is not a fancy touchscreen, but it is powerful enough to show temperature, time, scores, menus, and more!"

**Award: +10 XP for understanding what an LCD is!**

---

![lesson-33-i2c-before-after](images/lesson-33-i2c-before-after.png)

### Step 2: The I2C Shortcut (5 min)

**The Problem:**

> "A raw LCD needs 12+ wires to connect to Arduino. That is a LOT of wiring and uses up many pins."

**The Solution -- I2C Adapter:**

> "The I2C backpack is a tiny board soldered to the back of the LCD. It converts those 12+ connections into just 4 wires. I2C is a communication protocol -- a language that lets devices talk over just 2 data wires."

**The 4 Wires:**

| LCD I2C Pin | Arduino Pin | What It Does |
|-------------|-------------|-------------|
| VCC | 5V | Power |
| GND | GND | Ground |
| SDA | A4 | Data line |
| SCL | A5 | Clock line |

> "SDA carries the data. SCL is the clock that keeps everything synchronized. Together they let the Arduino send instructions to the LCD."

**Award: +10 XP for understanding I2C!**

---

![lesson-33-lcd-wiring](images/lesson-33-lcd-wiring.png)

### Step 3: Wire the LCD (5 min)

**Wiring Diagram:**

```
  Arduino Uno                    LCD (I2C backpack)
  +---------+                    +----------+
  | 5V      |----[wire]-------->| VCC      |
  | GND     |----[wire]-------->| GND      |
  | A4 (SDA)|----[wire]-------->| SDA      |
  | A5 (SCL)|----[wire]-------->| SCL      |
  +---------+                    +----------+

  Just 4 wires! That is the beauty of I2C.
```

**Steps:**

1. Connect **LCD VCC** to **Arduino 5V**
2. Connect **LCD GND** to **Arduino GND**
3. Connect **LCD SDA** to **Arduino A4**
4. Connect **LCD SCL** to **Arduino A5**

> "That is it! Four wires. Compare that to 12+ wires without the I2C backpack. This is why engineers love I2C."

**Award: +20 XP for wiring the LCD!**

---

![lesson-33-lcd-cursor-positions](images/lesson-33-lcd-cursor-positions.png)

### Step 4: Install the Library (5 min)

The Arduino IDE needs a special **library** to talk to the I2C LCD.

> "A library is like a recipe book for the Arduino. Instead of writing hundreds of lines of code to control the LCD, someone already wrote it and packaged it as a library. We just install it and use it!"

**Installation Steps:**

1. In the Arduino IDE, go to **Sketch > Include Library > Manage Libraries**
2. In the search box, type **LiquidCrystal I2C**
3. Find **LiquidCrystal I2C** by Frank de Brabander (or similar)
4. Click **Install**
5. Close the Library Manager

**Award: +10 XP for installing the library!**

---

### Step 5: Hello World on the LCD (8 min)

**The Code:**

```cpp
// Lesson 33: LCD Hello World

#include <LiquidCrystal_I2C.h>

// Create LCD object: address 0x27, 16 columns, 2 rows
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();         // Start up the LCD
  lcd.backlight();    // Turn on the backlight

  lcd.setCursor(0, 0);         // Column 0, Row 0 (top left)
  lcd.print("Hello World!");

  lcd.setCursor(0, 1);         // Column 0, Row 1 (bottom left)
  lcd.print("Arduino Rocks!");
}

void loop() {
  // Nothing here -- message stays on screen
}
```

**Upload and look at the LCD!**

```
+------------------+
| Hello World!     |  <-- Row 0
| Arduino Rocks!   |  <-- Row 1
+------------------+
```

> "You just gave your Arduino its own screen! setCursor(column, row) tells the LCD WHERE to start writing. (0,0) is the top-left corner."

**If the screen is blank but backlit:** Try address `0x3F` instead of `0x27`. Some LCDs use a different address.

**Award: +20 XP for displaying Hello World on the LCD!**

---

### Step 6: Display Dynamic Data (8 min)

**Show a Counter:**

```cpp
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

int counter = 0;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Counter:");
}

void loop() {
  counter = counter + 1;

  lcd.setCursor(0, 1);     // Move to row 1
  lcd.print("                ");  // Clear the row (16 spaces)
  lcd.setCursor(0, 1);
  lcd.print(counter);

  delay(1000);  // Count once per second
}
```

**Show Potentiometer Reading:**

```cpp
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Pot Reader:");
}

void loop() {
  int potValue = analogRead(A0);
  float voltage = potValue * (5.0 / 1023.0);

  lcd.setCursor(0, 1);
  lcd.print("                ");  // Clear row
  lcd.setCursor(0, 1);
  lcd.print("V=");
  lcd.print(voltage, 2);
  lcd.print("  R=");
  lcd.print(potValue);

  delay(200);
}
```

> "Now the LCD shows live sensor data! Twist the potentiometer and watch the voltage change on the screen in real time. No computer needed!"

**Award: +30 XP for displaying live data on the LCD!**

---

### Step 7: Countdown Timer Challenge (5 min)

```cpp
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();

  for (int i = 10; i >= 0; i--) {
    lcd.clear();             // Clear entire screen
    lcd.setCursor(3, 0);
    lcd.print("COUNTDOWN!");
    lcd.setCursor(7, 1);
    lcd.print(i);
    delay(1000);
  }

  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("** LIFTOFF! **");
  lcd.setCursor(3, 1);
  lcd.print("We have GO!");
}

void loop() {
  // Stays on the LIFTOFF message
}
```

> "10... 9... 8... 7... 6... 5... 4... 3... 2... 1... LIFTOFF! You just built a real countdown display!"

**Award: +20 XP for the countdown timer!**

---

### Step 8: Wand Check -- LCD Power Verification (3 min)

> "Let us verify that the LCD is getting proper power from the Arduino."

1. Set the Wand to **DC Voltage**
2. Measure between **LCD VCC** and **LCD GND** -- should read ~5V
3. If you want to check I2C lines: SDA and SCL should read close to 5V when idle (pulled high)

**Award: +20 XP for verifying LCD power!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does "16x2" mean for an LCD?
- A) 16 pixels by 2 pixels
- B) 16 characters wide, 2 rows tall
- C) 16 volts, 2 amps

**(Correct: B -- +20 XP!)**

**Question 2:** How many wires does the I2C LCD need?
- A) 12
- B) 4
- C) 8

**(Correct: B -- +20 XP!)**

**Question 3:** What does `lcd.setCursor(5, 1)` do?
- A) Sets the brightness to 5
- B) Moves the cursor to column 5, row 1 (second row)
- C) Prints the number 51

**(Correct: B -- +20 XP!)**

---

## Lesson 33 Complete!

```
  =============================================

     DISPLAY COMMANDER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire an I2C LCD to Arduino
     [check] Install and use a library
     [check] Display text with lcd.print()
     [check] Show live sensor data on screen
     [check] Build a countdown timer display

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- LCD concepts | 10 |
| I2C understanding | 10 |
| LCD wiring | 20 |
| Library installation | 10 |
| Hello World display | 20 |
| Dynamic data display | 30 |
| Countdown timer | 20 |
| Wand Check | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 34** -- the Module 4 Grand Finale -- you will combine EVERYTHING you have learned to build a **Digital Piano with Display!** Buttons play musical notes, the LCD shows the note name, and LEDs light up as you play. It is the ultimate Arduino project for this module. Get all your components ready!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LCD screen is blank (no backlight) | Check VCC and GND connections; make sure the I2C backpack is soldered correctly |
| LCD has backlight but no text | Try changing the address from 0x27 to 0x3F in the code |
| Text is garbled or wrong characters | Check SDA (A4) and SCL (A5) connections; make sure they are not swapped |
| Library not found | Re-open Library Manager and search for "LiquidCrystal I2C"; make sure it installed |
| Only one row displays text | Make sure you use setCursor(0, 1) for the second row (row counting starts at 0) |
| Text does not clear properly | Use lcd.clear() to clear the whole screen, or print spaces over old text |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 32: Piezo Buzzer and Tones -- Give Your Arduino a Musical Voice](lesson-32-piezo-buzzer-and-tones.md) | [Lesson 34: Module 4 Project -- Digital Piano + Display →](lesson-34-project-digital-piano.md) |
