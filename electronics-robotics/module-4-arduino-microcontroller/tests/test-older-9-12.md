# Module 4: Arduino Microcontroller
## Test for Ages 9–12 (Older)

**Your Name:** __________________ **Date:** ____________

**Total Time:** ~35 minutes | **Total XP Available:** 200 XP

---

## Scoring Guide
- Multiple Choice (Section 1): 2 points each = 12 XP each
- True/False (Section 2): 2 points each = 8 XP each
- Short Answer (Section 3): 3 points each = 15 XP each
- Code Analysis (Section 4): 5 points each = 25 XP each
- Application Scenario (Section 5): 4 points each = 20 XP each
- Bonus Challenge: 6 points = 20 XP
- **Base Score:** 180 XP | **Bonus:** 20 XP | **Total:** 200 XP max

---

## Section 1: Multiple Choice (6 questions)

**1. The main difference between `digitalRead()` and `analogRead()` is:**
- A) `digitalRead()` is faster
- B) `digitalRead()` reads 0 or 5V; `analogRead()` reads 0–1023 (voltage divided into steps)
- C) `analogRead()` only works on certain pins
- D) They do the same thing; the names are different for fun

**2. PWM (Pulse Width Modulation) allows:**
- A) Faster communication between Arduino and computer
- B) Direct voltage output from 0–5V continuously
- C) Simulating analog output by rapidly turning a pin on/off
- D) More input pins on the Arduino

**3. A pull-up resistor is used to:**
- A) Hold a button pin at a known voltage (HIGH) when the button is not pressed
- B) Speed up the Arduino processor
- C) Power external LEDs
- D) Reduce the size of the Arduino board

**4. What does `Serial.println("Hello");` do?**
- A) Prints to the Arduino's LCD screen
- B) Prints to the Serial Monitor on your computer
- C) Saves text to the Arduino's memory
- D) Plays a sound through a speaker

**5. To read an analog voltage (like from a potentiometer), you would use:**
- A) `digitalWrite(pin, HIGH);`
- B) `digitalRead(pin);`
- C) `analogRead(pin);`
- D) `pinMode(pin, INPUT);`

**6. I2C protocol uses only 2 wires (SDA and SCL) for communication. Why is this useful compared to parallel connections?**
- A) It is faster
- B) It uses fewer wires, making wiring simpler and boards more compact
- C) It is more powerful
- D) No real advantage; just looks cool

---

## Section 2: True or False (4 questions)

**7. TRUE / FALSE: The Arduino runs the `loop()` function one time only, then stops.**

**8. TRUE / FALSE: A 16x2 LCD display connected via I2C requires only 2 signal wires (SDA and SCL) plus power and ground.**

**9. TRUE / FALSE: `map(500, 0, 1023, 0, 180)` converts an analog reading to a servo motor angle.**

**10. TRUE / FALSE: `delay(1000)` blocks the Arduino from doing anything else for 1 second.**

---

## Section 3: Short Answer (3 questions)

**11. Explain the difference between `setup()` and `loop()`. When does each run?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**12. What is serial communication and why does an Arduino need it?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**13. Describe what "blocking" means in Arduino code and why it can be a problem.**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

---

## Section 4: Code Analysis (5 questions, 25 XP each)

**14. Read this Blink sketch. If you upload it, how fast does the LED blink?**

```cpp
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
}
```

- A) Blinks once per second (500 ms ON + 500 ms OFF)
- B) Blinks 10 times per second
- C) Blinks once every 2 seconds
- D) Does not blink; the code is broken

**Explanation:** __________________________________________________________________

---

**15. Calculate the result of: `map(analogValue, 0, 1023, 0, 180)` when `analogValue = 512`**

```
Result: _________ degrees
```

**Show your work:**

---

**16. This code tries to read a button on pin 2, but students say it does not work. Identify the bug:**

```cpp
void setup() {
  // Missing code here?
}

void loop() {
  int buttonState = digitalRead(2);

  if (buttonState == HIGH) {
    digitalWrite(13, HIGH);  // Turn LED on
  } else {
    digitalWrite(13, LOW);   // Turn LED off
  }
}
```

**What is missing?** ___________________________________________________________________

**How would you fix it?** ________________________________________________________________

---

**17. What does this code do? Explain line by line.**

```cpp
int potPin = A0;
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int sensorValue = analogRead(potPin);
  int brightness = map(sensorValue, 0, 1023, 0, 255);
  analogWrite(ledPin, brightness);
}
```

**Explanation:** ____________________________________________________________________

_________________________________________________________________________________

---

**18. You have an I2C LCD that requires setup in `setup()`. Write a SHORT code snippet that would initialize and print "Hello, Arduino!" to the LCD. (You do NOT need to remember exact syntax — pseudocode is fine.)**

```cpp
void setup() {
  // Your code here:


}
```

---

## Section 5: Application Scenarios (20 XP each)

**19. You want to make an LED fade in and out smoothly (not just blink on/off). You have PWM available on pin 9. Describe your approach: what function would you use, what values would you change, and in what order?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

**20. A student tries to read 3 analog sensors at the same time using `analogRead()`, but the Serial Monitor shows only one sensor updates per loop. Why? How would you fix it to read all 3?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

---

## Section 6: Bonus Challenge (20 XP)

**21. Design a simple "traffic light" system. Your Arduino should:**
- Turn on RED (pin 5) for 3 seconds
- Turn on YELLOW (pin 6) for 1 second
- Turn on GREEN (pin 7) for 3 seconds
- Repeat forever

**Write pseudocode (or real Arduino code if you remember!) in the `loop()` function. Do NOT write `setup()`.**

```cpp
void loop() {
  // Your code here:




}
```

**Explain your approach:**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

---

**Teacher: Circle the final score → [ ] 180 XP | [ ] 190 XP | [ ] 200 XP**
