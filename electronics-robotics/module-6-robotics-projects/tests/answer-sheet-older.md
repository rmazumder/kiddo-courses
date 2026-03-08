# Module 6: Robotics Projects
## Answer Sheet — Ages 9–12 (Older)

**Teacher Guide:** This answer sheet provides correct answers, worked solutions, and scoring rubrics. Total: 200 XP max.

---

## Section 1: Multiple Choice Answers (12 XP each)

| Q | Answer | Concept | Why other options are wrong |
|---|--------|---------|------------------------------|
| 1 | **B) Changing speed of left and right motors independently** | Differential drive | A is mechanical (not software-controlled); C is Ackermann steering; D is irrelevant |
| 2 | **B) Without common ground, voltage signals are undefined** | Ground reference | A is false (common ground is required); C is false (ground supplies no power); D is nonsense |
| 3 | **C) 4V** | Voltage drop calculation: 6V − 2V = 4V | A is wrong; B ignores dropout; D is only the dropout |
| 4 | **C) It detects a white surface (IR is reflected back)** | Wait — standard logic is reversed! **CORRECTION: Should be B)** | Black absorbs IR, sensor sees LOW or no reflection. White reflects IR, sensor sees HIGH. (This question has ambiguous wording; accept both B and C with explanation.) |
| 5 | **A) 5V Arduino output would damage the 3.3V logic input** | Logic level translation | B is false; C is false (no amplification); D is false (conversion is incidental) |
| 6 | **B) The number of joints/servo motors that can move independently** | Degrees of freedom | A is speed; C is cost; D is angular range (related but different) |

---

## Section 2: True/False Answers (8 XP each)

| Q | Answer | Explanation |
|---|--------|-------------|
| 7 | **TRUE** | PWM duty cycle (% high time) directly controls average voltage to motor, thus speed. |
| 8 | **FALSE** | One IR sensor can work (usually centered), but two sensors improve turning accuracy. Not strictly required for basic obstacle avoidance. |
| 9 | **FALSE** | HC-05 uses UART (serial) communication, not I2C. I2C is TWI protocol for LCD, sensors, etc. |
| 10 | **TRUE** | 3 degrees of freedom (3 independently moving joints) allow reaching any point in 3D space (theoretically, ignoring reach limits). |

---

## Section 3: Short Answer (15 XP each)

**11. L298N motor driver purpose:**

✅ **Full Answer (15 XP):**
- "The L298N amplifies Arduino's small signal output to drive high-current motors."
- "Arduino pins produce ~5V at max ~40 mA. Motors need 3–6V at 100+ mA."
- "L298N takes IN1/IN2 logic signals and switches large current through motor."
- "Also allows direction control (IN1/IN2 states reverse motor direction)."
- **Analogy:** "Like a power steering system — small input signal controls big motor output."

⚠️ **Partial Answer (10 XP):**
- "Motor driver powers motors" — correct but lacks current explanation

---

**12. Line-following detection and correction:**

✅ **Full Answer (15 XP):**
- "Robots use one or two IR sensors below the chassis to detect the black line."
- "Black line absorbs IR (sensor reads LOW). White background reflects IR (sensor reads HIGH)."
- "If sensor drifts LEFT (sees white), slow LEFT motor → robot turns right back onto line."
- "If sensor drifts RIGHT (sees white), slow RIGHT motor → robot turns left back onto line."
- "Two sensors improve accuracy and allow faster correction."

⚠️ **Partial Answer (10 XP):**
- "Uses IR sensors" and "corrects by turning" but mechanism is unclear

---

**13. Common ground explanation:**

✅ **Full Answer (15 XP):**
- "Voltage is always measured between two points. Common ground = both circuits agree on 0V reference."
- "Without common ground, signals are floating/undefined. Example: Arduino outputs 5V, but motor driver doesn't know what 0V is → communication fails."
- "With common ground, both systems measure from the same 0V reference → signals are correct."
- **Example:** "Like two people on different buildings with different floor references. They need the same ground level (0 feet) to communicate heights."

⚠️ **Partial Answer (10 XP):**
- "They need to share ground" but lacks explanation of why

---

## Section 4: Code/Analysis (25 XP each)

**14. PWM speed calculation:**

✅ **Correct Answer (25 XP):**
```
Percentage = (200 / 255) × 100
Percentage = 78.43% ≈ 78%

Answer: 78% (accept 77–79%)

Effect of increase to 240/255:
(240 / 255) × 100 = 94.1% ≈ 94%

Explanation: "Increasing PWM duty cycle increases average voltage to motor, making it spin faster."
```

⚠️ **Partial Credit (15 XP):**
- Correct calculation but weak explanation of the effect

---

**15. Robot direction from motor control:**

✅ **Correct Answer (25 XP):**
- **Answer: FORWARD**
- **Why:** "Both Motor A and Motor B have IN1=HIGH and IN2=LOW. In an H-bridge, this configuration makes current flow in the same direction through both motors. When wheels spin the same direction at the same speed, the robot goes straight forward."

⚠️ **Partial Credit (15 XP):**
- Says "Forward" but explanation of H-bridge is weak or missing

---

**16. IR sensor left detection — robot action:**

✅ **Full Answer (25 XP):**
- **Action:** "Slow or stop the LEFT motor. Keep RIGHT motor running."
- **Effect:** "This makes the right side move faster, causing the robot to turn LEFT back onto the line."
- **Logic:** "If left sensor sees the line, robot is drifting RIGHT. Turn LEFT to correct."
- **Alternative:** "Or use servo-based centering: move sensor left/right to center line in view."

⚠️ **Partial Credit (15 XP):**
- Says "turn left" but logic/mechanism is unclear

---

**17. ASCII code 0x46 = 70 decimal:**

✅ **Correct Answer (25 XP):**
- **Answer: F** (uppercase letter F)
- **Explanation:** "70 in ASCII is 'F'. 0x46 hex = 4×16 + 6 = 70 decimal."
- **Robot context:** "Might mean 'forward' command in this protocol."

⚠️ **Partial Credit (15 XP):**
- Says "F" but no hexadecimal explanation

---

## Section 5: Application Scenarios (20 XP each)

**19. Obstacle-avoiding robot with servo-mounted ultrasonic sensor:**

✅ **Full Answer (20 XP):**
- **Scanning algorithm:**
  ```
  Sweep servo left (e.g., 45°)
  Read distance
  If distance < 20 cm, obstacle on left

  Sweep servo center (90°)
  Read distance
  If distance < 20 cm, obstacle ahead

  Sweep servo right (e.g., 135°)
  Read distance
  If distance < 20 cm, obstacle on right

  Compare distances; turn toward the direction with most space
  ```
- **Alternative:** "Use servo to continuously scan 45°–135° and pick largest gap."

⚠️ **Partial Credit (12 XP):**
- Mentions servo scanning but algorithm is vague

---

**20. Line-follower oscillation — causes & fixes:**

✅ **Full Answer (20 XP):**
- **Cause 1:** "IR sensors too close together or gain too high. Robot over-corrects."
  - **Fix:** "Increase sensor spacing or add smoothing/damping to reduce over-correction."
- **Cause 2:** "Motors response too fast or loop runs too slowly, causing lag."
  - **Fix:** "Add PWM ramp-up (gradual acceleration) or increase loop speed."
- **Cause 3:** "Line is too narrow or sensor calibration is off."
  - **Fix:** "Use wider line or recalibrate sensor thresholds."

⚠️ **Partial Credit (12 XP):**
- One cause + fix, but not two complete solutions

---

## Section 6: Bonus Challenge (20 XP)

**21. Bluetooth command system design:**

✅ **Full Answer (20 XP):**
- **Command structure (example):**
  ```
  'F' = forward
  'B' = backward
  'L' = turn left
  'R' = turn right
  'S' = stop
  '0'–'9' = speed 0–100%
  ```

- **Parsing pseudocode:**
  ```cpp
  void loop() {
    if (Serial.available() > 0) {
      char command = Serial.read();
      switch (command) {
        case 'F': moveForward(); break;
        case 'B': moveBackward(); break;
        case 'L': turnLeft(); break;
        case 'R': turnRight(); break;
        case 'S': stopRobot(); break;
        default: break;
      }
    }
  }
  ```

- **Safety checks:**
  - "Timeout: if no command received for 2 seconds, stop robot."
  - "Validate: only accept known commands; ignore garbage."
  - "Motor limits: prevent damage from invalid speed values (0–255 range)."

⚠️ **Partial Credit (12 XP):**
- Command structure and parsing correct, but missing safety checks
- Safety checks present but implementation unclear

---

## Common Student Mistakes & How to Address

| Mistake | Why | Correction |
|---------|-----|-----------|
| Thinks Arduino pins can power motors | Underestimates motor current draw | "Motors need 100+ mA. Arduino pins max out at 40 mA. Motor driver is required." |
| Confuses forward/backward motor direction | Doesn't understand H-bridge logic | "IN1=HIGH, IN2=LOW = one direction. Reverse them = opposite direction." |
| Forgets common ground | Doesn't understand voltage reference | "Voltage is always measured between two points. Both circuits must agree on 0V." |
| Oscillating line-follower blame | Attributes to hardware only | "Often a software/tuning issue. Try smoothing, damping, or sensor spacing." |
| Forgets safety checks in Bluetooth code | Assumes input is always valid | "Always validate commands and add timeout to prevent runaway robot." |

---

## Stretch It! (Advanced Discussion)

**For high performers, discuss:**
- "How would you use accelerometers to detect when the robot tips over?"
- "What is a PID controller and how would it improve line-following?"
- "How could you add mapping/SLAM (Simultaneous Localization and Mapping) to your robot?"
- "What is inverse kinematics and how does it apply to robot arms?"

---

## Scoring Summary

| Section | Points | XP |
|---------|--------|-----|
| Section 1 (6 MC) | 12 | 72 |
| Section 2 (4 T/F) | 8 | 32 |
| Section 3 (3 SA) | 9 | 45 |
| Section 4 (5 Code/Analysis) | 15 | 75 |
| Section 5 (2 App Scenario) | 8 | 40 |
| **Subtotal** | **52** | **264** |
| Section 6 (Bonus challenge) | 0–6 | 0–20 |
| **TOTAL BASE** | **52** | **180** |
| **TOTAL WITH BONUS** | **52–58** | **180–200 XP** |

**Expected Distribution:**
- **180 XP:** Correct on base sections, skips bonus or attempts partially
- **190 XP:** Minor errors on application scenarios; bonus mostly complete
- **200 XP:** Perfect score including comprehensive bonus design

