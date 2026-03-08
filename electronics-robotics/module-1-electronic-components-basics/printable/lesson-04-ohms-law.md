# Lesson 4: Ohm's Law -- Quick Reference

**Age:** 6--12 years | **Time:** 50--55 min | **XP:** 260

---

## Ohm's Law Formula

![Water System Ohm's Law](../images/lesson-04-water-system-ohms-law.png)

**V = I × R**

- **V** (Voltage) = Electrical pressure in volts
- **I** (Current) = Flow of electrons in amps
- **R** (Resistance) = Opposition in ohms

**Analogy:** V (pump pressure) × I (water flow) ÷ R (pipe narrowness)

---

## VIR Triangle

![VIR Triangle](../images/lesson-04-vir-triangle.png)

**Use the triangle to solve for any variable:**

```
       V
    -------
    I  ×  R
```

**To solve:**
- **Find V?** V = I × R
- **Find I?** I = V ÷ R
- **Find R?** R = V ÷ I

---

## Practice Examples

**Example 1:** Battery = 9V, LED current = 20mA (0.02A)
- R = V ÷ I = 9 ÷ 0.02 = 450Ω
- (Use a 470Ω resistor)

**Example 2:** You have a 220Ω resistor, 9V battery
- I = V ÷ R = 9 ÷ 220 = 0.041A = 41mA
- (LED gets 41mA of current)

---

## Parameter Effects

![Parameter Effects Table](../images/lesson-04-parameter-effects-table.png)

| Change | Effect on Current | LED Brightness |
|--------|------------------|-----------------|
| More voltage ↑ | Current goes UP ↑ | Brighter ↑ |
| More resistance ↑ | Current goes DOWN ↓ | Dimmer ↓ |
| Less resistance ↓ | Current goes UP ↑ | Brighter ↑ |

---

## Real-World Applications

- 🔦 **Flashlight design** — Choose resistor to protect LED
- 🏠 **House wiring** — Circuit breakers use Ohm's Law
- 🔋 **Battery selection** — Pick voltage for your circuit
- 🌡️ **Temperature** — Resistance changes with heat (thermistor)

---

## Quick Quiz

**Q1:** What does Ohm's Law say?
**A:** V = I × R (Voltage equals current times resistance).

**Q2:** If you double the voltage but keep resistance the same, what happens to current?
**A:** Current doubles (doubles the "pressure" = doubles the flow).

**Q3:** Why do you need a resistor with an LED?
**A:** LEDs only handle a few volts; a resistor limits the current to safe levels.

---

## Challenge

**Design your circuit:** Calculate what resistor you need to safely connect an LED to your 9V battery. (Target: 20mA of current)

---

*Print this with the VIR triangle for reference!*
