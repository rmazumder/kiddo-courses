# 🎮 Raspberry Pi Explorer — Module 2, Lesson 1: What is GPIO? 🔌

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 2: GPIO & ELECTRONICS  ⚡                       ║
 ║  Lesson 1 of 3                                          ║
 ║  XP Available: 175 XP  |  Badge: 🔌 GPIO Guide          ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Welcome to the MOST EXCITING module yet! 🎉 Today you'll
discover the **secret superpower** of the Raspberry Pi — its **GPIO pins**!
These 40 tiny metal pins are what make the Pi different from any other computer.
They're like 40 magic fingers that can sense, control, and communicate with the
outside world! 🦸

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Explain what GPIO pins are and why they're special
- ✅ Know the difference between INPUT and OUTPUT pins
- ✅ Understand voltage levels (3.3V vs 5V) and why they matter
- ✅ Read a GPIO pin diagram using BOTH numbering systems (BCM & BOARD)
- ✅ Follow all GPIO safety rules to protect your Pi

---

## 🪝 Hook — Your Pi's Hidden Superpowers! 🦸

Look at the top of your Raspberry Pi. See those **40 little metal pins** sticking
up in two neat rows? Most people walk right past them. But YOU know better!

Those pins are like **40 tiny superpowers** waiting to be unlocked. With them,
you can:
- 💡 Turn lights on and off
- 🔘 Read button presses
- 🌡️ Measure temperature
- 📏 Measure distance
- 🎵 Play music through a buzzer
- 🤖 Control robots and motors
- 🚨 Build alarm systems

**No regular computer can do this!** A laptop doesn't have GPIO pins. A desktop
PC doesn't have them. Only YOUR Raspberry Pi has them! That makes your Pi special.

---

## 🧠 Learning Point 1: What IS GPIO? 📡

**GPIO** stands for **G**eneral **P**urpose **I**nput/**O**utput.

Let's break that down:
- **General Purpose** = They can be used for LOTS of different things
- **Input** = The pin can LISTEN (read data from buttons, sensors, etc.)
- **Output** = The pin can TALK (send power to LEDs, buzzers, motors, etc.)

> 💡 **Analogy:** Think of GPIO pins like your HANDS:
> - **Input Mode** = Your hands FEELING things (is this hot? cold? smooth? rough?)
> - **Output Mode** = Your hands DOING things (pushing, pulling, pressing buttons)
>
> Each GPIO pin can be set to either mode — just like you choose whether to feel
> something or grab something with your hand!

### Input vs. Output — Simple Examples:

```
📥 INPUT (Pi LISTENS):                📤 OUTPUT (Pi TALKS):
┌──────────────────────┐              ┌──────────────────────┐
│                      │              │                      │
│  🔘 Button pressed?  │              │  💡 Turn LED on!     │
│  🌡️ What temperature? │              │  🔔 Make buzzer beep!│
│  📏 How far away?    │              │  🤖 Spin motor!      │
│  💧 Is it wet?       │              │  📺 Show on display! │
│                      │              │                      │
│  The Pi READS data   │              │  The Pi SENDS power  │
│  FROM the outside    │              │  TO the outside      │
│  world               │              │  world               │
│                      │              │                      │
└──────────────────────┘              └──────────────────────┘
```

---

## 🧠 Learning Point 2: The Pin Map — Know Your Pins! 🗺️

Your Pi has **40 pins total**, but they're NOT all the same! Some provide power,
some are ground (like the negative terminal on a battery), and some are the
programmable GPIO pins.

### The Complete GPIO Pin Diagram 📊

```
    🍓 RASPBERRY PI GPIO PIN MAP 🍓
    (Looking at the Pi with USB ports pointing DOWN)

          3.3V  (1) (2)  5V
    GPIO2/SDA1  (3) (4)  5V
    GPIO3/SCL1  (5) (6)  GND
         GPIO4  (7) (8)  GPIO14/TXD
           GND  (9) (10) GPIO15/RXD
        GPIO17 (11) (12) GPIO18/PWM0
        GPIO27 (13) (14) GND
        GPIO22 (15) (16) GPIO23
          3.3V (17) (18) GPIO24
  GPIO10/MOSI  (19) (20) GND
   GPIO9/MISO  (21) (22) GPIO25
  GPIO11/SCLK  (23) (24) GPIO8/CE0
           GND (25) (26) GPIO7/CE1
   GPIO0/ID_SD (27) (28) GPIO1/ID_SC
         GPIO5 (29) (30) GND
         GPIO6 (31) (32) GPIO12/PWM0
   GPIO13/PWM1 (33) (34) GND
   GPIO19/MISO (35) (36) GPIO16
        GPIO26 (37) (38) GPIO20/MOSI
           GND (39) (40) GPIO21/SCLK

    COLOR CODE:
    🔴 = 3.3V Power       (pins 1, 17)
    🟠 = 5V Power         (pins 2, 4)
    ⚫ = Ground/GND       (pins 6, 9, 14, 20, 25, 30, 34, 39)
    🟢 = GPIO (usable!)   (all other pins)
```

### Visual Color Map:

```
    ┌─────────────────────────────────────────┐
    │         GPIO PIN HEADER (Top View)       │
    │                                          │
    │   🔴  ○  ○  🟠     PIN 1 is here! ──→ 🔴│
    │   🟢  ○  ○  🟠                           │
    │   🟢  ○  ○  ⚫                           │
    │   🟢  ○  ○  🟢                           │
    │   ⚫  ○  ○  🟢                           │
    │   🟢  ○  ○  🟢                           │
    │   🟢  ○  ○  ⚫                           │
    │   🟢  ○  ○  🟢                           │
    │   🔴  ○  ○  🟢                           │
    │   🟢  ○  ○  ⚫                           │
    │   🟢  ○  ○  🟢                           │
    │   🟢  ○  ○  🟢                           │
    │   🟢  ○  ○  ⚫                           │
    │   🟢  ○  ○  🟢                           │
    │   🟢  ○  ○  🟢                           │
    │   ⚫  ○  ○  🟢                           │
    │   🟢  ○  ○  🟢                           │
    │   🟢  ○  ○  ⚫                           │
    │   🟢  ○  ○  🟢                           │
    │   ⚫  ○  ○  🟢                           │
    │                                          │
    │   Left column: ODD pins (1,3,5...)       │
    │   Right column: EVEN pins (2,4,6...)     │
    └─────────────────────────────────────────┘
```

### Types of Pins:

| Pin Type | Count | What It Does |
|----------|-------|-------------|
| 🔴 **3.3V Power** | 2 pins | Provides 3.3 volts of power |
| 🟠 **5V Power** | 2 pins | Provides 5 volts of power |
| ⚫ **Ground (GND)** | 8 pins | The "return path" for electricity (like the negative end of a battery) |
| 🟢 **GPIO** | 26 pins | The programmable pins YOU control with code! |
| 🔵 **Special** | 2 pins | ID EEPROM pins (pins 27, 28) — don't use these! |

> 🔑 **Key Vocabulary:**
> - **3.3V** = 3.3 volts — the SAFE voltage for GPIO pins
> - **5V** = 5 volts — MORE power, but can DAMAGE things meant for 3.3V!
> - **GND** = Ground — the "exit" path for electricity. Every circuit needs one!
> - **GPIO** = The pins you can program as input or output

---

## 🧠 Learning Point 3: Two Ways to Count Pins! 🔢

Here's where it gets a little tricky (but don't worry, you've got this!).

There are **TWO different numbering systems** for GPIO pins:

### 1. BOARD Numbering 📋

Counts pins by their **physical position** on the board: 1, 2, 3, 4...40.

```
BOARD numbers = The PHYSICAL pin positions
Pin 1 is at the top-left, Pin 40 is at the bottom-right.
Simple counting: 1, 2, 3, 4, 5... 40
```

### 2. BCM Numbering 🧠

Counts pins by their **Broadcom chip number**: GPIO2, GPIO3, GPIO4...GPIO27.

```
BCM numbers = The CHIP's internal numbering
These DON'T go in order! GPIO17 might be on physical pin 11!
These are used by the computer's brain (BCM chip).
```

### Side-by-Side Comparison:

```
Physical   BCM         Physical   BCM
(BOARD)    Number      (BOARD)    Number
────────────────────────────────────────
Pin 1  → 3.3V Power   Pin 2  → 5V Power
Pin 3  → GPIO 2       Pin 4  → 5V Power
Pin 5  → GPIO 3       Pin 6  → GND
Pin 7  → GPIO 4       Pin 8  → GPIO 14
Pin 9  → GND          Pin 10 → GPIO 15
Pin 11 → GPIO 17      Pin 12 → GPIO 18
Pin 13 → GPIO 27      Pin 14 → GND
Pin 15 → GPIO 22      Pin 16 → GPIO 23
...and so on!
```

> 💡 **Analogy:** Imagine a classroom:
> - **BOARD numbering** = Seat numbers (Seat 1, Seat 2, Seat 3...)
> - **BCM numbering** = Student names (Alex in Seat 1, Charlie in Seat 3...)
>
> Same student, two ways to find them!

### Which Should YOU Use?

In this course, we'll use **BCM numbering** because:
- It's more common in tutorials and guides
- The Python library (RPi.GPIO) uses it by default
- Most example code online uses BCM

**We'll always write it like this:** `GPIO 17` (BCM number)

---

## 🧠 Learning Point 4: Voltage — The Power Rules! ⚡

```
⚠️⚠️⚠️ CRITICAL SAFETY INFORMATION ⚠️⚠️⚠️
```

### Understanding Voltage Levels:

| Voltage | Where? | Safe for GPIO? |
|---------|--------|---------------|
| **3.3V** | GPIO pins output this | ✅ YES! This is GPIO voltage! |
| **5V** | The 5V power pins (2 & 4) | ❌ NOT for GPIO! Can damage them! |
| **0V** | Ground (GND) pins | ✅ Safe — it's the "off" state |

### What HIGH and LOW Mean:

When a GPIO pin is set to **OUTPUT**:
```
HIGH (ON)  = Pin sends out 3.3V  → LED lights up! 💡
LOW  (OFF) = Pin sends out 0V   → LED turns off  ⚫
```

When a GPIO pin is set to **INPUT**:
```
HIGH = Pin detects 3.3V → "Something is ON!"   (like a button pressed)
LOW  = Pin detects 0V   → "Nothing happening"  (button not pressed)
```

> 💡 **Analogy:** Think of a light switch:
> - **HIGH** = Switch is UP (light on!) 💡
> - **LOW** = Switch is DOWN (light off) ⚫

---

## 🧠 Learning Point 5: Safety Rules for GPIO! 🛡️

```
╔══════════════════════════════════════════════════════════════╗
║                  ⚠️ GPIO SAFETY RULES ⚠️                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. 🔴 NEVER connect a GPIO pin directly to 5V!            ║
║     → GPIO pins are 3.3V ONLY! 5V WILL damage them!        ║
║                                                              ║
║  2. 🔴 NEVER connect two GPIO pins directly together!       ║
║     → If one is HIGH (3.3V) and one is LOW (0V),           ║
║       you'll create a short circuit! 💥                      ║
║                                                              ║
║  3. 🔴 NEVER draw more than 16mA from a single GPIO pin!   ║
║     → Always use a resistor with LEDs!                      ║
║     → The TOTAL across all pins should not exceed 50mA      ║
║                                                              ║
║  4. 🔴 ALWAYS wire your circuit with the Pi POWERED OFF!    ║
║     → Shut down → Unplug → Wire → Plug in → Boot           ║
║                                                              ║
║  5. 🔴 ALWAYS double-check your wiring before powering on!  ║
║     → One wrong wire can damage your Pi permanently!        ║
║                                                              ║
║  6. 🟢 ALWAYS use resistors with LEDs!                      ║
║     → A 220Ω resistor is perfect for most LEDs              ║
║                                                              ║
║  7. 🟢 ALWAYS connect GND (ground) to complete circuits!    ║
║     → Every circuit needs a path back to ground             ║
║                                                              ║
║  8. 🟡 Be CAREFUL with static electricity!                  ║
║     → Touch a metal object before handling your Pi          ║
║     → Don't walk on carpet in socks then touch GPIO pins!   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

> 🔑 **Key Vocabulary:**
> - **mA** = Milliamps — a measure of electrical current (how much electricity flows)
> - **Resistor** = A component that limits current flow (protects your components!)
> - **Short Circuit** = When electricity takes a wrong shortcut — BAD! 💥
> - **Ground (GND)** = The return path for electricity, like the drain in a sink

---

## 🎮 Activity 1: GPIO Pin Scavenger Hunt! 🔍

**+25 XP**

Look at the GPIO pin map above and answer these questions:

```
┌──────────────────────────────────────────────────────┐
│           🔍 GPIO SCAVENGER HUNT                     │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. How many GND (ground) pins are there?            │
│     Answer: ___                                      │
│                                                      │
│  2. What is on physical pin 1? (top-left)            │
│     Answer: ___                                      │
│                                                      │
│  3. What BCM GPIO number is on physical pin 11?      │
│     Answer: GPIO ___                                 │
│                                                      │
│  4. Which physical pins provide 5V power?            │
│     Answer: Pin ___ and Pin ___                      │
│                                                      │
│  5. Is it safe to connect a GPIO pin to 5V?          │
│     Answer: YES / NO                                 │
│                                                      │
│  6. How many programmable GPIO pins are there?       │
│     Answer: ___                                      │
│                                                      │
│  7. What physical pin is GPIO 17?                    │
│     Answer: Pin ___                                  │
│                                                      │
│  8. What voltage do GPIO output pins send?           │
│     Answer: ___ V                                    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

<details>
<summary>🔍 Click to reveal answers!</summary>

1. **8** GND pins (pins 6, 9, 14, 20, 25, 30, 34, 39)
2. **3.3V Power**
3. **GPIO 17**
4. Pin **2** and Pin **4**
5. **NO!** Never! It will damage your GPIO! ⚠️
6. **26** programmable GPIO pins
7. Pin **11**
8. **3.3V**

</details>

---

## 🎮 Activity 2: Input or Output? Sort the Devices! 🔀

**+25 XP**

For each device below, decide: Would the Pi use an **INPUT** pin or an
**OUTPUT** pin to work with it?

| # | Device | INPUT or OUTPUT? |
|---|--------|-----------------|
| 1 | 💡 LED (light) | ___ |
| 2 | 🔘 Push button | ___ |
| 3 | 🔔 Buzzer | ___ |
| 4 | 🌡️ Temperature sensor | ___ |
| 5 | 🤖 Motor | ___ |
| 6 | 📏 Distance sensor | ___ |
| 7 | 💧 Rain sensor | ___ |
| 8 | 📺 Small screen/display | ___ |

<details>
<summary>🔍 Click to reveal answers!</summary>

| # | Device | Answer | Why? |
|---|--------|--------|------|
| 1 | 💡 LED | **OUTPUT** | Pi SENDS power to make the LED light up |
| 2 | 🔘 Button | **INPUT** | Pi READS whether the button is pressed |
| 3 | 🔔 Buzzer | **OUTPUT** | Pi SENDS signals to make sound |
| 4 | 🌡️ Temp sensor | **INPUT** | Pi READS data from the sensor |
| 5 | 🤖 Motor | **OUTPUT** | Pi SENDS power to spin the motor |
| 6 | 📏 Distance sensor | **BOTH!** | OUTPUT to send a signal, INPUT to read the echo! |
| 7 | 💧 Rain sensor | **INPUT** | Pi READS whether it's wet |
| 8 | 📺 Display | **OUTPUT** | Pi SENDS data to show on screen |

</details>

---

## 🎮 Activity 3: Find the GPIO Pins on YOUR Pi! 👆

**+25 XP**

This is a HANDS-ON activity! Grab your actual Raspberry Pi (make sure it's
**powered OFF and unplugged**!) and complete these tasks:

```
⚠️ Pi must be POWERED OFF for this activity!
```

```
┌──────────────────────────────────────────────────────┐
│         👆 FIND THE PINS!                            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  □ 1. Find the GPIO header (40 pins in 2 rows)      │
│       Where is it located on the board?              │
│       Answer: ___________________________            │
│                                                      │
│  □ 2. Find Pin 1 (top-left, near the corner)         │
│       Some boards have a square pad for Pin 1!       │
│       Can you spot it? YES / NO                      │
│                                                      │
│  □ 3. Count the pins in one row                      │
│       How many in each row? ___                      │
│       How many rows? ___                             │
│       Total: ___ × ___ = ___                         │
│                                                      │
│  □ 4. Look at your Pi — can you find these?          │
│       □ The Ethernet port                            │
│       □ The USB ports                                │
│       □ The HDMI ports                               │
│       □ The USB-C power port                         │
│       □ The SD card slot (underneath!)               │
│                                                      │
│  □ 5. Now look at the GPIO pin map in this lesson    │
│       and point to where these pins would be:        │
│       □ A 5V pin                                     │
│       □ A GND pin                                    │
│       □ GPIO 17 (physical pin 11)                    │
│       □ GPIO 18 (physical pin 12)                    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What does GPIO stand for?
- A) Great Pins for Internet Output
- B) General Purpose Input/Output
- C) Green Pin Indicator On
- D) Graphics Processing Input/Output

**Q2:** What voltage do GPIO pins use?
- A) 12V
- B) 5V
- C) 3.3V
- D) 1.5V

**Q3:** How many total pins are on the GPIO header?
- A) 20
- B) 26
- C) 40
- D) 50

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — General Purpose Input/Output!
- **Q2: C** — 3.3V! Remember: NEVER use 5V with GPIO pins! ⚠️
- **Q3: C** — 40 pins total (26 GPIO + power + ground + special pins)

</details>

---

## 🏅 Lesson Complete — GPIO Guide Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 ELECTRIFYING WORK, EXPLORER! 🎉       ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║         🔌 GPIO GUIDE BADGE 🔌                ║
 ║                                              ║
 ║     You know your GPIO pins inside and out!  ║
 ║     The world of electronics awaits! ⚡      ║
 ║                                              ║
 ║     XP Earned This Lesson:                   ║
 ║     📖 Reading: +50 XP                       ║
 ║     🎮 Activity 1: +25 XP                    ║
 ║     🎮 Activity 2: +25 XP                    ║
 ║     🎮 Activity 3: +25 XP                    ║
 ║     ⚡ Quiz: up to +60 XP                    ║
 ║     ─────────────────────                    ║
 ║     💰 TOTAL: up to 185 XP                   ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 2.2: LEDs and Circuits!** 💡

You'll learn about LEDs, resistors, and breadboards — then BUILD your very
first circuit! Get your components ready — things are about to LIGHT UP! ✨

---

*You just learned the language of electronics! Those 40 pins are YOUR superpowers now!* ⚡
