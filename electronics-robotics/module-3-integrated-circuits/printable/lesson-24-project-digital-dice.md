# Lesson 24: Project -- Digital Dice -- Quick Reference

**Age:** 6--12 years | **Time:** 60--90 min | **XP:** 360

---

## Building a Digital Dice

**Show any number 1-6 when you press the button!**

Combines EVERYTHING from Module 3:
- 555 timer (fast clock)
- 4017 counter (counts 1-6)
- Logic gates (decode outputs)
- 7 LEDs (dice face pattern)

---

## The Dice Face Pattern

Seven LED positions in 3x3 grid:

```
  A   B
C   G   D
  E   F
```

Which LEDs light for each number:
- **1:** G only (center)
- **2:** B, E (diagonal corners)
- **3:** B, G, E (diagonal line)
- **4:** A, B, E, F (four corners)
- **5:** A, B, G, E, F (four corners + center)
- **6:** A, B, C, D, E, F (all except center)

---

## The Circuit Chain

```
ROLL Button
     ↓
555 Timer (fast clock ~100 Hz)
     ↓
4017 Counter (cycles 1-6, resets to 1)
     ↓
Logic gates (decode which LEDs for current number)
     ↓
7 LED dice display
```

---

## How to Build

### Phase 1: Plan the Dice
- Arrange 7 LEDs in dice pattern
- Decide which output controls which LED
- Create logic equations for each number

### Phase 2: Build 555 + 4017
- 555 in astable mode (~100 Hz)
- 4017 counter connected to 555 output
- Limit 4017 to count only 1-6 (not 0-9)

### Phase 3: Add Logic Gates
- Use AND/OR gates to decode 4017 outputs
- Each gate controls one LED position
- Test each number pattern

### Phase 4: Assemble Dice
- Mount LEDs in physical dice housing (cardboard cube)
- Connect breadboard circuit
- Mount button for "ROLL"

### Phase 5: Test & Debug
- Press button → numbers 1-6 appear
- Verify each pattern matches standard dice
- Debug any LEDs not lighting

---

## Logic Equations (for each LED)

Use 4017 outputs (Q0-Q5) as inputs:

**Example for LED A (corner 1):**
```
A = Q3 OR Q4 OR Q5 (appears in numbers 4, 5, 6)
```

**Example for LED G (center):**
```
G = Q0 OR Q2 OR Q4 (appears in numbers 1, 3, 5)
```

(You'll derive these during the project)

---

## Real Electronics!

This project uses:
- ✓ Timing circuits (555)
- ✓ Counting circuits (4017)
- ✓ Logic gates (AND, OR)
- ✓ Output display (LEDs)
- ✓ Breadboarding & wiring
- ✓ Debugging with Wand

**You just built a real microcontroller project!**

---

## Challenge Extensions

**Faster rolling:** Speed up 555 clock
**Slower rolling:** Slow down 555 clock
**Auto-mode:** Remove button, let it roll continuously
**Sound:** Add piezo buzzer when rolling
**Multiple dice:** Build two dice, add together

---

*Print this with dice patterns diagram and circuit schematic!*
