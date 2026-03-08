# Module 4: Arduino Microcontroller
## Answer Sheet — Ages 9–12 (Older)

**Teacher Guide:** This answer sheet provides correct answers, worked solutions, and scoring rubrics. Total: 200 XP max.

---

## Section 1: Multiple Choice Answers (12 XP each)

| Q | Answer | Concept | Why other options are wrong |
|---|--------|---------|------------------------------|
| 1 | **B) `digitalRead()` reads 0 or 5V; `analogRead()` reads 0–1023** | Digital vs Analog I/O | A is false (speed); C is false (both work on analog pins A0-A5); D ignores key difference |
| 2 | **C) Simulating analog output by rapidly turning a pin on/off** | PWM principle | A is I2C; B is false (PWM is simulated); D is irrelevant |
| 3 | **A) Hold a button pin at a known voltage (HIGH) when button is not pressed** | Pull-up resistor | B is false; C is for power; D is false (resistors don't reduce board size) |
| 4 | **B) Prints to the Serial Monitor on your computer** | Serial communication | A is LCD (different command); C is false (Arduino doesn't have permanent storage like this); D is audio (different hardware) |
| 5 | **C) `analogRead(pin);`** | Analog input | A and B are output commands; D is setup only |
| 6 | **B) Uses fewer wires, making wiring simpler and boards more compact** | I2C advantage | A is false; C is not inherent advantage; D is silly |

---

## Section 2: True/False Answers (8 XP each)

| Q | Answer | Explanation |
|---|--------|-------------|
| 7 | **FALSE** | `loop()` runs continuously and repeatedly. It only stops when power is removed. |
| 8 | **TRUE** | I2C (TWI) is a 2-wire protocol: SDA (data) and SCL (clock) lines, plus shared power/ground. |
| 9 | **TRUE** | `map()` converts a range: input 500 in range (0–1023) maps to output in range (0–180), suitable for servo angles. |
| 10 | **TRUE** | `delay()` halts all code execution for the specified milliseconds. During a 1-second delay, no other code runs. |

---

## Section 3: Short Answer (15 XP each)

**11. Difference between `setup()` and `loop()`:**

✅ **Full Answer (15 XP):**
- "`setup()` runs ONE time, immediately after power-on or reset."
- "`loop()` runs over and over, continuously, until the Arduino powers off."
- "`setup()` initializes pins, serial communication, and variables."
- "`loop()` contains the main program logic that repeats."
- **Example:** "setup() = getting ready to brush your teeth. loop() = the actual brushing (repeat forever)."

⚠️ **Partial Answer (10 XP):**
- "setup() runs first, loop() runs after" — correct but lacks repetition explanation

---

**12. Serial communication and why Arduino needs it:**

✅ **Full Answer (15 XP):**
- "Serial communication allows the Arduino to send text messages to your computer."
- "Used for debugging — you can print sensor values, variable states, and messages."
- "Happens through the USB cable connecting Arduino to computer."
- "Serial Monitor displays these messages so you can see what your code is doing."
- **Keyword:** Debugging, communication, visibility

⚠️ **Partial Answer (10 XP):**
- "Arduino talks to the computer" — correct but vague about purpose

---

**13. Blocking in Arduino code:**

✅ **Full Answer (15 XP):**
- "Blocking means the Arduino STOPS running code and waits."
- "`delay()` is a blocking function — it pauses the entire program."
- "Problem: while `delay()` is active, the Arduino cannot respond to button presses, sensor reads, or other interrupts."
- "Solution: use `millis()` instead to check elapsed time without blocking."
- **Example:** "If you use `delay(5000)`, you cannot read a button for those 5 seconds!"

⚠️ **Partial Answer (10 XP):**
- "delay() stops the program" — correct but no explanation of why this is bad

---

## Section 4: Code Analysis (25 XP each)

**14. Blink sketch — how fast?**

✅ **Correct Answer (25 XP):**
- **A) Blinks once per second (500 ms ON + 500 ms OFF)**
- **Explanation:** "HIGH for 500 ms + delay 500 ms = 500 ms on. Then LOW for 500 ms + delay 500 ms = 500 ms off. Total cycle = 1000 ms (1 second). LED is on 50% of the time, blink frequency = 1 Hz."

⚠️ **Partial Credit (15 XP):**
- Identifies the answer but lacks cycle explanation

---

**15. Calculate `map(512, 0, 1023, 0, 180)`:**

✅ **Correct Answer (25 XP):**
```
map() formula: output = (input − input_min) / (input_max − input_min) × (output_max − output_min) + output_min

output = (512 − 0) / (1023 − 0) × (180 − 0) + 0
output = 512 / 1023 × 180
output = 0.5 × 180
output = 90 degrees

Result: 90°
```
**Meaning:** Potentiometer at midpoint (512/1023) → servo at middle angle (90/180).

⚠️ **Partial Credit (15 XP):**
- Correct result but no work shown
- Arithmetic error (e.g., 85° or 95°) but method correct

---

**16. Button code bug identification:**

✅ **Full Answer (25 XP):**
- **Missing code:** `pinMode(2, INPUT);` and possibly `pinMode(13, OUTPUT);` in `setup()`
- **Explanation:** "Without `pinMode()`, the Arduino does not know pin 2 is an input. The system uses default settings which may not work correctly."
- **Alternative:** "Missing pull-up resistor externally, or the `INPUT_PULLUP` mode: `pinMode(2, INPUT_PULLUP);`"

⚠️ **Partial Credit (15 XP):**
- Identifies missing `pinMode()` but incomplete explanation

---

**17. Potentiometer-to-LED code explanation (line by line):**

✅ **Full Answer (25 XP):**
- `int potPin = A0;` → "Declare potentiometer on analog pin A0"
- `int ledPin = 13;` → "Declare LED on digital pin 13"
- `pinMode(ledPin, OUTPUT);` → "Set pin 13 as output"
- `analogRead(potPin);` → "Read potentiometer value (0–1023)"
- `map()` → "Convert 0–1023 range to 0–255 (PWM brightness range)"
- `analogWrite()` → "Write PWM signal to fade LED from dim to bright based on pot position"
- **Summary:** "This creates a potentiometer-controlled LED brightness."

⚠️ **Partial Credit (15 XP):**
- Explains most lines but misses the relationship between map() and analogWrite()

---

**18. I2C LCD initialization pseudocode:**

✅ **Acceptable Answers (25 XP):**
```cpp
// Actual C++ (if they remember):
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Address 0x27, 16x2 display

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.print("Hello, Arduino!");
}
```

OR **Pseudocode (also acceptable):**
```
setup():
  - Initialize I2C library
  - Create LCD object with I2C address
  - Turn on LCD backlight
  - Print text "Hello, Arduino!"
```

⚠️ **Partial Credit (15 XP):**
- Correct structure but syntax errors or incomplete library calls

---

## Section 5: Application Scenarios (20 XP each)

**19. LED fade in/out smoothly:**

✅ **Full Answer (20 XP):**
- "Use `analogWrite(pin, value)` with PWM."
- "Create a loop that increments brightness from 0 to 255, then decrements back to 0."
- "Use short delays (e.g., 10–50 ms) between increments so fading looks smooth."
- **Pseudocode:**
  ```
  for brightness = 0 to 255: analogWrite(9, brightness); delay(20);
  for brightness = 255 to 0: analogWrite(9, brightness); delay(20);
  repeat
  ```
- **Key insight:** "PWM simulates analog by turning the pin on/off very fast. Higher duty cycle = brighter."

⚠️ **Partial Credit (12 XP):**
- Mentions PWM and `analogWrite()` but missing loop logic

---

**20. Multiple sensors reading slowly:**

✅ **Full Answer (20 XP):**
- **Why:** "`analogRead()` is relatively slow (~100 microseconds per read). If reading 3 sensors in a loop, the total time per cycle delays updates."
- **Fix:** "Use interrupts or a timer (e.g., `millis()`) to read each sensor on a staggered schedule, not all at once."
- **Alternative:** "Use a multiplexer IC to select which sensor the Arduino reads."
- **Simple fix:** "Spread the reads across multiple `loop()` cycles or use non-blocking timing."

⚠️ **Partial Credit (12 XP):**
- Identifies the problem but solution is vague

---

## Section 6: Bonus Challenge (20 XP)

**21. Traffic light system pseudocode:**

✅ **Full Answer (20 XP):**
```cpp
void loop() {
  digitalWrite(5, HIGH);   // RED on
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  delay(3000);             // 3 seconds

  digitalWrite(5, LOW);    // YELLOW on
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  delay(1000);             // 1 second

  digitalWrite(5, LOW);    // GREEN on
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  delay(3000);             // 3 seconds
}
```

**Approach Explanation:**
- "Use `digitalWrite()` to turn LEDs on/off one at a time."
- "RED (pin 5) turns on, others off. Wait 3 seconds."
- "YELLOW (pin 6) turns on, others off. Wait 1 second."
- "GREEN (pin 7) turns on, others off. Wait 3 seconds."
- "Loop repeats, creating a continuous traffic light cycle."

⚠️ **Partial Credit (12 XP):**
- Logic correct but missing one or two delays
- Code structure is right but values are wrong

---

## Common Student Mistakes & How to Address

| Mistake | Why | Correction |
|---------|-----|-----------|
| Forgets `pinMode()` in `setup()` | Assumes pin mode is automatic | "Every pin MUST be told if it's INPUT or OUTPUT before using it" |
| Mixes `digitalWrite()` with `analogWrite()` | Confusion between digital and PWM | "`digitalWrite()` = on/off only. `analogWrite()` = PWM for fading" |
| Uses `delay()` everywhere | Blocking seems easy | "Blocking pauses EVERYTHING. Use `millis()` for real-world apps" |
| Reads analog repeatedly in one `loop()` | Doesn't optimize timing | "Consider staggering reads or using timers for efficiency" |
| Incorrect `map()` calculations | Math error | "Write out the formula step-by-step" |

---

## Stretch It! (Advanced Discussion)

**For high performers, discuss:**
- "How could you read 10 analog sensors without slowing down the `loop()`?"
- "Why does PWM only work on certain Arduino pins (3, 5, 6, 9, 10, 11)?"
- "How would you use interrupts to respond instantly to a button press?"
- "What is the difference between Serial and I2C communication?"

---

## Scoring Summary

| Section | Points | XP |
|---------|--------|-----|
| Section 1 (6 MC) | 12 | 72 |
| Section 2 (4 T/F) | 8 | 32 |
| Section 3 (3 SA) | 9 | 45 |
| Section 4 (5 Code Analysis) | 15 | 75 |
| Section 5 (2 App Scenario) | 8 | 40 |
| **Subtotal** | **52** | **264** |
| Section 6 (Bonus challenge) | 0–6 | 0–20 |
| **TOTAL BASE** | **52** | **180** |
| **TOTAL WITH BONUS** | **52–58** | **180–200 XP** |

**Expected Distribution:**
- **180 XP:** Correct on all base sections, bonus partial or skipped
- **190 XP:** Minor errors on application scenarios; bonus mostly correct
- **200 XP:** Perfect score on all sections including bonus

