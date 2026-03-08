# Module 1: Electronic Components Basics
## Answer Sheet — Ages 9–12 (Older)

**Teacher Guide:** This answer sheet provides correct answers, worked solutions for calculations, and scoring rubrics. Total: 200 XP max.

---

## Section 1: Multiple Choice Answers (12 XP each)

| Q | Answer | Concept | Why other options are wrong |
|---|--------|---------|------------------------------|
| 1 | **B) Ohm's Law (V = I × R)** | Fundamental relationship | A is relativity; C is analogy only; D is electrochemistry |
| 2 | **C) It will burn out from too much current** | Over-current damage | A is wrong (no limiting resistor); B is backwards; D is false |
| 3 | **A) Electricity (electrons)** | Capacitor function | B is heat; C is acoustic; D is optical — capacitors store electrical charge |
| 4 | **B) DC only works with batteries; AC flows both directions** | AC vs DC distinction | A is wrong; C is misleading; D ignores fundamental difference |
| 5 | **C) Both A and B** | Transistor dual purpose | Transistors amplify AND switch |
| 6 | **B) 1,000 ohms (1 kΩ)** | Color code reading: Brown=1, Black=0, Red×100 | A is 100Ω; C is 10kΩ; D is arbitrary |

---

## Section 2: True/False Answers (8 XP each)

| Q | Answer | Explanation |
|---|--------|-------------|
| 7 | **TRUE** | Diodes are one-way gates for current. Anode (+) to cathode (−) only. |
| 8 | **TRUE** | Perfect analogy! Capacitor fills with charge; releases when needed. |
| 9 | **FALSE** | Potentiometer IS a variable resistor. You can adjust it by turning the knob. |
| 10 | **TRUE** | Series circuit means current must flow through all components. One break = circuit off. |

---

## Section 3: Short Answer (15 XP each)

**11. Why is a resistor needed in an LED circuit? What bad thing happens if you skip it?**

✅ **Full Answer (15 XP):**
- "A resistor limits current flow to safe levels (typically 15-20 mA for an LED)."
- "Without a resistor, the full battery voltage (e.g., 9V) pushes too much current through the LED."
- "Too much current causes the LED to overheat and burn out immediately."
- **Keyword:** Current limiting or Over-current protection

⚠️ **Partial Answer (10 XP):**
- "Resistor protects the LED" — but lacks explanation of mechanism

❌ **Wrong (0 XP):**
- "Resistor makes LED brighter" or "Resistor slows electricity" (too vague)

---

**12. Describe how an NPN transistor works. (Hint: think of it as a gate with a control signal.)**

✅ **Full Answer (15 XP):**
- "Base pin is the control input — small signal."
- "When current flows into the base, it opens the gate between collector and emitter."
- "Collector-to-emitter current is much larger than base current — amplification!"
- "Turn off base current = gate closes = no collector-emitter current."
- **Keyword:** Gate, amplification, control signal

⚠️ **Partial Answer (10 XP):**
- "It's like a switch" — correct but incomplete

❌ **Wrong (0 XP):**
- "It's a resistor that changes" or confuses with diode

---

**13. What is the difference between a capacitor and a battery?**

✅ **Full Answer (15 XP):**
- "Battery produces voltage chemically and continuously."
- "Capacitor temporarily stores charge; releases quickly when needed."
- "Battery has internal resistance and lasts a long time; capacitor charges/discharges fast."
- **Keyword:** Chemical reaction vs. charge storage

⚠️ **Partial Answer (10 XP):**
- "Battery lasts longer" or "Capacitor charges fast" — only one aspect

---

## Section 4: Calculations (25 XP each)

**14. Using Ohm's Law: V = 9V, R = 450Ω, find I**

✅ **Correct Answer (25 XP):**
```
Ohm's Law: V = I × R
Rearrange: I = V / R
I = 9V / 450Ω
I = 0.02 A  (or 20 mA)
```

⚠️ **Partial Credit (15 XP):**
- Correct formula but arithmetic error (e.g., I = 0.5A)
- Uses formula but no units in answer

❌ **No Credit (0 XP):**
- Wrong formula or logic

---

**15. 5V supply, red LED (2V forward voltage), 20 mA needed. Find resistor.**

✅ **Correct Answer (25 XP):**
```
Formula: R = (V_battery − V_LED) / I_desired
R = (5V − 2V) / 0.020A
R = 3V / 0.020A
R = 150 ohms

Acceptable range: 150Ω ± 10% (135–165Ω)
```

⚠️ **Partial Credit (15 XP):**
- Correct setup but arithmetic error
- Forgets to convert 20 mA to 0.02 A

❌ **No Credit (0 XP):**
- Wrong formula or missing subtraction step

---

**16. Resistor color: Orange-Orange-Brown. Find value.**

✅ **Correct Answer (25 XP):**
```
Orange = 3
Orange = 3
Brown = ×10 (multiplier)

Value = 33 × 10 = 330 ohms (330Ω)
```

⚠️ **Partial Credit (15 XP):**
- Correctly reads first two bands (33) but gets multiplier wrong
- States 3300Ω (reversed multiplier)

---

## Section 5: Application Scenarios (20 XP each)

**17. Three LEDs in series, total 6V drop on 9V battery, 15 mA. Do you need a resistor? Calculate it.**

✅ **Full Answer (20 XP):**
- **"Yes, you need a resistor."**
- Voltage across resistor: 9V − 6V = 3V
- Using Ohm's Law: R = 3V / 0.015A = **200 ohms**
- Explains: "Without it, current would exceed 15 mA and damage the LEDs."

⚠️ **Partial Credit (12 XP):**
- Correctly calculates resistor value but fails to explain WHY
- Says "yes" to resistor but calculation is wrong

❌ **No Credit (0 XP):**
- Says "no resistor needed" or logic is completely incorrect

---

**18. LED dims in summer heat. Explain why and what to adjust.**

✅ **Full Answer (20 XP):**
- **Explanation:** "As temperature rises, resistance of wires and components increases (thermal drift). Higher total resistance = lower current = dimmer LED."
- **Solution:** "Reduce the resistor value to increase current, OR use a voltage regulator to compensate for the thermal drift."
- **Alternative:** "Use a fixed resistor instead of component that changes with temperature."

⚠️ **Partial Credit (12 XP):**
- Mentions temperature causes dimming but no mechanism
- Solution is vague or incomplete

❌ **No Credit (0 XP):**
- "The battery dies" or completely incorrect explanation

---

## Section 6: Bonus Challenge (20 XP)

**19. Design a parallel LED circuit with resistors for red and green LEDs on 9V.**

✅ **Full Answer (20 XP):**
- **Circuit diagram shows:**
  - 9V battery
  - Two parallel branches: one for red, one for green
  - Each branch has its own resistor + LED
  - Both branches return to ground
  - Proper labels

- **Red LED Resistor:**
  ```
  R = (9V − 2V) / 0.020A = 7V / 0.020A = 350Ω
  ```

- **Green LED Resistor:**
  ```
  R = (9V − 2.2V) / 0.020A = 6.8V / 0.020A = 340Ω
  ```

- **Why parallel?** "Each LED gets full 9V but its own resistor limits current to 20 mA. If one burns out, the other still works."

⚠️ **Partial Credit (12 XP):**
- Correct circuit topology but wrong resistor calculations
- Calculations correct but circuit is series (wrong topology)

---

## Common Student Mistakes & How to Address

| Mistake | Why It Happens | Correction |
|---------|----------------|-----------|
| Forgets to convert mA to A | Unit confusion | "Always convert to base units: 20 mA = 0.020 A" |
| Uses 9V instead of (9V − 2V) in LED calculation | Forgets to subtract LED forward voltage | "Resistor only needs to drop the LEFTOVER voltage" |
| Reverses series/parallel logic | Confusion about current distribution | "Parallel = each path gets full voltage; series = voltage splits" |
| Reads color code as 330kΩ instead of 330Ω | Mistakes multiplier bands | Show them a real resistor with color bands |

---

## Stretch It! (Advanced Discussion)

**For high performers, discuss:**
- "What if you stacked 10 LEDs in series? Would your resistor value change? Why?"
- "Why don't we use a single huge resistor to protect everything?"
- "What happens in AC circuits? Does Ohm's Law still work?" (Intro to impedance)
- "How does a voltage regulator help with thermal drift?"

---

## Scoring Summary

| Section | Points | XP |
|---------|--------|-----|
| Section 1 (6 MC) | 12 | 72 |
| Section 2 (4 T/F) | 8 | 32 |
| Section 3 (3 SA) | 9 | 45 |
| Section 4 (3 Calc) | 15 | 75 |
| Section 5 (2 App Scenario) | 8 | 40 |
| **Subtotal** | **52** | **264** |
| Section 6 (Bonus challenge) | 0–6 | 0–20 |
| **TOTAL BASE** | **52** | **180** |
| **TOTAL WITH BONUS** | **52–58** | **180–200 XP** |

**Expected Distribution:**
- **180 XP:** Student answers all base questions correctly, skips or partially attempts bonus.
- **190 XP:** Student completes bonus with minor errors.
- **200 XP:** Perfect score on all sections including bonus.

