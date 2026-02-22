# 📝 Raspberry Pi Explorer — Module 2 Quiz: GPIO & Electronics! ⚡

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 2 QUIZ — GPIO & ELECTRONICS  ⚡                 ║
 ║  12 Questions  |  240 XP possible + 100 bonus           ║
 ║  Badge: 📝 Quiz Ace 2 (Score 80%+)                      ║
 ╚══════════════════════════════════════════════════════════╝
```

> **Instructions:** Answer all 12 questions. Each correct answer = **+20 XP**!
> Score 10 or more correct (80%+) to earn the **📝 Quiz Ace 2** badge!
> Perfect 12/12 = **+100 XP BONUS!** 🎯

---

## Question 1 📡

**What does GPIO stand for?**

- A) General Purpose Input/Output
- B) Green Pin Internal Output
- C) Graphics Processing Interface Online
- D) General Pin Integration Operation

---

## Question 2 ⚡

**What voltage do GPIO output pins provide when set to HIGH?**

- A) 5V
- B) 12V
- C) 3.3V
- D) 1.5V

---

## Question 3 🔌

**How many total pins are on the Raspberry Pi's GPIO header?**

- A) 20
- B) 26
- C) 40
- D) 50

---

## Question 4 💡

**Which leg of an LED is the positive (+) leg?**

- A) The short leg
- B) The bent leg
- C) The long leg
- D) Both legs are the same

---

## Question 5 🛡️

**Why must you ALWAYS use a resistor with an LED?**

- A) To make the LED brighter
- B) To change the color of the LED
- C) To limit current and prevent the LED from burning out
- D) Because the breadboard requires it

---

## Question 6 🍞

**On a breadboard, which holes are connected together?**

- A) All holes in the same column (top to bottom)
- B) All holes everywhere
- C) Holes in the same row, on the same side (e.g., a1-e1)
- D) Only holes next to each other diagonally

---

## Question 7 🐍

**What Python command turns ON an LED connected to GPIO 17?**

- A) `GPIO.input(17, GPIO.HIGH)`
- B) `GPIO.output(17, GPIO.HIGH)`
- C) `GPIO.on(17)`
- D) `LED.turn_on(17)`

---

## Question 8 🔢

**What's the difference between BCM and BOARD numbering?**

- A) BCM uses the chip's numbers; BOARD uses physical pin positions
- B) They're the same thing
- C) BCM is for buttons; BOARD is for LEDs
- D) BCM only works on Pi 3; BOARD works on Pi 4

---

## Question 9 ⚠️

**What should you do BEFORE connecting or changing wires on your Pi?**

- A) Run the program first
- B) Nothing, just plug wires in anytime
- C) Shut down and unplug the Pi completely
- D) Close all Terminal windows

---

## Question 10 🧹

**What does `GPIO.cleanup()` do?**

- A) Deletes all Python files
- B) Resets all GPIO pins to their default state
- C) Turns off the Pi
- D) Removes the RPi.GPIO library

---

## Question 11 🔘

**When a GPIO pin is set to INPUT and reads HIGH, what does that mean?**

- A) The pin is broken
- B) The pin is detecting voltage (something is ON, like a pressed button)
- C) The LED is too bright
- D) The Pi needs to restart

---

## Question 12 🚦

**In the traffic light project, what order do the lights go?**

- A) Red → Yellow → Green → Red
- B) Green → Yellow → Red → Red+Yellow → Green
- C) Green → Red → Yellow → Green
- D) All on at the same time → all off

---

## 📊 Score Tracker

```
┌─────────────────────────────────────────┐
│         MY QUIZ 2 SCORE                 │
├─────────────────────────────────────────┤
│                                         │
│  Q1:  ○ Correct  ○ Incorrect            │
│  Q2:  ○ Correct  ○ Incorrect            │
│  Q3:  ○ Correct  ○ Incorrect            │
│  Q4:  ○ Correct  ○ Incorrect            │
│  Q5:  ○ Correct  ○ Incorrect            │
│  Q6:  ○ Correct  ○ Incorrect            │
│  Q7:  ○ Correct  ○ Incorrect            │
│  Q8:  ○ Correct  ○ Incorrect            │
│  Q9:  ○ Correct  ○ Incorrect            │
│  Q10: ○ Correct  ○ Incorrect            │
│  Q11: ○ Correct  ○ Incorrect            │
│  Q12: ○ Correct  ○ Incorrect            │
│                                         │
│  Total Correct: ___ / 12               │
│  XP Earned:     ___ / 240 XP           │
│  Perfect Score Bonus: ___              │
│                                         │
│  Badge Earned:                          │
│  □ 📝 Quiz Ace 2 (80%+ = 10/12)        │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🔍 Answer Key

<details>
<summary>🔐 Click to reveal ALL answers!</summary>

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | **A** | General Purpose Input/Output — the magic pins! |
| 2 | **C** | 3.3V! Never connect GPIO to 5V! |
| 3 | **C** | 40 total pins (26 GPIO + power + ground + special) |
| 4 | **C** | The LONG leg is positive. "Long leg = positive vibes!" |
| 5 | **C** | Resistors limit current to protect the LED from burning out |
| 6 | **C** | Same row, same side! (a-e or f-j in the same numbered row) |
| 7 | **B** | `GPIO.output(17, GPIO.HIGH)` sends 3.3V to pin 17 |
| 8 | **A** | BCM = chip's internal numbering; BOARD = physical pin position |
| 9 | **C** | ALWAYS shut down and unplug before changing wires! |
| 10 | **B** | Cleanup resets all pins to their default safe state |
| 11 | **B** | HIGH means the pin detects voltage — something is active! |
| 12 | **B** | Green → Yellow → Red → Red+Yellow → back to Green! |

### Scoring:
```
12/12 = 240 XP + 100 BONUS = 340 XP total! 🏆 PERFECT!
11/12 = 220 XP  ⭐ Incredible!
10/12 = 200 XP  🏅 Quiz Ace 2 Badge Earned!
9/12  = 180 XP  💪 So close!
8/12  = 160 XP  📖 Good effort!
<8    = Review Module 2 and try again! 💪
```

</details>

---

## 🏅 Quiz Complete!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║  📝 MODULE 2 QUIZ COMPLETE! 📝               ║
 ║                                              ║
 ║  Score 10+ out of 12?                        ║
 ║  You earned: 📝 QUIZ ACE 2 BADGE! 🏅         ║
 ║                                              ║
 ║  MODULE 2 COMPLETE!                          ║
 ║  You're an electronics pro now! ⚡            ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Module 3: Cool Projects!** 🎉

LED patterns, sensors, buzzers, and music! Get ready to build some SERIOUSLY
cool stuff! 🎵🌡️📏🔔

---

*GPIO mastered! You're ready for the next level!* ⚡
