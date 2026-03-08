# Module 6: Robotics Projects
## Test for Ages 9–12 (Older)

**Your Name:** __________________ **Date:** ____________

**Total Time:** ~35 minutes | **Total XP Available:** 200 XP

---

## Scoring Guide
- Multiple Choice (Section 1): 2 points each = 12 XP each
- True/False (Section 2): 2 points each = 8 XP each
- Short Answer (Section 3): 3 points each = 15 XP each
- Code/Analysis (Section 4): 5 points each = 25 XP each
- Application Scenario (Section 5): 4 points each = 20 XP each
- Bonus Challenge: 6 points = 20 XP
- **Base Score:** 180 XP | **Bonus:** 20 XP | **Total:** 200 XP max

---

## Section 1: Multiple Choice (6 questions)

**1. Differential drive steering works by:**
- A) A mechanical differential splits power equally to both wheels
- B) Changing speed of left and right motors independently
- C) Servo motors steering the front wheels
- D) An external remote controlling each wheel

**2. Why is a common ground required across separate power supplies (Arduino battery + motor battery)?**
- A) It is not required; it is just good practice
- B) Without common ground, voltage signals are undefined relative to motor driver
- C) Common ground provides extra power
- D) To prevent the batteries from exploding

**3. The L298N has a maximum voltage drop of ~2V. If you have a 6V battery and a motor, approximately how much voltage reaches the motor?**
- A) 8V
- B) 6V
- C) 4V
- D) 2V

**4. The TCRT5000 IR sensor reads HIGH when:**
- A) It sees a bright white surface
- B) It detects a black line (IR is absorbed, sensor reads no reflection)
- C) It detects a white surface (IR is reflected back)
- D) It measures temperature

**5. The HC-05 Bluetooth module's RX pin requires a voltage divider because:**
- A) 5V Arduino output would damage the 3.3V logic input
- B) Bluetooth requires special voltage levels
- C) It amplifies the signal
- D) It converts digital to analog

**6. "Degrees of freedom" in a robot arm refers to:**
- A) How fast the arm moves
- B) The number of joints/servo motors that can move independently
- C) How much the arm costs
- D) The range of motion in degrees (0–360)

---

## Section 2: True or False (4 questions)

**7. TRUE / FALSE: PWM duty cycle directly controls DC motor speed.**

**8. TRUE / FALSE: An obstacle-avoiding robot needs IR sensors on both sides to work effectively.**

**9. TRUE / FALSE: The HC-05 Bluetooth module communicates over I2C protocol.**

**10. TRUE / FALSE: A robot arm with 3 degrees of freedom can reach any point in 3D space (theoretically).**

---

## Section 3: Short Answer (15 XP each)

**11. Explain the purpose of the L298N motor driver. Why not just connect motors directly to the Arduino?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**12. Describe how a line-following robot detects and corrects its path when it drifts off the black line.**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**13. What does "common ground" mean and why is it critical in a robot with separate power supplies?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

---

## Section 4: Code/Analysis (25 XP each)

**14. A robot uses PWM to control motor speed. Given a motor driver output of 200/255 PWM:**

```
Percentage motor speed = (200 / 255) × 100 = _________%
```

**Explain what happens to motor speed if you increase this to 240/255:**

_Answer: ________________________________________________________________________

---

**15. Read this movement function. Does the robot go FORWARD or BACKWARD?**

```cpp
void moveForward() {
  digitalWrite(motor1_IN1, HIGH);
  digitalWrite(motor1_IN2, LOW);
  digitalWrite(motor2_IN1, HIGH);
  digitalWrite(motor2_IN2, LOW);
}
```

**Answer:** The robot goes: FORWARD / BACKWARD

**Why?** __________________________________________________________________

(Hint: Motor A and Motor B are set the same way. What does IN1=HIGH, IN2=LOW do?)

---

**16. A robot line-follower has two IR sensors. If LEFT sensor sees the line but RIGHT does not, what should the robot do?**

**Answer:** ______________________________________________________________________

**Explain your logic:**

_________________________________________________________________________

---

**17. The HC-05 Bluetooth receives the byte 0x46 (70 decimal). In robot control, this might mean "turn right." Without knowing the protocol, what is the character representation of 0x46?**

**Answer:** The character is: ___________

---

## Section 5: Application Scenarios (20 XP each)

**19. You are building an obstacle-avoiding robot. The ultrasonic sensor is mounted on a servo that sweeps side-to-side. Describe your scanning algorithm: how would the robot detect obstacles on the left, right, and center?**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

**20. A student's line-following robot oscillates wildly, zigzagging across the line instead of following smoothly. Suggest two possible causes and fixes.**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

_________________________________________________________________________________

---

## Section 6: Bonus Challenge (20 XP)

**21. Design a robot control system using HC-05 Bluetooth. Describe:**
- Command structure (e.g., what bytes mean forward, left, right, stop?)
- How you would parse incoming Bluetooth data in the main `loop()`
- What safety checks you would include

**Your design:**

_Answer: ________________________________________________________________________

_________________________________________________________________________________

**Pseudocode for Bluetooth command parsing:**

```cpp
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    // Your code here:




  }
}
```

---

**Teacher: Circle the final score → [ ] 180 XP | [ ] 190 XP | [ ] 200 XP**
