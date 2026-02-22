# Lesson 27: Variables and the Serial Monitor -- Give Your Arduino a Voice

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, so far your Arduino has been blinking silently. Would it not be cool if it could TALK to you? Today you are going to discover the **Serial Monitor** -- a secret window on your computer where the Arduino can send messages. You will also learn about **variables** -- little labeled boxes in the Arduino's memory that store numbers and text. By the end, your Arduino will be counting, chatting, and reporting data like a pro!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Create and use variables to store numbers
- Open and read the Serial Monitor
- Use `Serial.begin()` and `Serial.println()` to send messages from Arduino to your computer
- Print changing values (like a counter) to the Serial Monitor
- Understand the difference between `int`, `float`, and `String` variable types

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| Breadboard | 1 |
| LED (any color) | 1 |
| 330-ohm resistor | 1 |
| Jumper wires | 3 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Silent Robot Problem (3 min)

> "Imagine you have a robot helper, but it cannot talk. You ask it to do something, and it does it... but you have no idea if it worked, if it failed, or what it is thinking. Frustrating, right?"

> "Right now, your Arduino is like that silent robot. It blinks, but it cannot tell you WHY it is blinking, or what values it is working with. Today we give it a voice!"

**Award: +10 XP for understanding why communication matters!**

---

### Step 2: What Are Variables? (8 min)

**A variable is a labeled box that holds a value.**

> "Imagine you have a box labeled 'My Age.' Inside the box is the number 8. If your birthday comes along, you open the box, take out 8, and put in 9. The label stays the same, but the number inside changes."

**Creating Variables in Arduino:**

```cpp
int blinkSpeed = 500;       // A whole number -- 500 milliseconds
int counter = 0;             // Starts at zero
float voltage = 3.14;        // A decimal number
String myName = "Arduino";   // Text (words)
```

**Variable Types:**

| Type | What It Holds | Example |
|------|-------------|---------|
| `int` | Whole numbers | `int age = 10;` |
| `float` | Decimal numbers | `float temp = 23.5;` |
| `String` | Text | `String name = "Alex";` |
| `bool` | True or false | `bool ledOn = true;` |

> "You MUST tell Arduino what type of box you want. An int box only holds whole numbers. A float box can hold decimals. A String box holds words."

**Award: +20 XP for learning variable types!**

---

### Step 3: The Serial Monitor -- Arduino's Voice (8 min)

The **Serial Monitor** is a window in the Arduino IDE where the Arduino can print messages to your computer screen.

**How It Works:**

1. In your code, add `Serial.begin(9600)` in `setup()` -- this starts the communication at 9600 speed (called **baud rate**)
2. Use `Serial.println("Hello!")` to print a message
3. After uploading, click the **magnifying glass icon** in the top-right corner of the IDE to open the Serial Monitor

**Your First Talking Sketch:**

```cpp
void setup() {
  Serial.begin(9600);             // Start talking at 9600 baud
  Serial.println("Hello, World!");
  Serial.println("I am Arduino!");
  Serial.println("I am alive!");
}

void loop() {
  // Nothing here yet
}
```

**Upload it, then open the Serial Monitor.**

> "Look at that! Your Arduino just said hello! This is how engineers debug their code -- they make the Arduino print messages so they can see what is happening inside."

**Award: +20 XP for getting your first Serial Monitor message!**

---

### Step 4: Variables + Serial Monitor Together (10 min)

Now combine variables with printing. Type this code:

```cpp
int blinkSpeed = 500;  // How fast the LED blinks (milliseconds)
int blinkCount = 0;    // How many times the LED has blinked
int ledPin = 7;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Blink Counter Started! ===");
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(blinkSpeed);
  digitalWrite(ledPin, LOW);
  delay(blinkSpeed);

  blinkCount = blinkCount + 1;  // Add 1 to the counter

  Serial.print("Blink #");
  Serial.print(blinkCount);
  Serial.print(" | Speed: ");
  Serial.print(blinkSpeed);
  Serial.println(" ms");
}
```

**What You Will See in the Serial Monitor:**

```
=== Blink Counter Started! ===
Blink #1 | Speed: 500 ms
Blink #2 | Speed: 500 ms
Blink #3 | Speed: 500 ms
...
```

> "Your Arduino is counting its own blinks! The variable blinkCount goes up by 1 every time the LED blinks. And it tells you about it through the Serial Monitor."

**Award: +30 XP for building a blink counter!**

---

### Step 5: Change Variables -- Change Behavior (5 min)

**Challenge 1:** Change `blinkSpeed` to `100` at the top of the code. Upload. Watch the LED blink super fast AND see the counter race in the Serial Monitor.

**Challenge 2:** Make the blink speed change over time:

```cpp
void loop() {
  digitalWrite(ledPin, HIGH);
  delay(blinkSpeed);
  digitalWrite(ledPin, LOW);
  delay(blinkSpeed);

  blinkCount = blinkCount + 1;
  blinkSpeed = blinkSpeed + 50;  // Gets slower each time!

  Serial.print("Blink #");
  Serial.print(blinkCount);
  Serial.print(" | Speed: ");
  Serial.print(blinkSpeed);
  Serial.println(" ms");
}
```

> "Each blink, the delay gets 50 milliseconds longer. The LED starts fast and gradually slows down. You changed a variable inside the loop and the Arduino's behavior changed!"

**Award: +20 XP for making the blink speed change dynamically!**

---

### Step 6: Wand Check -- Verify With Your Own Eyes and Hands (5 min)

> "The Serial Monitor says the LED is blinking. Your eyes can see it blinking. But the Wand gives you the EXACT voltage. Let us triple-check!"

1. Set the Wand to **DC Voltage**
2. Black probe on **GND**, red probe on **pin 7**
3. Watch the voltage jump between **~5V** (HIGH) and **~0V** (LOW) as the LED blinks

**Fun Observation:**

> "When the blink is slow (like 1000ms), you can clearly see the Wand jump between 5V and 0V. When the blink is super fast (like 50ms), the Wand might show a number IN BETWEEN -- like 2.5V. That is because the Wand is averaging the fast switching. Remember this -- it will be important in Lesson 30 about PWM!"

**Award: +20 XP for using the Wand to verify blink voltages!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What is a variable?
- A) A type of wire
- B) A labeled box in the Arduino's memory that stores a value
- C) A command that turns off the Arduino

**(Correct: B -- +20 XP!)**

**Question 2:** What does `Serial.println("Hello")` do?
- A) Prints "Hello" on the Serial Monitor
- B) Turns on pin 13
- C) Deletes the program

**(Correct: A -- +20 XP!)**

**Question 3:** What type of variable would you use to store the number 3.14?
- A) int
- B) String
- C) float

**(Correct: C -- +20 XP!)**

---

## Lesson 27 Complete!

```
  =============================================

     VARIABLE WIZARD BADGE UNLOCKED!

     Skills unlocked:
     [check] Create and use variables
     [check] Open and read the Serial Monitor
     [check] Print text and numbers to the Monitor
     [check] Build a blink counter
     [check] Change behavior by changing variables

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook discussion | 10 |
| Variable types lesson | 20 |
| First Serial Monitor message | 20 |
| Blink counter sketch | 30 |
| Dynamic blink speed challenge | 20 |
| Wand Check | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 28**, you will add a **button** to your circuit and learn how to READ inputs! Your Arduino will not just send signals out -- it will listen to the real world. Press a button, and the LED responds. This is where things get really interactive!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Serial Monitor shows garbage characters | Make sure Serial.begin(9600) matches the baud rate dropdown in the Serial Monitor (bottom right) |
| Serial Monitor is blank | Did you click the magnifying glass icon? Is the code uploaded? Is the USB plugged in? |
| Counter does not increase | Make sure `blinkCount = blinkCount + 1;` is inside the `loop()` function |
| LED does not blink but Serial Monitor works | Check LED wiring -- is the LED connected to the correct pin with a resistor? |
| Numbers look wrong in Serial Monitor | Check that you are using `int` for whole numbers and `float` for decimals |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 26: Your First Sketch -- Blink an External LED](lesson-26-your-first-sketch-blink.md) | [Lesson 28: Reading Digital Inputs -- Buttons →](lesson-28-reading-digital-inputs-buttons.md) |
