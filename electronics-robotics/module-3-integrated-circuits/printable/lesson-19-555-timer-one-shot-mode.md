# Lesson 19: 555 Timer Monostable -- One-Shot Mode

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 220

---

## What You'll Learn

✓ Monostable mode = ONE pulse per button press (one-shot)
✓ Use a button to trigger a timed pulse
✓ The 555 waits, then pulses for exactly the time you choose
✓ Build a pushbutton circuit that controls LED duration

---

## The Egg Timer Analogy

**Monostable = Press the button, wait for it...**

```
1. Press button = START timer (like flipping egg timer)
2. Timer counts down (like sand falling)
3. Time up = OUTPUT goes LOW (like egg timer bell)
4. Circuit waits for next button press
```

Unlike astable (always blinking), monostable waits for YOU!

---

## The One-Shot Pulse Sequence

```
Step 1: Waiting state (output LOW, no action)
        Button not pressed

Step 2: Button pressed! (triggers Pin 2)
        Output goes HIGH immediately

Step 3: Capacitor discharges for set time
        Output stays HIGH

Step 4: Time expires (reaches 1/3 VCC)
        Output goes LOW

Step 5: Back to waiting
        Ready for next button press
```

---

## Monostable Formula

```
Pulse duration (seconds) = 1.1 × R × C

Example:
R = 100k ohm, C = 47 microfarad
Duration = 1.1 × 100,000 × 0.000047
Duration ≈ 5.17 seconds
```

Bigger R or C = longer pulse

---

## The Circuit

```
+9V ─── [100k resistor] ─── Pin 7 & 6
                               │
                              [47µF C]
                               │
                              GND

Button connects to Pin 2
Pin 4 (Reset) to +9V
Pin 3 (Output) to LED
```

---

## Building Steps

1. Mount 555 IC (notch UP!)
2. Pin 8 → +9V, Pin 1 → GND
3. R (100k) from +9V to Pin 7
4. C (47µF) from Pin 6/7 junction to GND
5. Connect Pin 2 to Pin 6 (trigger)
6. Add push button: Button to Pin 2, other side to GND (with pull-up resistor)
7. Pin 4 to +9V (reset/enable)
8. Pin 3 through 330Ω to LED

---

## Testing

Press button → LED lights for 5+ seconds → LED off → Wait for next press

**Try different capacitors:**
- 10µF = ~1 second pulse
- 47µF = ~5 second pulse
- 100µF = ~10 second pulse

---

## Real-World Uses

- Alarm circuits (press to activate alarm for set time)
- Burglar alarms (motion sensor triggers 30-second siren)
- Automatic door timers (press button, door stays open for 5 seconds)
- Game timers (press to give player 60 seconds to act)

---

*Print this page and compare to Astable mode!*
