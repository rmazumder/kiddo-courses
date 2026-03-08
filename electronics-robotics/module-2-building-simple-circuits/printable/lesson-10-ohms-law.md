# Lesson 10: Ohm's Law -- The Superpower Formula

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 240

---

## What You'll Learn

✓ The most important formula in electronics: **V = I × R**
✓ Predict what your Multimeter will measure BEFORE testing
✓ Calculate voltage, current, or resistance from a formula
✓ Understand why components have "ratings"
✓ Pick the right resistors for your circuits

---

## The Magic Formula

```
V = I × R

Voltage = Current × Resistance
```

**What it means:**
- **V (Volts):** How hard the battery pushes → Measured in Volts (V)
- **I (Amps):** How much electricity flows → Measured in Amps or milliamps (mA)
- **R (Ohms):** How much the component blocks → Measured in Ohms (Ω)

---

## The Water Park Analogy

Think of a water slide:

```
       WATER PUMP (Battery pushes water)
              ↓
       WATER PRESSURE (Voltage)
              ↓
       [ WIDE SLIDE ]  ← Low resistance, fast flow
              ↓
       [ NARROW SLIDE ] ← High resistance, slow flow
              ↓
         POOL (Return to pump)

In Electronics:
Battery pushes electrons (like water pressure)
Resistors slow the flow (like narrow slide)
More resistance = less current flows
```

**Ohm's Law is the SAME formula:**
```
Pressure = Flow × Narrowness
Voltage = Current × Resistance
V = I × R
```

---

## The Three Rearrangements

You can flip Ohm's Law to solve for any value:

### Formula 1: Find VOLTAGE
```
V = I × R

Example:
Current = 10 mA (0.01 A)
Resistance = 330 Ω
Voltage = 0.01 × 330 = 3.3V
```

### Formula 2: Find CURRENT
```
I = V / R

Example:
Voltage = 9V
Resistance = 1000 Ω (1k)
Current = 9 / 1000 = 0.009 A = 9 mA
```

### Formula 3: Find RESISTANCE
```
R = V / I

Example:
Voltage = 9V
Current = 20 mA (0.02 A)
Resistance = 9 / 0.02 = 450 Ω
```

---

## The VIR Triangle Trick

**Draw this and keep it handy!**

```
       +-------+
      /    V    \
     /  -------  \
    /   I  ×  R   \
   +----------------+
```

**How to use it:**
1. Cover the variable you want to find
2. Read what's left = your formula!

- **Cover V:** See I × R → `V = I × R`
- **Cover I:** See V / R → `I = V / R`
- **Cover R:** See V / I → `R = V / I`

---

## Practice Calculations

### Problem 1: LED with 330Ω resistor
```
Battery: 9V
Resistor: 330 ohms
LED forward voltage: 2V

Voltage across resistor: 9V - 2V = 7V

Current through circuit:
I = V / R
I = 7V / 330Ω
I = 0.0212 A = 21.2 mA
```
✓ **This is safe for an LED!**

### Problem 2: LED with 10k resistor (too much blocking)
```
Battery: 9V
Resistor: 10,000 ohms

Current:
I = 9V / 10,000Ω
I = 0.0009 A = 0.9 mA
```
✗ **Too little current! LED barely glows!**

### Problem 3: LED with 100Ω resistor (too little blocking)
```
Battery: 9V
Resistor: 100 ohms

Current:
I = 9V / 100Ω
I = 0.09 A = 90 mA
```
✗ **Too much current! LED burns out!**

### Problem 4: Which resistor for 15mA?
```
We need: I = 15 mA = 0.015 A
Battery: 9V
LED drops: 2V
Voltage for resistor: 9V - 2V = 7V

R = V / I
R = 7V / 0.015A
R = 466.7 Ω

→ Use a 470Ω resistor (closest standard value)
```

---

## Standard Resistor Values (Color Codes)

Common values you'll encounter:

| Value | Uses |
|-------|------|
| 100 Ω | Very low resistance (careful!) |
| **220 Ω** | LED protection (bright) |
| **330 Ω** | LED protection (standard) |
| 470 Ω | LED protection (dimmer) |
| **1k (1000 Ω)** | General purpose |
| 10k | High resistance (low current) |
| 100k | Very high resistance |

**Rules of thumb:**
- **330Ω** is your "safe bet" for most LEDs with 9V
- **Smaller R** = brighter LED (but more heat)
- **Bigger R** = dimmer LED (but safer)

---

## Why Ohm's Law Matters

1. **Pick the right resistor** → Without Ohm's Law, you guess and burn components
2. **Predict behavior** → "Will this LED be bright or dim?"
3. **Calculate power** → "How fast will my battery drain?"
4. **Debug circuits** → "Why isn't my LED working?"
5. **Design safely** → "Is this resistor strong enough?"

---

## Key Takeaways

1. **V = I × R** (Voltage = Current × Resistance)
2. **Can rearrange:** I = V/R or R = V/I
3. **Use VIR triangle** for quick formula lookup
4. **Test your math** with the Multimeter
5. **Pick resistors** using Ohm's Law to protect components

---

## Quick Quiz (Test Yourself!)

**Q1:** What does V = I × R mean?
✓ **Answer:** Voltage equals Current times Resistance

**Q2:** 9V battery, 1k resistor. How much current flows?
✓ **Answer:** I = 9 / 1000 = 0.009 A = 9 mA

**Q3:** You need 330Ω resistor but only have 220Ω. What happens?
✓ **Answer:** More current flows → LED is brighter (but hotter, shorter life)

**Q4:** LED needs 15mA and you have 9V. What resistor?
✓ **Answer:** R = V/I = 7V / 0.015A ≈ 470Ω

---

## Challenge

**Design a circuit:**
- Battery: 9V
- LED: needs 20mA max, forward voltage 2V
- What resistor value?

Calculate: R = (9V - 2V) / 0.020A = 7V / 0.020A = **350Ω**
→ Use a **330Ω** or **470Ω** resistor

---

## Your New Superpower

You can now:
- **Predict** circuit behavior before building
- **Calculate** component values
- **Understand** why circuits work (or don't work)
- **Design** circuits with confidence

🧙 **You are an electronics wizard now!**

---

*Print this page. Keep the VIR triangle with you always!*
