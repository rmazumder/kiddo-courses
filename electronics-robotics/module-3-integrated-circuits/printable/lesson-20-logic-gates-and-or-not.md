# Lesson 20: Logic Gates AND, OR, NOT -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 230

---

## The Three Basic Logic Gates

**AND Gate:** Both inputs must be ON = Output ON
- Analogy: "Both keys AND the door opens"

**OR Gate:** Either input ON = Output ON
- Analogy: "Door A OR Door B = You get in"

**NOT Gate:** Inverts input (opposite)
- Analogy: "Mirror shows opposite"

---

## Truth Tables

### AND (both must be 1)
| A | B | OUT |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

### OR (either can be 1)
| A | B | OUT |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

### NOT (inverts)
| IN | OUT |
|----|-----|
| 0 | **1** |
| 1 | 0 |

---

## The ICs

- **7408** = AND gate (4 gates per chip)
- **7432** = OR gate (4 gates per chip)
- **7404** = NOT gate (6 gates per chip)

---

## Pin Layout (7408 AND as example)

Pin 14 = VCC (+5V)
Pin 7 = GND
Pins 1-2 = Input A, B (Gate 1)
Pin 3 = Output (Gate 1)
Similar pattern for other 3 gates

---

## Building a Circuit

1. Mount IC, Pin 14 to +5V, Pin 7 to GND
2. Connect push buttons or switches to inputs
3. Connect output to LED through 330Ω resistor
4. Test with truth table

---

## Challenge

Combine gates to build more complex logic!

*Print this page as reference for all basic gates!*
