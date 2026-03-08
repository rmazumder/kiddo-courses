# Lesson 22: Seven-Segment Display -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 230

---

## The 7-Segment Display

Seven LEDs arranged in a pattern that can display all digits 0-9:

```
    a
   ───
  │ g │
f │   │ b
  │ d │
   ───
  │   │
e │   │ c
  │ e │
   ───
```

---

## Segment Layout

```
  a
 ─ ─
f g b
 ─ ─
e d c
```

Segments a, b, c, d, e, f, g = 7 segments (plus decimal point DP)

---

## Which Segments Make Each Digit?

| # | Segments | # | Segments |
|---|----------|---|----------|
| 0 | abcdef | 5 | afgcd |
| 1 | bc | 6 | afgedc |
| 2 | abged | 7 | abc |
| 3 | abgcd | 8 | all 7 |
| 4 | fgbc | 9 | abgfcd |

---

## The 7447 BCD Decoder

**BCD = Binary Coded Decimal**
- 4 binary inputs (0-15)
- 7 outputs control the 7 segments
- Automatically lights correct segments for each digit!

**Inputs:** Pins A, B, C, D (binary 0000-1111)
**Outputs:** Pins a-g connect directly to segment LEDs

---

## How to Use 7447

1. Connect Pin 16 to +5V, Pin 8 to GND
2. Connect 4 switches/buttons to inputs A, B, C, D
3. Connect each output (a-g) through 220Ω resistor to LED segment
4. Connect all LED common cathodes to GND
5. Flip switches → digits appear!

---

## Pin Numbers

```
7447 IC pinout:
 1 = A (input LSB)
 2 = B (input)
 6 = C (input)
 7 = D (input MSB)
 9 = a (output)
10 = b
11 = c
12 = d
13 = e
14 = f
15 = g
16 = VCC (+5V)
 8 = GND
```

---

## Real-World Uses

- Digital clocks and timers
- Scoreboards
- Elevator floor numbers
- Microwave timers
- Thermostats

---

*Print this with the 7447 pinout for reference!*
