# 🎮 Raspberry Pi Explorer — Module 1, Lesson 3: Linux on Pi — Terminal Ninja! 🐧

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 1: MEET YOUR RASPBERRY PI  🍓                   ║
 ║  Lesson 3 of 3                                          ║
 ║  XP Available: 200 XP  |  Badge: 🐧 Linux Ninja         ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Time to become a TERMINAL NINJA! 🥷 You'll learn to
control your Raspberry Pi with text commands typed into the Terminal. This is
how REAL hackers, engineers, and computer scientists work. When you type
commands into a black screen and things happen — that's POWER! 💪

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Open and use the Terminal like a pro
- ✅ Navigate the file system (move between folders)
- ✅ Create, view, and delete files and folders
- ✅ Use Pi-specific commands (check temperature, update software)
- ✅ Feel like a real hacker 😎

---

## 🪝 Hook — The Secret Language of Computers 🤫

In movies, you see hackers typing super-fast on a black screen with green text,
right? 🎬 That's called a **Terminal** (or **command line**). And guess what?

**That's EXACTLY what you're about to learn!**

The Terminal is like having a conversation with your computer:
- You TYPE a command (ask the computer to do something)
- The computer DOES it and shows you the result
- It's faster than clicking around with a mouse once you know the commands!

Think of it like this: using a mouse is like pointing at things in a restaurant
menu. Using the Terminal is like SPEAKING the order directly to the chef! 🍳

---

## 🧠 Learning Point 1: Terminal Basics — Your First Commands! 🚀

### Opening the Terminal

Click the **Terminal icon** on the taskbar (it looks like `>_`) or go to:
**Pi Menu → Accessories → Terminal**

You'll see something like this:
```
pi@raspberrypi:~ $
```

Let's break that down:
```
pi          = Your username (who you are)
@           = "at"
raspberrypi = Your Pi's name
:~          = Where you are (~ means your home folder)
$           = Ready for your command!
```

> 🔑 **Key Vocabulary:**
> - **Terminal** = A text-based way to control your computer
> - **Command** = An instruction you type for the computer
> - **Directory** = A fancy word for "folder"
> - **Path** = The address/location of a file or folder

### The Essential Commands — Your Ninja Toolkit! 🥷

#### 1. `pwd` — "Where Am I?" 📍

**P**rint **W**orking **D**irectory — tells you which folder you're in right now.

```bash
pi@raspberrypi:~ $ pwd
/home/pi
```

> 💡 **Analogy:** It's like asking "What room am I in?" and the house answers
> "You're in the bedroom!"

#### 2. `ls` — "What's In Here?" 👀

**L**i**s**t — shows all files and folders in the current directory.

```bash
pi@raspberrypi:~ $ ls
Desktop    Documents    Downloads    Music    Pictures    Videos
```

**Power-up versions:**
```bash
ls -l        # Long format (shows details like size and date)
ls -a        # Show ALL files, including hidden ones (starting with .)
ls -la       # Both! Details AND hidden files!
```

> 💡 **Analogy:** It's like opening a drawer and seeing what's inside!

#### 3. `cd` — "Take Me There!" 🚶

**C**hange **D**irectory — moves you to a different folder.

```bash
cd Desktop           # Go into the Desktop folder
cd ..                # Go BACK one folder (to the parent)
cd ~                 # Go HOME (back to /home/pi)
cd /                 # Go to the very TOP of the file system
```

```
🗂️ Think of folders like rooms in a house:

    / (root - the whole house)
    ├── home/
    │   └── pi/          ← This is YOUR room! (home folder)
    │       ├── Desktop/
    │       ├── Documents/
    │       ├── Downloads/
    │       ├── Music/
    │       ├── Pictures/
    │       └── Videos/
    ├── etc/             ← System settings
    ├── usr/             ← Programs
    ├── tmp/             ← Temporary files
    └── var/             ← System logs
```

#### 4. `mkdir` — "Build a New Room!" 🏗️

**M**a**k**e **Dir**ectory — creates a new folder.

```bash
mkdir my_projects              # Creates a folder called "my_projects"
mkdir my_projects/led_fun      # Creates a subfolder inside my_projects
```

#### 5. `touch` — "Create a New File!" 📄

Creates a new, empty file.

```bash
touch hello.txt                # Creates an empty file called hello.txt
touch my_projects/notes.txt    # Creates a file inside my_projects
```

#### 6. `cat` — "Read This File!" 📖

Con**cat**enate — displays the contents of a file.

```bash
cat hello.txt                  # Shows what's inside hello.txt
```

#### 7. `nano` — "Edit This File!" ✏️

Opens a simple text editor right in the Terminal!

```bash
nano hello.txt                 # Opens hello.txt for editing
```

```
┌──────────────────────────────────────────┐
│  GNU nano — hello.txt                    │
├──────────────────────────────────────────┤
│                                          │
│  Hello! This is my first Pi file!        │
│  I'm learning Linux commands!            │
│                                          │
│                                          │
├──────────────────────────────────────────┤
│ ^X Exit  ^O Save  ^K Cut  ^U Paste      │
└──────────────────────────────────────────┘

^ means hold the Ctrl key!
Ctrl + O = Save the file
Ctrl + X = Exit nano
```

#### 8. `cp` — "Copy This!" 📋

```bash
cp hello.txt hello_backup.txt          # Copy a file
cp -r my_folder my_folder_backup       # Copy a whole folder (-r = recursive)
```

#### 9. `mv` — "Move (or Rename) This!" 📦

```bash
mv hello.txt Documents/               # Move file to Documents folder
mv old_name.txt new_name.txt           # Rename a file!
```

#### 10. `rm` — "Delete This!" 🗑️

```bash
rm hello.txt                   # Delete a file (CAREFUL! No undo!)
rm -r my_old_folder            # Delete a folder and everything in it
```

```
⚠️ WARNING: rm is PERMANENT! There is NO recycle bin!
   Once you delete something with rm, it's GONE FOREVER!
   Always double-check before deleting! 🔍
```

#### 11. `clear` — "Clean the Screen!" 🧹

```bash
clear                          # Clears all the text on the Terminal
```

---

## 🧠 Learning Point 2: Pi-Specific Commands! 🍓

These commands are special — they only work on a Raspberry Pi!

### Check Your Pi's Temperature 🌡️

Your Pi can get hot when it's working hard! Check its temperature:

```bash
vcgencmd measure_temp
```

**Output:**
```
temp=45.0'C
```

> 💡 Normal is 40-60°C. If it goes above 80°C, your Pi needs a fan or heatsink!

### Check Your Pi's Voltage ⚡

```bash
vcgencmd measure_volts
```

### See How Much RAM is Being Used 🧠

```bash
free -h
```

**Output:**
```
              total        used        free
Mem:          3.7Gi       512Mi       2.8Gi
```

### See How Much SD Card Space is Left 💾

```bash
df -h
```

### See What's Running on Your Pi 📊

```bash
htop
```

This opens a colorful display showing everything your Pi is doing! Press `q`
to exit.

### Your Pi's Network Info 🌐

```bash
hostname -I               # Shows your Pi's IP address
ifconfig                   # Detailed network information
ping google.com            # Test if your internet is working (Ctrl+C to stop)
```

---

## 🧠 Learning Point 3: Updating Your Pi! 🔄

Just like your phone gets updates, your Pi needs updates too! This keeps it
safe and adds new features.

### The Two Magic Update Commands:

```bash
sudo apt update            # Check WHAT updates are available
sudo apt upgrade -y        # INSTALL the updates (-y means "yes to all")
```

> 🔑 **Key Vocabulary:**
> - **sudo** = "Super User Do" — gives you admin powers! Like a master key 🔑
> - **apt** = The Pi's app store / package manager
> - **update** = Check for new versions
> - **upgrade** = Install the new versions

```
💡 Think of it like this:

sudo apt update    →  "Check the app store for updates" 🔍
sudo apt upgrade   →  "Download and install them all!" 📥

Always run UPDATE first, THEN UPGRADE!
```

### Install New Software:

```bash
sudo apt install [program-name]       # Install a new program
```

For example:
```bash
sudo apt install cowsay                # Install a fun program!
cowsay "I love Raspberry Pi!"          # Try it out!
```

**Output:**
```
 ________________________
< I love Raspberry Pi!  >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

> 😂 Try it! `cowsay` is a real program that makes a cow say things!

---

## 🧠 Learning Point 4: Exploring the Pi File System 🗺️

```
/ (root - The VERY TOP of everything!)
│
├── /home/pi/              👤 YOUR stuff! Projects, files, photos
│   ├── Desktop/
│   ├── Documents/
│   ├── Downloads/
│   ├── Music/
│   ├── Pictures/
│   └── Videos/
│
├── /boot/                 🥾 Files needed to START the Pi
│
├── /etc/                  ⚙️ Configuration files (Pi settings)
│
├── /usr/                  📦 Programs and apps live here
│   ├── /usr/bin/          → Executable programs
│   └── /usr/lib/          → Library files programs need
│
├── /var/                  📝 Log files and variable data
│   └── /var/log/          → System logs (diaries!)
│
├── /tmp/                  🗑️ Temporary files (auto-deleted)
│
├── /dev/                  🔌 Device files (USB, GPIO, etc.)
│
├── /proc/                 🧠 Running processes info
│
└── /opt/                  📁 Optional software
```

> 💡 **Analogy:** The file system is like a building:
> - `/` is the front door (root — everything starts here)
> - `/home/pi` is YOUR bedroom (your personal space!)
> - `/etc` is the control room (system settings)
> - `/tmp` is the trash room (temporary stuff)
> - `/dev` is the hardware room (where physical devices connect)

---

## 🎮 Activity 1: Terminal Obstacle Course! 🏃

**+25 XP**

Complete each step IN ORDER. Type each command and write what happened!

```
┌──────────────────────────────────────────────────────────┐
│          🏃 TERMINAL OBSTACLE COURSE 🏃                  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│ Step 1: Find out where you are                           │
│   Command: pwd                                           │
│   Result: ____________________________                   │
│                                                          │
│ Step 2: List what's in your home folder                  │
│   Command: ls                                            │
│   Result: ____________________________                   │
│                                                          │
│ Step 3: Create a new folder called "ninja_training"      │
│   Command: mkdir ninja_training                          │
│   ✅ Done? □                                             │
│                                                          │
│ Step 4: Go INTO that folder                              │
│   Command: cd ninja_training                             │
│   ✅ Done? □                                             │
│                                                          │
│ Step 5: Confirm you're in the right place                │
│   Command: pwd                                           │
│   Result: ____________________________                   │
│                                                          │
│ Step 6: Create 3 files                                   │
│   Command: touch secret1.txt secret2.txt secret3.txt     │
│   ✅ Done? □                                             │
│                                                          │
│ Step 7: List the files to see them                       │
│   Command: ls                                            │
│   Result: ____________________________                   │
│                                                          │
│ Step 8: Write something in secret1.txt                   │
│   Command: nano secret1.txt                              │
│   → Type a secret message, then Ctrl+O, Enter, Ctrl+X   │
│   ✅ Done? □                                             │
│                                                          │
│ Step 9: Read your secret message                         │
│   Command: cat secret1.txt                               │
│   Result: ____________________________                   │
│                                                          │
│ Step 10: Go back home                                    │
│   Command: cd ~                                          │
│   Verify: pwd (should say /home/pi)                      │
│   ✅ Done? □                                             │
│                                                          │
│ 🎉 OBSTACLE COURSE COMPLETE! You're a Terminal Ninja! 🥷│
└──────────────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Pi Health Check! 🏥

**+25 XP**

Let's give your Pi a full health checkup! Run each command and record the results.

```
┌──────────────────────────────────────────────────┐
│           🏥 PI HEALTH CHECK REPORT              │
├──────────────────────────────────────────────────┤
│                                                  │
│  Patient: Raspberry Pi                           │
│  Doctor: _________________________ (your name)   │
│                                                  │
│  1. Temperature Check 🌡️                         │
│     Command: vcgencmd measure_temp               │
│     Temperature: ________°C                      │
│     Healthy? (under 60°C = yes) ____             │
│                                                  │
│  2. Memory Check 🧠                              │
│     Command: free -h                             │
│     Total RAM: ______                            │
│     Used RAM: ______                             │
│     Free RAM: ______                             │
│                                                  │
│  3. Storage Check 💾                             │
│     Command: df -h                               │
│     Total Space: ______                          │
│     Used Space: ______                           │
│     Free Space: ______                           │
│                                                  │
│  4. Network Check 🌐                             │
│     Command: hostname -I                         │
│     IP Address: ______                           │
│     Internet Working? (ping google.com)          │
│     Result: YES / NO                             │
│                                                  │
│  5. Uptime Check ⏰                              │
│     Command: uptime                              │
│     How long has Pi been on? ______              │
│                                                  │
│  6. OS Version 📋                                │
│     Command: cat /etc/os-release                 │
│     Version: ______                              │
│                                                  │
│  DIAGNOSIS: My Pi is ____________! 🎉            │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 3: Build a Project Folder Structure! 📁

**+25 XP**

Real programmers organize their files neatly! Create this folder structure
using ONLY Terminal commands:

**Target Structure:**
```
/home/pi/pi_explorer/
├── module_01/
│   ├── notes.txt         (write "Module 1 complete!" inside)
│   └── code/
├── module_02/
│   ├── notes.txt         (write "GPIO is awesome!" inside)
│   └── code/
├── module_03/
│   ├── notes.txt         (write "Sensors rock!" inside)
│   └── code/
└── module_04/
    ├── notes.txt         (write "Final project here!" inside)
    └── code/
```

**Commands to use (fill in the blanks!):**

```bash
# Step 1: Go home
cd ~

# Step 2: Create the main folder
mkdir _______________

# Step 3: Create all module folders
mkdir _______________/module_01
mkdir _______________/module_02
mkdir _______________/module_03
mkdir _______________/module_04

# Step 4: Create code subfolders in each
mkdir _______________/module_01/code
mkdir _______________/module_02/code
mkdir _______________/module_03/code
mkdir _______________/module_04/code

# Step 5: Create and write to notes files
echo "Module 1 complete!" > _______________/module_01/notes.txt
echo "GPIO is awesome!" > _______________/module_02/notes.txt
echo "Sensors rock!" > _______________/module_03/notes.txt
echo "Final project here!" > _______________/module_04/notes.txt

# Step 6: Verify your work!
ls -R pi_explorer
```

<details>
<summary>🔍 Click to reveal the answers!</summary>

```bash
cd ~
mkdir pi_explorer
mkdir pi_explorer/module_01
mkdir pi_explorer/module_02
mkdir pi_explorer/module_03
mkdir pi_explorer/module_04
mkdir pi_explorer/module_01/code
mkdir pi_explorer/module_02/code
mkdir pi_explorer/module_03/code
mkdir pi_explorer/module_04/code
echo "Module 1 complete!" > pi_explorer/module_01/notes.txt
echo "GPIO is awesome!" > pi_explorer/module_02/notes.txt
echo "Sensors rock!" > pi_explorer/module_03/notes.txt
echo "Final project here!" > pi_explorer/module_04/notes.txt
ls -R pi_explorer
```

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What command shows you which folder you're currently in?
- A) `ls`
- B) `cd`
- C) `pwd`
- D) `rm`

**Q2:** What does `sudo` mean?
- A) "Super Undo"
- B) "Super User Do" — gives you admin powers
- C) "System Update"
- D) "Shut Down"

**Q3:** How do you safely shut down your Pi from the Terminal?
- A) `rm everything`
- B) `shutdown please`
- C) `sudo shutdown -h now`
- D) Just pull the power cable

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: C** — `pwd` = Print Working Directory! Shows where you are. 📍
- **Q2: B** — "Super User Do" — it's like a master key! 🔑
- **Q3: C** — `sudo shutdown -h now` — always shut down safely! ⚠️

</details>

---

## 🏅 Lesson Complete — Linux Ninja Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 INCREDIBLE WORK, NINJA! 🎉            ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║          🐧 LINUX NINJA BADGE 🐧              ║
 ║                                              ║
 ║     You can navigate the Terminal like       ║
 ║     a PRO! Commands bow before you! 🥷       ║
 ║                                              ║
 ║     XP Earned This Lesson:                   ║
 ║     📖 Reading: +50 XP                       ║
 ║     🎮 Activity 1 (Obstacle Course): +25 XP  ║
 ║     🎮 Activity 2 (Health Check): +25 XP     ║
 ║     🎮 Activity 3 (Folder Build): +25 XP     ║
 ║     ⚡ Quiz: up to +60 XP                    ║
 ║     ⭐ Bonus: cowsay install: +15 XP         ║
 ║     ─────────────────────                    ║
 ║     💰 TOTAL: up to 200 XP                   ║
 ║                                              ║
 ║     Running Total: up to 570 XP              ║
 ║     Level: 🔧 Pi Tinkerer!                   ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Module 1 Quiz!** 📝

Test everything you've learned about Raspberry Pi, setup, and Linux commands.
Score 80% or higher to earn the **📝 Quiz Ace 1** badge!

Then it's on to **Module 2: GPIO & Electronics** where the REAL fun begins —
you'll make LEDs light up with code! 💡⚡

---

### 📋 Linux Command Cheat Sheet (Keep This!)

```
┌─────────────────────────────────────────────────────────┐
│              🐧 LINUX COMMAND CHEAT SHEET               │
├──────────────┬──────────────────────────────────────────┤
│ Command      │ What It Does                             │
├──────────────┼──────────────────────────────────────────┤
│ pwd          │ Print where you are                      │
│ ls           │ List files and folders                   │
│ ls -la       │ List ALL files with details              │
│ cd [folder]  │ Go to a folder                           │
│ cd ..        │ Go back one level                        │
│ cd ~         │ Go to home folder                        │
│ mkdir [name] │ Create a new folder                      │
│ touch [name] │ Create a new empty file                  │
│ nano [file]  │ Edit a file                              │
│ cat [file]   │ Display file contents                    │
│ cp [a] [b]   │ Copy file a to b                         │
│ mv [a] [b]   │ Move or rename file                      │
│ rm [file]    │ Delete a file (CAREFUL!)                 │
│ rm -r [dir]  │ Delete a folder (CAREFUL!)               │
│ clear        │ Clear the screen                         │
│ sudo         │ Run as admin (Super User)                │
│ apt update   │ Check for software updates               │
│ apt upgrade  │ Install software updates                 │
│ apt install  │ Install new software                     │
│ shutdown     │ Shut down the Pi                         │
├──────────────┼──────────────────────────────────────────┤
│ PI-SPECIFIC: │                                          │
│ vcgencmd     │ Check Pi hardware info                   │
│ measure_temp │ Check CPU temperature                    │
│ hostname -I  │ Show IP address                          │
│ free -h      │ Show memory usage                        │
│ df -h        │ Show disk space                          │
│ htop         │ Show running processes                   │
└──────────────┴──────────────────────────────────────────┘
```

---

*You're becoming a real computer wizard! Keep going, future inventor!* ⭐

---

## Navigation

| | |
|:---|---:|
| [← 🎮 Raspberry Pi Explorer — Module 1, Lesson 2: Setting Up Your Pi! 💻](lesson_02_setting_up.md) | [Module Overview →](README.md) |
