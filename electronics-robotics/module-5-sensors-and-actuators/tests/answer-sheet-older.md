# Module 5: Sensors and Actuators
## Answer Sheet — Ages 9–12 (Older)

**Teacher Guide:** This answer sheet provides correct answers, worked solutions, and scoring rubrics. Total: 200 XP max.

---

## Section 1: Multiple Choice Answers (12 XP each)

| Q | Answer | Concept | Why other options are wrong |
|---|--------|---------|------------------------------|
| 1 | **B) Sound travels to the object AND back, so we divide by 2** | Distance calculation principle | A is false; C is nonsensical; D is false |
| 2 | **C) Continuous rotation to a voltage proportional to position** | Voltage divider output | A is wrong (AC/DC converter); B is wrong (analog already); D is wrong (no voltage conversion) |
| 3 | **A) Arduino pins do not have enough current to drive motors directly** | Current amplification | B is false (driver doesn't speed up); C is false (resistor unrelated); D is false (driver is current amplifier, not converter) |
| 4 | **B) NaN = "Not a Number" means the sensor reading failed** | Error handling | A is false (sensors don't always fail); C is false (checking is good practice); D is false (should always check) |
| 5 | **A) LDR's resistance changes with light, changing voltage output** | Voltage divider with variable resistor | B is false (energy storage); C is false (amplification is separate); D is false (no conversion) |
| 6 | **B) PWM signal on servo pin controls angle directly** | Servo control mechanism | A is vague; C is false (servos can reverse); D is false (DC motors work fine) |

---

## Section 2: True/False Answers (8 XP each)

| Q | Answer | Explanation |
|---|--------|-------------|
| 7 | **TRUE** | PIR sensors need warm-up time (~30 sec) to stabilize and provide accurate motion detection. |
| 8 | **FALSE** | Active buzzer produces sound at fixed frequency; you just turn it on/off. Passive buzzer NEEDS a PWM tone signal to produce sound at different frequencies. |
| 9 | **TRUE** | HC-05 operates at 3.3V logic (HIGH = 3.3V), but Arduino outputs 5V. Voltage divider (2×10kΩ resistors) reduces 5V to ~3.3V on RX pin to avoid damaging the module. |
| 10 | **TRUE** | The servo library uses `servo.write(angle)` which accepts the mapped value directly, so `map()` output goes straight to servo. |

---

## Section 3: Short Answer (15 XP each)

**11. Active vs Passive buzzers:**

✅ **Full Answer (15 XP):**
- **Active buzzer:** Has built-in oscillator. Just apply power (HIGH/LOW) to turn on/off. Fixed frequency. Simpler to use."
- **Passive buzzer:** Requires a tone/frequency signal (PWM). Can produce different pitches/melodies. More versatile.
- **Use active:** Simple alert/alarm (one beep).
- **Use passive:** Music, multiple tones, melody generation.
- **Example:** "Microwave uses active buzzer (one beep). Piano uses passive (many notes)."

⚠️ **Partial Answer (10 XP):**
- "Active is on/off, passive needs tone" — correct but lacks example or use case

---

**12. Common ground between separate power supplies:**

✅ **Full Answer (15 XP):**
- "Voltage is measured between two points. Without common ground, the Arduino cannot properly measure the motor driver's signals."
- "Common ground = reference point = both circuits must agree on 0V."
- "If Arduino ground ≠ motor driver ground, signal levels are undefined/incorrect."
- "Result: motor driver gets garbage data from Arduino pins = erratic behavior."
- **Analogy:** "Like two people speaking different languages — they need a common reference to communicate."

⚠️ **Partial Answer (10 XP):**
- "They need to share ground for reference" — correct but incomplete explanation

---

**13. Differential drive steering:**

✅ **Full Answer (15 XP):**
- "Two motors drive left and right wheels independently."
- "To turn left: slow/stop LEFT motor, speed up RIGHT motor."
- "Left wheel moves slower than right wheel = robot curves left."
- "To turn right: opposite — slow RIGHT, speed LEFT."
- "To go straight: both motors same speed."
- "To spin: one motor forward, one backward."

⚠️ **Partial Answer (10 XP):**
- "Two motors control steering" but unclear on left vs right logic

---

## Section 4: Code/Calculations (25 XP each)

**14. Ultrasonic distance from 294 µs duration:**

✅ **Correct Answer (25 XP):**
```
distance = duration × 0.034 / 2
distance = 294 × 0.034 / 2
distance = 9.996 / 2
distance = 4.998 ≈ 5 cm

Answer: 5 cm (or 5.0 cm)
```

⚠️ **Partial Credit (15 XP):**
- Correct formula but arithmetic error
- Forgets to divide by 2 (gets 9.996 cm)

---

**15. LDR voltage divider: R_fixed = 10kΩ, R_LDR = 1kΩ:**

✅ **Correct Answer (25 XP):**
```
V_out = 5V × R_LDR / (R_fixed + R_LDR)
V_out = 5V × 1kΩ / (10kΩ + 1kΩ)
V_out = 5V × 1kΩ / 11kΩ
V_out = 5V × 0.0909
V_out = 0.4545 V ≈ 0.45 V or 0.5 V

Answer: ~0.45 V (accept 0.4–0.5 V)
```

⚠️ **Partial Credit (15 XP):**
- Correct formula, math error (e.g., 1V)
- Correct principle, units missing

---

**16. PWM speed percentage:**

✅ **Correct Answer (25 XP):**
```
Percentage = (150 / 255) × 100
Percentage = 0.5882 × 100
Percentage = 58.82% ≈ 59%

Answer: 59% (accept 58–60%)
```

⚠️ **Partial Credit (15 XP):**
- Correct calculation but rounding error (e.g., 55% or 60%)

---

**17. Servo code — does it work?**

✅ **Full Answer (25 XP):**
- **Does it work?** **NO**
- **Why?** "The code increments `angle` and checks bounds, but never actually writes to the servo. The servo is not controlled."
- **What is missing?** "`servo.write(angle);` inside the loop after angle calculation."
- **Corrected:**
  ```cpp
  servo.write(angle);  // Add this line after angle increment
  ```

⚠️ **Partial Credit (15 XP):**
- Identifies "no servo write" but explanation is vague
- Says "code is wrong" but doesn't explain why

---

**18. ASCII code 0x41 = 65 decimal:**

✅ **Correct Answer (25 XP):**
- **Answer: A** (uppercase letter A)
- **Explanation:** "65 in ASCII is the character 'A'. 0x41 hexadecimal = 4×16 + 1 = 65 decimal."

⚠️ **Partial Credit (15 XP):**
- Says "A" but no explanation of hexadecimal conversion

---

## Section 5: Application Scenarios (20 XP each)

**19. Obstacle-avoiding robot algorithm:**

✅ **Full Answer (20 XP):**
- **Distance threshold:** "Detect obstacles when distance < 20 cm (or 15–25 cm range)."
- **Robot action:** "Stop moving forward, then turn left or right to avoid."
- **Algorithm:**
  ```
  if (distance < 20 cm) {
    Stop motors
    Turn right 90°
    Continue moving
  } else {
    Move forward
  }
  ```
- **Alternative:** "Back up, turn, resume."

⚠️ **Partial Credit (12 XP):**
- Mentions threshold but unclear on action
- Has action but no specific distance value

---

**20. Servo jitter and smooth movement causes & fixes:**

✅ **Full Answer (20 XP):**
- **Cause 1:** "Noisy power supply causing voltage fluctuation. Servo responds to electrical noise."
  - **Fix:** "Use a capacitor (100 µF) across servo power pins to smooth voltage."
- **Cause 2:** "Too-fast loop() sending changing angles rapidly. Servo oscillates."
  - **Fix:** "Add `delay(50)` or longer between `servo.write()` calls to give servo time to settle."
- **Cause 3:** "PWM signal noise from nearby components."
  - **Fix:** "Shield servo signal wire or move away from noise sources."

⚠️ **Partial Credit (12 XP):**
- One cause + fix, but not two complete solutions

---

## Section 6: Bonus Challenge (20 XP)

**21. Smart light system design:**

✅ **Full Answer (20 XP):**
- **Darkness threshold:** "If analog LDR value < 300 (arbitrary; depends on calibration), it is dark."
- **Dimming logic:** "Map LDR value to LED brightness: `analogWrite(LED_pin, map(ldrValue, 0, 1023, 0, 255));`"
- **Code structure:**
  ```cpp
  void loop() {
    int ldrValue = analogRead(A0);
    int brightness = map(ldrValue, 0, 1023, 0, 255);
    analogWrite(ledPin, brightness);
    delay(100);  // Update every 100 ms
  }
  ```
- **Explanation:** "LDR reads light level; brighter ambient = higher analog value = brighter LED output (inverse control if needed)."

⚠️ **Partial Credit (12 XP):**
- Correct threshold and logic but incomplete code
- Code correct but no threshold explanation

---

## Common Student Mistakes & How to Address

| Mistake | Why | Correction |
|---------|-----|-----------|
| Forgets to divide by 2 in distance formula | Thinks sound only goes one way | "Sound travels to object AND back. We only want distance to object, so divide by 2." |
| Confuses active/passive buzzer | No real-world experience | Show them: active buzzer (steady tone), passive buzzer (varying tones). |
| Wrong voltage divider calculation | Math error or unit confusion | "Write out the formula with all units, then substitute." |
| Thinks servo can spin 360° | Confuses standard servo with continuous rotation servo | "Standard servo = 0–180°. Continuous servo = full rotation." |
| Forgets common ground | Doesn't understand voltage reference | "Voltage is measured between two points. Both circuits must agree on 0V." |

---

## Stretch It! (Advanced Discussion)

**For high performers, discuss:**
- "How would you filter noisy analog readings to reduce servo jitter?"
- "What is hysteresis in sensor readings and how would you implement it?"
- "How could you use multiple sensors to triangulate an object's position?"
- "What is the difference between absolute and relative positioning?"

---

## Scoring Summary

| Section | Points | XP |
|---------|--------|-----|
| Section 1 (6 MC) | 12 | 72 |
| Section 2 (4 T/F) | 8 | 32 |
| Section 3 (3 SA) | 9 | 45 |
| Section 4 (5 Calc/Code) | 15 | 75 |
| Section 5 (2 App Scenario) | 8 | 40 |
| **Subtotal** | **52** | **264** |
| Section 6 (Bonus challenge) | 0–6 | 0–20 |
| **TOTAL BASE** | **52** | **180** |
| **TOTAL WITH BONUS** | **52–58** | **180–200 XP** |

**Expected Distribution:**
- **180 XP:** Correct on base sections, skips or partially attempts bonus
- **190 XP:** Minor errors on application scenarios; bonus attempted
- **200 XP:** Perfect score including complete bonus design

