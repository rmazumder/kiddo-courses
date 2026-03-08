# Lesson 11: Series Circuits -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 220

---

## What You'll Learn

✓ Build a circuit where components are lined up one after another (like train cars)
✓ Understand that electricity takes ONE path through all components
✓ Measure voltage drops and prove they add up to the battery voltage
✓ Know: Remove ONE component = the WHOLE circuit stops

---

## The Big Idea: The Single-Track Train

![A single-track train loop analogy for series circuits. A colorful toy train track forms a complete oval loop. A battery locomotive (red/orange, labeled "Battery - the engine") pulls three cargo cars in a line: a resistor car (yellow, labeled "Resistor"), an LED car (bright with a glow, labeled "LED"), and a buzzer car (with sound waves, labeled "Buzzer"). Blue arrows along the track show the direction of flow, and a label reads "Only ONE path - everyone shares the same track!" The train cars are drawn as friendly cartoon characters riding the rails. A single track with no branches or forks is emphasized. A cheerful cartoon kid waves at the passing train from a platform. A callout bubble explains: "Same current flows through ALL components!"](../images/lesson-11-train-track-series.png)

**Series = ONE track for electricity**

| Feature | Series Circuit |
|---------|-----------------|
| **Paths** | ONE only |
| **Current** | Same everywhere |
| **Voltage** | Splits between components |
| **If one breaks** | Everything stops |

---

## Build It: Two Resistors in Series

```
9V (+) ---- [330Ω] ---- [470Ω] ---- 9V (-)
```

**On the breadboard:**
1. Battery: red to +rail, black to −rail
2. R1 (330Ω): row 5 to row 8
3. R2 (470Ω): row 8 to row 11
4. Jumper: row 11 to −rail

✓ **One track. Both resistors must work or nothing works.**

---

## Measure It: The Voltage Treasure Hunt

![A treasure trail map styled like a board game path for the voltage treasure hunt. The winding trail starts at a treasure chest labeled "9V Battery (Total Treasure: 9 gold coins)" in red/orange. Along the path are three stops: Stop 1 is a resistor gate that takes 2 gold coins (labeled "Resistor: 2V drop, 7 coins left"), Stop 2 is an LED castle that takes 2 coins (labeled "LED: 2V drop, 5 coins left"), and Stop 3 is a buzzer bridge that takes 5 coins (labeled "Buzzer: 5V drop, 0 coins left"). Gold coin icons are spent at each stop and the count decreases. At the end of the trail, a sign reads "All 9 coins spent! Voltage adds up to total!" A cartoon explorer kid walks the path collecting measurements with a multimeter probe as a walking stick. The path loops back to the battery to start again.](../images/lesson-11-voltage-treasure-hunt.png)

**Use your Multimeter (set to DC Volts, 20V range):**

1. **Total voltage** (across battery): _____ V
   → Should be about **9V**

2. **Voltage across R1** (330Ω): _____ V
   → Should be about **3.7V**

3. **Voltage across R2** (470Ω): _____ V
   → Should be about **5.3V**

**The magic:** 3.7V + 5.3V = 9V ✓
*All the voltage drops ADD UP to the battery voltage!* (Kirchhoff's Voltage Law)

---

## The Independence Test

![A diagram showing a circuit break test. Two panels: Left panel labeled "Series Circuit Intact": all three LEDs glow brightly in a line. Right panel labeled "One LED Removed": the other LEDs are dark/off, with an X through the broken LED. A cartoon kid removes one LED while making a confused face. Text reads: "Remove ONE component, and everything stops!"](../images/lesson-11-break-test-series.png)

**Remove the middle resistor.** What happens?
- Multimeter reads: _____ V (should be 0V)
- The circuit is BROKEN
- Current cannot flow anywhere

**That's series! One break = total stop.**

---

## Key Takeaways

1. **Series = Single track** → Electricity only has ONE path
2. **Same current everywhere** → All components get the same "flow"
3. **Voltage splits** → Each component uses up some of the battery's push
4. **Voltages add up** → V_R1 + V_R2 = V_battery
5. **Fragile circuit** → One broken part stops everything

---

## Quick Quiz (Test Yourself!)

**Q1:** In a series circuit, what's the same everywhere?
- A) Voltage
- B) Current
- C) Resistance
✓ **Answer: B (Current)**

**Q2:** You have a 9V battery and two resistors in series. R1 drops 4V. How much does R2 drop?
✓ **Answer: 5V** (4V + 5V = 9V)

**Q3:** What happens if you remove one resistor from a series circuit?
✓ **Answer: The whole circuit stops (open circuit)**

---

## Next Steps

Try building a **three-component series circuit** (battery → R1 → LED → R2 → battery).
Use your Wand to measure voltage at each stop!

**Pro Tip:** Series circuits are simple but fragile. Next lesson: parallel circuits (much more reliable!)

---

*Print this page. Keep it handy for reference!*
