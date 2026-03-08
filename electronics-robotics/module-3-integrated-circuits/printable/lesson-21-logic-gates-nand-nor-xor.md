# Lesson 21: Advanced Logic Gates NAND, NOR, XOR -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 230

---

## The Advanced Gates

**NAND:** NOT-AND (opposite of AND)
- Output 0 only when BOTH inputs are 1
- "You get IN unless both your keys work"

**NOR:** NOT-OR (opposite of OR)
- Output 1 only when BOTH inputs are 0
- "Light ON only if no switches pressed"

**XOR:** Exclusive OR
- Output 1 when inputs DIFFER
- "Two-switch light (either switch toggles, not both)"

---

## Truth Tables

### NAND (opposite of AND)
| A | B | OUT |
|---|---|-----|
| 0 | 0 | **1** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | 0 |

### NOR (opposite of OR)
| A | B | OUT |
|---|---|-----|
| 0 | 0 | **1** |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

### XOR (different = 1)
| A | B | OUT |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | 0 |

---

## The ICs

- **7400** = NAND (4 gates per chip)
- **7402** = NOR (4 gates per chip)
- **7486** = XOR (4 gates per chip)

---

## The NAND Secret

**NAND is "universal"** = You can build ANY gate using only NAND gates!

- NOT: Connect both NAND inputs together
- AND: NAND + NOT = AND
- OR: Build from NAND + NOTs
- XOR: Build from multiple NANDs

Clever, right?

---

## XOR Real-World: The Hallway Light

Two switches, one light:
- Switch A at entrance
- Switch B at far end

Either switch can toggle light ON/OFF
Both switches ON? Light OFF (XOR behavior)

This is why hallway lights use XOR!

---

*Print this page next to the basic gates reference!*
