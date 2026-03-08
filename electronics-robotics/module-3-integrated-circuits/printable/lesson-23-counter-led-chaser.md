# Lesson 23: Counter LED Chaser -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 230

---

## The 4017 Decade Counter

**Counter = Counts from 0 to 9, one output at a time**

Like a spotlight sweeping across 10 LEDs in sequence!

---

## How It Works

```
Clock pulse in (from 555)
         ↓
    4017 Counter
         ↓
Output 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (repeat)
```

Only ONE output is HIGH at any moment

---

## The Circuit Combination

**555 Timer (astable) + 4017 Counter = LED Chaser**

```
555 generates clock pulses
        ↓
    4017 counts them
        ↓
   10 LEDs light in sequence
   (one at a time)
```

Result: Chase pattern!

---

## 4017 Pin Connections

```
Pin 16 = VCC (+5V)
Pin  8 = GND
Pin 13 = Clock (from 555 Pin 3)
Pins 1-11 = Outputs Q0-Q9 (connect to LEDs)
Pin 12 = Reset (tie to GND normally, or use button to reset)
```

---

## Circuit Speed

**Speed = 555 frequency**

- Slow 555 (1 Hz) = LED chases slowly (1 per second)
- Fast 555 (10 Hz) = LED chases quickly (10 per second)
- Very fast (100 Hz) = appears continuous glow

Adjust 555 resistors/capacitor to change chase speed!

---

## Building Steps

1. Build 555 in astable mode (blinker)
2. Mount 4017 IC (notch UP)
3. Pin 16 to +5V, Pin 8 to GND
4. Pin 13 to Pin 3 of 555 (clock input)
5. Each output Q0-Q9 to 330Ω resistor then LED to GND
6. Power ON → LEDs chase!

---

## Variations

**Change chase direction:** Wire outputs in different order

**Change speed:** Modify 555 R and C values

**Add button:** Connect to Pin 12 (reset) to restart chase

**Multiple patterns:** Use different output combinations

---

*Print this with the chaser wiring diagram!*
