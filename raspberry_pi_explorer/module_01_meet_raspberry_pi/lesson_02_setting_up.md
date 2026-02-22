# 🎮 Raspberry Pi Explorer — Module 1, Lesson 2: Setting Up Your Pi! 💻

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 1: MEET YOUR RASPBERRY PI  🍓                   ║
 ║  Lesson 2 of 3                                          ║
 ║  XP Available: 175 XP  |  Badge: 💻 Setup Star          ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** It's time to bring your Raspberry Pi to LIFE! 🎉 Today
you'll go from an empty box to a fully working computer. Think of it like
building a LEGO set — follow the steps, and at the end, you'll have something
AWESOME! 🏗️

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ List everything you need to set up a Raspberry Pi
- ✅ Flash (install) Raspberry Pi OS onto a MicroSD card
- ✅ Connect all the cables correctly
- ✅ Boot your Pi for the very first time! 🎉
- ✅ Navigate the Raspberry Pi desktop

---

## 🪝 Hook — Unboxing Day! 📦

Remember the feeling of opening a new toy or game on your birthday? 🎁 Today
is even BETTER! You're about to set up your very own computer — one that YOU
control, YOU program, and YOU build amazing things with.

In about 30 minutes, you'll go from "a bunch of stuff on a table" to a fully
working Raspberry Pi computer. Ready? Let's GO! 🚀

---

## 🧠 Learning Point 1: What You Need — The Setup Checklist ✅

Before we start, let's make sure you have EVERYTHING. Lay out all your items
on a clean, dry table. Check off each item:

```
┌─────────────────────────────────────────────────────────┐
│             📋 SETUP CHECKLIST                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  □  🍓 Raspberry Pi 4 (or Pi 5)                        │
│  □  💾 MicroSD Card (32GB+, Class 10)                   │
│  □  🔌 USB-C Power Supply (5V, 3A)                      │
│  □  📺 Monitor or TV with HDMI                          │
│  □  🔗 Micro-HDMI to HDMI cable                         │
│  □  ⌨️ USB Keyboard                                      │
│  □  🖱️ USB Mouse                                         │
│  □  🌐 Wi-Fi network name & password (ask a parent!)    │
│  □  💻 Another computer (to flash the SD card)          │
│  □  📱 SD card reader (or adapter)                      │
│                                                         │
│  OPTIONAL:                                              │
│  □  🧰 Pi Case (protects your Pi)                       │
│  □  🔊 Speakers or headphones                           │
│  □  🌐 Ethernet cable (if no Wi-Fi)                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> 🔑 **Key Vocabulary:**
> - **Flash** = Copy a special file (an "image") onto the SD card so the Pi can boot from it
> - **Boot** = Start up / turn on the computer for the first time
> - **OS** = Operating System — the main software that runs your computer (like Windows or macOS, but for Pi!)

---

## 🧠 Learning Point 2: Step-by-Step Setup! 🔧

### Step 1: Flash the SD Card with Raspberry Pi OS 💾

Your SD card is like the Pi's brain — it needs an **Operating System** (OS)
installed on it before the Pi can think!

**What you'll need for this step:**
- A regular computer (Windows, Mac, or Linux)
- Your MicroSD card
- An SD card reader

**Instructions:**

1. 🌐 On your regular computer, go to: **https://www.raspberrypi.com/software/**
2. 📥 Download **"Raspberry Pi Imager"** (it's free!)
3. 💿 Install and open Raspberry Pi Imager
4. You'll see a screen like this:

```
┌──────────────────────────────────────────────────┐
│          🍓 Raspberry Pi Imager                   │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐              │
│  │  CHOOSE      │  │  CHOOSE      │              │
│  │  DEVICE      │  │  OS           │              │
│  │  🍓          │  │  💿          │              │
│  └──────────────┘  └──────────────┘              │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐              │
│  │  CHOOSE      │  │              │              │
│  │  STORAGE     │  │    NEXT      │              │
│  │  💾          │  │    ▶️         │              │
│  └──────────────┘  └──────────────┘              │
│                                                  │
└──────────────────────────────────────────────────┘
```

5. Click **"CHOOSE DEVICE"** → Select your Pi model (Raspberry Pi 4 or 5)
6. Click **"CHOOSE OS"** → Select **"Raspberry Pi OS (64-bit)"** (the recommended one!)
7. 💾 Insert your MicroSD card into your computer's SD card reader
8. Click **"CHOOSE STORAGE"** → Select your MicroSD card

```
⚠️ WARNING: This will ERASE everything on the SD card!
   Make sure you're selecting the RIGHT card!
   Ask a parent if you're unsure! 👨‍👩‍👧‍👦
```

9. Click **"NEXT"**
10. It will ask: **"Would you like to apply OS customisation settings?"**
    - Click **"EDIT SETTINGS"**
    - Set your **username** (e.g., `pi`) and **password** (pick something you'll remember!)
    - Enter your **Wi-Fi network name** and **password**
    - Set your **timezone** and **country**
    - Click **"SAVE"** then **"YES"**
11. ⏳ Wait for it to write and verify (this takes 5-15 minutes)
12. 🎉 When it says **"Write Successful"**, remove the SD card!

> 💡 **Analogy:** Flashing the SD card is like loading a game cartridge.
> Without the game (OS) loaded, the console (Pi) has nothing to play!

---

### Step 2: Connect Everything! 🔌

Now let's plug everything in! Follow this EXACT order:

```
⚠️ IMPORTANT: Do NOT plug in the power cable yet!
   Connect everything ELSE first!
```

```
    📺 MONITOR/TV
         │
    HDMI Cable
         │
         ▼
    ┌─────────────────────────────────┐
    │         RASPBERRY PI            │
    │                                 │
    │  SD Card ──→ [inserted underneath]
    │                                 │
    │  HDMI ──→ [to your TV/monitor] │
    │                                 │
    │  USB ──→ [keyboard] ⌨️          │
    │  USB ──→ [mouse] 🖱️             │
    │                                 │
    │  USB-C ──→ [power - LAST!] 🔌  │
    └─────────────────────────────────┘
```

**Connection Order (IMPORTANT!):**

1. **💾 Insert the MicroSD card** into the slot on the BOTTOM of the Pi
   (it clicks in gently — don't force it!)

```
   The SD card slot is on the underside:

   ┌──────────────────────┐
   │     Pi (bottom)      │
   │                      │
   │           ┌──────┐   │
   │           │SD    │◄── Push in gently until it clicks
   │           │Card  │   │
   │           └──────┘   │
   └──────────────────────┘
```

2. **📺 Connect the HDMI cable** from the Pi to your monitor/TV
   - Use the **HDMI 0** port (the one closest to the USB-C power port)
   - Make sure your TV is set to the right HDMI input!

3. **⌨️ Plug in the keyboard** to any USB port

4. **🖱️ Plug in the mouse** to any USB port

5. **🔊 Plug in speakers/headphones** (optional) to the audio jack

---

### Step 3: POWER ON! ⚡🎉

This is the exciting part!

```
🔌 NOW plug in the USB-C power cable!

   Power Supply ──→ USB-C Port on Pi

   ┌──────────┐        ┌──────────┐
   │  WALL    │────────│  Pi      │
   │  OUTLET  │  USB-C │  USB-C   │
   │  🔌      │────────│  Port    │
   └──────────┘        └──────────┘
```

**What you should see:**

1. 🔴 A **red LED** lights up on the Pi → This means it has power!
2. 🟢 A **green LED** starts blinking → This means it's reading the SD card!
3. 📺 Your screen shows the **rainbow screen** briefly (this is normal!)
4. 📺 Then you'll see the **Raspberry Pi OS loading screen**!

```
   What your screen looks like during boot:

   ┌────────────────────────────────────────┐
   │                                        │
   │          🌈🌈🌈🌈🌈🌈🌈🌈             │
   │          🌈 RAINBOW  🌈               │
   │          🌈 SCREEN   🌈               │
   │          🌈🌈🌈🌈🌈🌈🌈🌈             │
   │                                        │
   │   (This appears for just a second!)    │
   │                                        │
   └────────────────────────────────────────┘
              ↓ Then... ↓
   ┌────────────────────────────────────────┐
   │                                        │
   │     🍓 Raspberry Pi OS                 │
   │                                        │
   │     Loading...                         │
   │     ████████████░░░░░░░ 65%            │
   │                                        │
   └────────────────────────────────────────┘
              ↓ Finally... ↓
   ┌────────────────────────────────────────┐
   │ 🖥️ THE DESKTOP! 🎉                     │
   │                                        │
   │  ┌──────────────────────────────────┐  │
   │  │ 🍓 Files  🌐 Browser  📁 Folder │  │
   │  │                                  │  │
   │  │                                  │  │
   │  │     Your beautiful desktop!      │  │
   │  │         You did it! 🎉          │  │
   │  │                                  │  │
   │  │                                  │  │
   │  └──────────────────────────────────┘  │
   │  [🍓 Menu] [📁] [🌐] [📧]    [🔊 📶]│
   └────────────────────────────────────────┘
```

> 🎉 **CONGRATULATIONS!** If you see the desktop, your Pi is alive and working!
> You just set up a computer! How cool is that?! 🍓

---

### Step 4: First Boot Setup 🔧

The first time your Pi boots, it might ask you a few questions:

1. **Country & Language** — Select yours from the dropdown
2. **Set Password** — If you didn't set one during flashing, create one now!
   - Pick something you'll remember but others won't guess
   - Write it down somewhere safe! 📝
3. **Wi-Fi** — Connect to your home network (if you didn't set it up during flashing)
4. **Update Software** — It might ask to update. Click YES!
   - ⏳ This can take 10-20 minutes — be patient!
5. **Restart** — Click "Restart" when prompted

---

## 🧠 Learning Point 3: The Raspberry Pi Desktop Tour 🖥️

Welcome to your new computer! Let's explore what everything does:

```
┌──────────────────────────────────────────────────────────┐
│ 🍓 Pi Menu                              🔊  📶  🔋  ⏰ │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
│         ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│         │ 📁       │  │ 🗑️       │  │ 🌐       │       │
│         │ File     │  │ Trash    │  │ Web      │       │
│         │ Manager  │  │ Can      │  │ Browser  │       │
│         └──────────┘  └──────────┘  └──────────┘       │
│                                                          │
│                                                          │
│                     🍓                                   │
│              (Your wallpaper!)                           │
│                                                          │
│                                                          │
├──────────────────────────────────────────────────────────┤
│ [🍓] [📁] [🌐] [📧]                     [🔊] [📶] [⏰]│
│  ▲    ▲    ▲    ▲                          ▲    ▲    ▲  │
│  │    │    │    │                          │    │    │  │
│ Menu File Web  Mail                     Volume WiFi Time│
│      Mgr  Brwsr                                         │
└──────────────────────────────────────────────────────────┘
```

### Important Things on the Desktop:

| What | Where | What It Does |
|------|-------|-------------|
| 🍓 **Pi Menu** | Top-left corner | Opens all apps — like a Start menu! |
| 📁 **File Manager** | Taskbar or desktop | Browse your files and folders |
| 🌐 **Web Browser** | Taskbar | Surf the internet! (Chromium browser) |
| 🖥️ **Terminal** | Pi Menu → Accessories | The COMMAND LINE — your superpower tool! ⚡ |
| 🐍 **Thonny** | Pi Menu → Programming | Write Python code here! |
| 📶 **Wi-Fi** | Top-right corner | Shows your internet connection |
| 🔊 **Volume** | Top-right corner | Control speaker volume |
| ⏰ **Clock** | Top-right corner | Shows the time |

### How to Open the Terminal (You'll Use This A LOT!) 💻

The **Terminal** is where you type commands to control your Pi like a hacker
in a movie (but for real!). 😎

**To open Terminal:**
1. Click the 🍓 **Pi Menu** (top-left)
2. Go to **"Accessories"**
3. Click **"Terminal"**

**Or even faster:** Look for the terminal icon on the taskbar (it looks like
a black rectangle `>_`)

```
┌──────────────────────────────────────────┐
│ pi@raspberrypi:~ $                       │
│                                          │
│ (This is the Terminal!)                  │
│ (You type commands here!)               │
│ (You're basically a hacker now!) 😎      │
│                                          │
└──────────────────────────────────────────┘
```

### How to Open Thonny (Your Code Editor!) 🐍

**Thonny** is where you'll write Python programs to control LEDs, read sensors,
and build all your projects!

1. Click the 🍓 **Pi Menu**
2. Go to **"Programming"**
3. Click **"Thonny Python IDE"**

```
┌──────────────────────────────────────────────────────┐
│ Thonny - Python IDE                          [–][□][×]│
├──────────────────────────────────────────────────────┤
│ # Write your Python code here!                       │
│ print("Hello, Raspberry Pi! 🍓")                     │
│                                                      │
│                                                      │
│                                                      │
├──────────────────────────────────────────────────────┤
│ >>> Hello, Raspberry Pi! 🍓                          │
│ >>>                                                  │
│ (This area shows the output of your code!)           │
└──────────────────────────────────────────────────────┘
```

---

## 🧠 Learning Point 4: How to Safely Shut Down Your Pi ⚠️

**NEVER just unplug your Pi!** This can damage your SD card and lose your files!

It's like pulling the plug on a game console while it's saving — you could
corrupt your save file! 😱

**The SAFE way to shut down:**

1. Click the 🍓 **Pi Menu** (top-left)
2. Click **"Logout"**
3. Click **"Shutdown"**

**OR from the Terminal:**
```bash
sudo shutdown -h now
```

> 🔑 **Key Vocabulary:**
> - **sudo** = "Super User Do" — gives you admin powers (like a master key! 🔑)
> - **shutdown** = Tells the Pi to turn off
> - **-h** = "Halt" — stop completely
> - **now** = Do it right away!

**Wait for the green LED to stop blinking**, THEN unplug the power.

```
⚠️ SAFETY RULE:
   Green LED blinking = Pi is still working! DON'T unplug!
   Green LED off = Safe to unplug! ✅
```

---

## 🎮 Activity 1: First Boot Scavenger Hunt! 🔍

**+25 XP**

Now that your Pi is running, let's explore! Find each of these things and
check them off:

```
┌──────────────────────────────────────────────────┐
│            🔍 SCAVENGER HUNT                     │
├──────────────────────────────────────────────────┤
│                                                  │
│  □ Find and open the FILE MANAGER                │
│    → How many folders are in /home/pi/?          │
│       Answer: ___                                │
│                                                  │
│  □ Find and open the WEB BROWSER                 │
│    → What is the default homepage?               │
│       Answer: ___                                │
│                                                  │
│  □ Find and open THONNY (Programming)            │
│    → Type: print("I am a Pi Explorer!")          │
│    → Click Run! What happened?                   │
│       Answer: ___                                │
│                                                  │
│  □ Find and open the TERMINAL                    │
│    → Type: hostname                              │
│    → What is your Pi's name?                     │
│       Answer: ___                                │
│                                                  │
│  □ Check your Wi-Fi connection                   │
│    → Are you connected? YES / NO                 │
│    → What's your network name?                   │
│       Answer: ___                                │
│                                                  │
│  □ Find the current time on your Pi              │
│    → What time does it show?                     │
│       Answer: ___                                │
│                                                  │
│  □ Change the desktop wallpaper!                 │
│    → Right-click desktop → Desktop Preferences   │
│    → Did you change it? YES / NO                 │
│                                                  │
│  BONUS: Find the version of Raspberry Pi OS      │
│    → Terminal: cat /etc/os-release               │
│    → What version? ___                           │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Your First Python Program! 🐍

**+25 XP**

Let's write your very first program on the Raspberry Pi!

1. Open **Thonny** (Pi Menu → Programming → Thonny)
2. Type this code EXACTLY:

```python
# My First Raspberry Pi Program! 🍓
# By: [Your Name]
# Date: [Today's Date]

print("=" * 40)
print("🍓 HELLO, RASPBERRY PI! 🍓")
print("=" * 40)
print()
print("My name is [YOUR NAME]!")
print("I am a Raspberry Pi Explorer!")
print("Today I set up my very own computer!")
print()
print("Fun facts about MY Pi:")
print("  🔴 It's the size of a credit card")
print("  🟢 It has 40 GPIO pins")
print("  🔵 It runs Linux!")
print("  🟡 I'm going to build amazing things!")
print()
print("=" * 40)
print("🚀 LET THE ADVENTURE BEGIN! 🚀")
print("=" * 40)
```

3. Click **"Run"** (the green ▶️ button) or press **F5**
4. Save the file as `hello_pi.py` when asked

**Expected output:**
```
========================================
🍓 HELLO, RASPBERRY PI! 🍓
========================================

My name is [YOUR NAME]!
I am a Raspberry Pi Explorer!
Today I set up my very own computer!

Fun facts about MY Pi:
  🔴 It's the size of a credit card
  🟢 It has 40 GPIO pins
  🔵 It runs Linux!
  🟡 I'm going to build amazing things!

========================================
🚀 LET THE ADVENTURE BEGIN! 🚀
========================================
```

> 🎉 You just wrote and ran your first program on the Raspberry Pi! YOU'RE A CODER! 🐍

---

## 🎮 Activity 3: Personalize Your Pi! 🎨

**+25 XP**

Make your Pi feel like HOME! Complete at least 3 of these customizations:

```
□ 1. Change your desktop wallpaper
      → Right-click desktop → Desktop Preferences

□ 2. Change the taskbar position
      → Right-click taskbar → Panel Settings → Position

□ 3. Set the correct timezone
      → Pi Menu → Preferences → Raspberry Pi Configuration → Localisation

□ 4. Test the sound
      → Plug in headphones → Right-click volume icon → Test

□ 5. Open the web browser and bookmark your favorite website

□ 6. Create a folder called "my_projects" on the desktop
      → Right-click desktop → Create New → Folder
```

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What software do you use to flash the SD card?
- A) Microsoft Word
- B) Raspberry Pi Imager
- C) iTunes
- D) Photoshop

**Q2:** What should you NEVER do when shutting down your Pi?
- A) Click the Pi Menu
- B) Type "sudo shutdown -h now"
- C) Just pull out the power cable
- D) Click "Shutdown"

**Q3:** What is Thonny used for?
- A) Playing games
- B) Browsing the internet
- C) Writing Python code
- D) Listening to music

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — Raspberry Pi Imager! It's the official tool from the Pi Foundation.
- **Q2: C** — NEVER just pull the power! Always shut down safely first! ⚠️
- **Q3: C** — Thonny is your Python code editor! You'll use it for ALL your projects! 🐍

</details>

---

## 🏅 Lesson Complete — Setup Star Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 AMAZING WORK, EXPLORER! 🎉            ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║         💻 SETUP STAR BADGE 💻                ║
 ║                                              ║
 ║     Your Pi is set up and running!           ║
 ║     You're officially a Pi owner! 🍓         ║
 ║                                              ║
 ║     XP Earned This Lesson:                   ║
 ║     📖 Reading: +50 XP                       ║
 ║     🎮 Activity 1 (Scavenger Hunt): +25 XP   ║
 ║     🎮 Activity 2 (First Program): +25 XP    ║
 ║     🎮 Activity 3 (Personalize): +25 XP      ║
 ║     ⚡ Quiz: up to +60 XP                    ║
 ║     ─────────────────────                    ║
 ║     💰 TOTAL: up to 185 XP                   ║
 ║                                              ║
 ║     Running Total: up to 370 XP              ║
 ║     Level: 🌿 Pi Apprentice!                 ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 1.3: Linux on Pi — Become a Terminal Ninja!** 🐧

You'll learn to control your Pi with text commands — just like a real hacker!
Type commands, navigate folders, and feel like you're in a movie! 🎬

---

*Your Pi is alive! You gave it power, an OS, and a purpose. That's incredible!* ⭐
