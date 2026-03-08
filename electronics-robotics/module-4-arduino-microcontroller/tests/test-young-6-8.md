# Module 4: Arduino Microcontroller
## Test for Ages 6–8 (Young)

**Your Name:** __________________ **Date:** ____________

**Total Time:** ~20 minutes | **Total XP Available:** 60 XP

---

## Scoring Guide
- Multiple Choice (Section 1): 1 point each = 5 XP each
- True/False (Section 2): 1 point each = 5 XP each
- Fill in the Blank (Section 3): 1 point each = 5 XP each
- Bonus: Code Matching (Section 4): 2 points = 10 XP
- **Base Score:** 50 XP | **Bonus:** 10 XP | **Total:** 60 XP max

---

## Section 1: Multiple Choice (5 questions)

**1. An Arduino is a:**
- A) Type of sandwich
- B) Tiny computer that follows your code instructions
- C) Component that stores electricity
- D) Motor that spins

**2. The `setup()` function runs:**
- A) Once when the Arduino powers on
- B) Every time you press a button
- C) Forever and ever
- D) Only in the daytime

**3. The `loop()` function runs:**
- A) Only one time
- B) Exactly 10 times
- C) Over and over forever
- D) Never, it is just decoration

**4. What does `delay(1000)` do?**
- A) Makes the LED turn off
- B) Makes the Arduino stop working
- C) Waits for 1 second (1000 milliseconds)
- D) Waits for 1 minute

**5. Serial Monitor is used to:**
- A) Watch the mail
- B) See messages the Arduino is "talking" to your computer
- C) Turn the Arduino on
- D) Count how many times the loop runs

---

## Section 2: True or False (3 questions)

**6. TRUE / FALSE: Arduino can read button presses using `digitalRead()`.**

**7. TRUE / FALSE: Arduino pins produce 12 volts of power.**

**8. TRUE / FALSE: `digitalWrite(LED_PIN, HIGH)` turns a LED on.**

---

## Section 3: Fill in the Blank (3 questions)

**Word Bank:** sketch | HIGH | LOW | setup | loop

**9. An Arduino program is called a _________________.

**10. When a pin is _________________, it sends 5V and powers an LED.

**11. The _________________ function runs your code over and over.

---

## Section 4: Bonus — Code Matching (2 points = 10 XP)

**12. Match each code line to what it does:**

```cpp
int ledPin = 13;
pinMode(ledPin, OUTPUT);
digitalWrite(ledPin, HIGH);
delay(1000);
digitalWrite(ledPin, LOW);
delay(1000);
```

| Code | What It Does |
|------|--------------|
| `int ledPin = 13;` | A) Wait 1 second (1000 ms) |
| `pinMode(ledPin, OUTPUT);` | B) Turn LED on (send 5V) |
| `digitalWrite(ledPin, HIGH);` | C) Create a variable for pin 13 |
| `delay(1000);` | D) Tell Arduino pin 13 is an output |
| `digitalWrite(ledPin, LOW);` | E) Turn LED off (send 0V) |

**Answers:**
- `int ledPin = 13;` → ___
- `pinMode(ledPin, OUTPUT);` → ___
- `digitalWrite(ledPin, HIGH);` → ___
- `delay(1000);` → ___
- `digitalWrite(ledPin, LOW);` → ___

---

## Extra Fun Question (not graded)

**What do you think would happen if you changed the `delay(1000)` to `delay(100)`?**

_Your answer: ________________________________________________________________________

_________________________________________________________________________________

---

**Teacher: Circle the final score → [ ] 50 XP | [ ] 55 XP | [ ] 60 XP**
