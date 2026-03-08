# Module 4: Arduino Microcontroller
## Answer Sheet — Ages 6–8 (Young)

**Teacher Guide:** This answer sheet provides correct answers. Each correct answer = 5 XP, except the bonus matching = 10 XP. Total: 60 XP max.

---

## Section 1: Multiple Choice Answers

| Question | Correct Answer | Concept |
|----------|----------------|---------|
| 1 | **B) Tiny computer that follows your code instructions** | Arduino definition |
| 2 | **A) Once when the Arduino powers on** | `setup()` purpose |
| 3 | **C) Over and over forever** | `loop()` behavior |
| 4 | **C) Waits for 1 second (1000 milliseconds)** | `delay()` function |
| 5 | **B) See messages the Arduino is "talking" to your computer** | Serial Monitor purpose |

---

## Section 2: True/False Answers

| Question | Answer | Explanation |
|----------|--------|-------------|
| 6 | **TRUE** | `digitalRead()` reads 0 (LOW) or 1 (HIGH) from a pin |
| 7 | **FALSE** | Arduino pins output 0–5V (5V maximum for HIGH state). 12V would damage it. |
| 8 | **TRUE** | `digitalWrite(pin, HIGH)` sends 5V to the pin, powering an LED |

---

## Section 3: Fill in the Blank Answers

| Question | Correct Answer | Alternate Acceptable Answers |
|----------|----------------|------------------------------|
| 9 | **sketch** | program, code |
| 10 | **HIGH** | (exact — no alternatives) |
| 11 | **loop** | (exact — no alternatives) |

---

## Section 4: Bonus — Code Matching (10 XP)

✅ **Full Credit (10 XP) — All matches correct:**
- `int ledPin = 13;` → **C)** Create a variable for pin 13
- `pinMode(ledPin, OUTPUT);` → **D)** Tell Arduino pin 13 is an output
- `digitalWrite(ledPin, HIGH);` → **B)** Turn LED on (send 5V)
- `delay(1000);` → **A)** Wait 1 second (1000 ms)
- `digitalWrite(ledPin, LOW);` → **E)** Turn LED off (send 0V)

⚠️ **Partial Credit (5 XP):**
- 3–4 matches correct

❌ **No Credit (0 XP):**
- Fewer than 3 correct matches

---

## Extra Fun Question (Discussion)

**Expected answer:** "If you change `delay(1000)` to `delay(100)`, the LED blinks 10 times faster! Each on/off cycle is 200 ms (100 ms on + 100 ms off) instead of 1 second."

---

## Teacher Notes & Extensions

**If a student struggles with:**

- **`setup()` vs `loop()`:** Show them: "Imagine brushing your teeth. `setup()` is getting the toothbrush ready once. `loop()` is brushing — you do it over and over!"
- **Serial Monitor:** Have them run a simple `Serial.println("test");` sketch and show them the output window.
- **Delays:** "Every time you use `delay()`, the Arduino takes a nap for that long. It cannot do anything else."

**Fun discussion (not graded):**
- "What if you put `setup()` code inside `loop()`? What would happen?" (It would re-initialize every loop!)
- "Can you make an LED blink without using `delay()`?" (Yes! Using `millis()` — advanced topic.)

---

## Scoring Summary

| Section | Points | XP |
|---------|--------|-----|
| Section 1 (5 MC questions) | 5 | 25 |
| Section 2 (3 T/F questions) | 3 | 15 |
| Section 3 (3 Fill-in questions) | 3 | 15 |
| **Subtotal** | **11** | **55** |
| Section 4 (Bonus matching) | 0–2 | 0–10 |
| **TOTAL** | **11–13** | **55–65 XP** |

**Expected range:** Most students earning 50–55 XP for correct MC, T/F, and fill-in work. Bonus elevates strong performance to 60 XP.

