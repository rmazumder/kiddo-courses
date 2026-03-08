# Module 5: Sensors and Actuators
## Test for Ages 9–12 (Older)

**Your Name:** __________________ **Date:** ____________

**Total Time:** ~35 minutes | **Total XP Available:** 200 XP

---

## Scoring Guide
- Multiple Choice (Section 1): 2 points each = 12 XP each
- True/False (Section 2): 2 points each = 8 XP each
- Short Answer (Section 3): 3 points each = 15 XP each
- Code/Calculations (Section 4): 5 points each = 25 XP each
- Application Scenario (Section 5): 4 points each = 20 XP each
- Bonus Challenge: 6 points = 20 XP
- **Base Score:** 180 XP | **Bonus:** 20 XP | **Total:** 200 XP max

---

## Section 1: Multiple Choice (6 questions)

**1. The ultrasonic distance formula is: distance = duration × 0.034 / 2. Why divide by 2?**
- A) It is a mistake in the formula
- B) Sound travels to the object AND back, so we divide by 2 to get one-way distance
- C) The Arduino calculates twice
- D) 0.034 already accounts for the round trip

**2. A voltage divider with a potentiometer converts:**
- A) AC to DC
- B) Digital signals to analog signals
- C) Continuous rotation to a voltage proportional to position
- D) 5V to 3.3V

**3. An L298N motor driver is necessary because:**
- A) Arduino pins do not have enough current to drive motors directly
- B) It speeds up the motor
- C) It replaces the need for a resistor
- D) It converts digital to PWM

**4. Why should you check `isnan()` when reading a DHT11 sensor?**
- A) The sensor always produces NaN values
- B) NaN = "Not a Number" means the sensor reading failed; checking prevents using bad data
- C) It speeds up the code
- D) It is optional; most people skip it

**5. A voltage divider for an LDR (light sensor) works by:**
- A) The LDR's resistance changes with light, changing the voltage output at the analog pin
- B) It stores the light energy as voltage
- C) It amplifies the light signal
- D) It converts light to heat

**6. Why does a servo motor only need 3 wires (power, ground, signal) while a DC motor needs direction control?**
- A) Servo motors are more advanced
- B) PWM signal on the servo pin controls angle directly (no direction logic needed)
- C) Servo motors cannot reverse direction
- D) DC motors are broken

---

## Section 2: True or False (4 questions)

**7. TRUE / FALSE: The PIR sensor needs a 30-second warm-up period before accurate readings.**

**8. TRUE / FALSE: An active buzzer requires a PWM signal to vary its loudness; a passive buzzer does not.**

**9. TRUE / FALSE: The HC-05 Bluetooth module requires a voltage divider on the RX pin because it operates at 3.3V logic while Arduino outputs 5V.**

**10. TRUE / FALSE: `map(analogValue, 0, 1023, 0, 180)` directly controls a servo motor's angle.**

---

## Section 3: Short Answer (15 XP each)

**11. Explain the difference between an active buzzer and a passive buzzer. When would you use each?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**12. Why must the Arduino and motor driver share a common ground (GND) even if they have separate power supplies?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**13. Describe how differential drive steering works. How does a robot turn left?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

---

## Section 4: Code/Calculations (25 XP each)

**14. Calculate the distance when an ultrasonic sensor returns a pulse duration of 294 microseconds:**

```
distance = duration × 0.034 / 2
distance = _________ cm
```

**Show your work:**

---

**15. You have an LDR in a voltage divider circuit. The equation is: V_out = 5V × R_LDR / (R_fixed + R_LDR)**

If R_fixed = 10kΩ and the LDR reads 1kΩ in bright light, what is V_out?

```
V_out = _________ V
```

**Show your work:**

---

**16. A DC motor is running at PWM speed 150 out of 255. What percentage is it running?**

```
Percentage = (150 / 255) × 100 = _________%
```

---

**17. Read this servo movement code. Predict: does the servo move from 0° to 180° or get stuck?**

```cpp
int angle = 0;

void setup() {
  pinMode(servoPin, OUTPUT);
}

void loop() {
  angle = angle + 1;
  if (angle > 180) angle = 0;
  // Missing: servo write command
  delay(50);
}
```

**Answer:** Does it work? Yes / No

**Why?** __________________________________________________________________

**What is missing?** ________________________________________________________

---

**18. The HC-05 Bluetooth module transmits a byte: 0x41 (65 decimal). What character is this?**

**Answer:** The character is: ___________

(Hint: Think of ASCII codes. 0x41 in hexadecimal.)

---

## Section 5: Application Scenarios (20 XP each)

**19. You are building an obstacle-avoiding robot. You have an ultrasonic sensor that reads distances. Describe your algorithm: what distance threshold would you use to detect an obstacle, and what would the robot do if it detects one?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

**20. A student complains: "My servo is jittery and doesn't move smoothly to 90°." Suggest two possible causes and how to fix each.**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

---

## Section 6: Bonus Challenge (20 XP)

**21. Design a "smart light" system that uses an LDR (light sensor) to auto-adjust room lighting. Describe:**
- How you would detect darkness (what analog threshold?)
- How you would dim/brighten an LED based on ambient light
- What code structure you would use (loop, functions, etc.)

**Your design:**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

**Pseudocode for the main `loop()`:**

```cpp
void loop() {
  // Your code here:




}
```

---

**Teacher: Circle the final score → [ ] 180 XP | [ ] 190 XP | [ ] 200 XP**
