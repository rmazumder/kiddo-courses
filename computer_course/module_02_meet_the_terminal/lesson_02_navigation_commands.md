# 🗺️ Command Quest — Module 2, Lesson 2: Navigation Commands

## 🌟 Your Mission Today

Explorer, it's time to learn how to MOVE around your computer using the terminal! 🧭 You'll master three essential navigation commands that will let you explore your file system like a pro. Think of it as learning to walk before you run — these commands are the foundation of everything else!

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `pwd` to find out where you are
- ✅ Use `ls` to see what's around you
- ✅ Use `cd` to move to different folders
- ✅ Navigate confidently through the file system using the terminal

---

## 🪝 Hook: Lost in a Dark Forest

Imagine you're dropped into a huge, dark forest. 🌲 You can't see anything. You have three magical tools:

1. 🧭 **A compass** that tells you EXACTLY where you are (that's `pwd`)
2. 🔦 **A flashlight** that shows everything around you (that's `ls`)
3. 🥾 **Magic boots** that teleport you to any location (that's `cd`)

With just these three tools, you can explore the ENTIRE forest! And with `pwd`, `ls`, and `cd`, you can explore your ENTIRE computer! Let's learn how! 🚀

---

## 🧠 Command 1: `pwd` — "Where Am I?" 🧭

### What it stands for: **P**rint **W**orking **D**irectory

### What it does:
Shows you the **full path** of the folder you're currently in. It's your GPS!

### Try it now:
```bash
pwd
```

### What you'll see:
```
/home/alex
```
or on Mac:
```
/Users/alex
```

This means you're in your **home directory** — your personal folder!

> 🎮 **Analogy:** `pwd` is like asking your GPS "Where am I right now?" It gives you the complete address.

### Why it's useful:
When you start moving around folders, it's easy to get "lost." `pwd` always tells you exactly where you are. Use it whenever you feel confused!

> 💡 **Pro Tip:** Whenever you feel lost in the terminal, type `pwd` to get your bearings!

---

## 🧠 Command 2: `ls` — "What's Here?" 🔦

### What it stands for: **L**i**s**t

### What it does:
Shows you all the files and folders in your current location.

### Try it now:
```bash
ls
```

### What you'll see (something like):
```
Desktop    Documents    Downloads    Music    Pictures    Videos
```

Those are the folders inside your home directory!

> 🎮 **Analogy:** `ls` is like shining a flashlight in a dark room — suddenly you can see everything that's in there!

### Supercharged `ls` — Useful Options:

| Command | What It Does | Remember It As |
|---------|-------------|----------------|
| `ls` | Lists files and folders | "What's here?" |
| `ls -l` | Shows detailed info (size, date, permissions) | "Tell me MORE about what's here" |
| `ls -a` | Shows ALL files, including hidden ones (start with `.`) | "Show me EVERYTHING, even secrets!" |
| `ls -la` | Combines both — detailed view of ALL files | "Show me EVERYTHING in detail!" |
| `ls Documents` | Lists what's inside the Documents folder | "What's in Documents?" |

### Example of `ls -l` output:
```
drwxr-xr-x  5 alex  staff  160  Jan 15 10:30 Documents
drwxr-xr-x  3 alex  staff   96  Jan 14 09:00 Downloads
-rw-r--r--  1 alex  staff  245  Jan 15 11:00 notes.txt
```

Let's decode one line:

| Part | Meaning |
|------|---------|
| `d` | It's a **d**irectory (folder). A `-` here means it's a file. |
| `rwxr-xr-x` | Permissions (who can read/write/run it) — more on this later! |
| `alex` | The owner of this file |
| `160` | Size in bytes |
| `Jan 15 10:30` | When it was last modified |
| `Documents` | The name |

### Hidden Files:
Files that start with a dot (`.`) are **hidden**. They don't show up with regular `ls`!

```bash
ls -a
```
```
.  ..  .bashrc  .profile  Documents  Downloads  notes.txt
```

Remember `.` means "current directory" and `..` means "parent directory" — they show up here too!

---

## 🧠 Command 3: `cd` — "Take Me There!" 🥾

### What it stands for: **C**hange **D**irectory

### What it does:
Moves you to a different folder. It's your teleporter!

### Basic Usage:

```bash
cd Documents
```

This moves you INTO the Documents folder. Check with `pwd`:
```bash
pwd
```
```
/home/alex/Documents
```

You moved! 🎉

> 🎮 **Analogy:** `cd` is like walking through a door into another room. Each folder is a room, and `cd` opens the door!

### Essential `cd` Moves:

| Command | Where It Takes You | Remember It As |
|---------|-------------------|----------------|
| `cd Documents` | Into the Documents folder | "Go into Documents" |
| `cd ..` | Up one level (parent folder) | "Go back / go up" |
| `cd ~` | Home directory (no matter where you are) | "Go home!" |
| `cd /` | Root directory (very top) | "Go to the top of the tree" |
| `cd ../..` | Up two levels | "Go up twice" |
| `cd -` | Back to where you were before | "Undo my last move" |

### Step-by-Step Navigation Example:

Let's go on a journey! Type each command and see what happens:

```bash
# Step 1: Check where you are
pwd
# Output: /home/alex

# Step 2: See what's here
ls
# Output: Desktop  Documents  Downloads  Music  Pictures

# Step 3: Go into Documents
cd Documents

# Step 4: Confirm you moved
pwd
# Output: /home/alex/Documents

# Step 5: See what's in Documents
ls
# Output: homework.txt  projects  school

# Step 6: Go into the school folder
cd school

# Step 7: Where are we now?
pwd
# Output: /home/alex/Documents/school

# Step 8: Go back up one level
cd ..

# Step 9: Check where we are
pwd
# Output: /home/alex/Documents

# Step 10: Go all the way home!
cd ~

# Step 11: Confirm
pwd
# Output: /home/alex
```

### ⚠️ Common Mistakes (and How to Fix Them):

| Mistake | Error Message | Fix |
|---------|--------------|-----|
| `cd documents` (wrong case) | `No such file or directory` | Capital D: `cd Documents` |
| `cd My Documents` (space in name) | Thinks "My" and "Documents" are separate | Use quotes: `cd "My Documents"` or backslash: `cd My\ Documents` |
| `cd folder_that_doesnt_exist` | `No such file or directory` | Use `ls` first to see what folders exist! |

> 💡 **Pro Tip:** Remember the **Tab** key! Start typing a folder name and press Tab — the terminal will auto-complete it for you. This also avoids typos!

---

## 🧠 The Navigation Combo: pwd + ls + cd

The real power comes from combining these three commands:

```
1. pwd  →  "Where am I?"
2. ls   →  "What's here?"
3. cd   →  "Move there!"
4. Repeat!
```

This is the basic rhythm of navigating in the terminal. It becomes second nature with practice!

```
🧭 pwd → 🔦 ls → 🥾 cd → 🧭 pwd → 🔦 ls → 🥾 cd → ...
```

---

## 🎮 Activity 1: Terminal Explorer Challenge! (⭐ 25 XP)

**Instructions:** Open your terminal and complete this navigation quest! Write down what you see at each step.

| Step | Command | What did you see? |
|------|---------|------------------|
| 1 | `pwd` | ??? |
| 2 | `ls` | ??? |
| 3 | `cd Documents` (or another folder you see) | ??? |
| 4 | `pwd` | ??? |
| 5 | `ls` | ??? |
| 6 | `cd ..` | ??? |
| 7 | `pwd` | ??? |
| 8 | `cd /` | ??? |
| 9 | `ls` | ??? |
| 10 | `cd ~` | ??? |

**Scoring:**
- Completed all 10 steps = ⭐ 25 XP
- Completed 5-9 steps = ⭐ 15 XP
- Completed 1-4 steps = ⭐ 10 XP

---

## 🎮 Activity 2: Navigation Translator! (⭐ 20 XP)

**Instructions:** Convert each English instruction into the correct terminal command.

| # | English | Terminal Command |
|---|---------|-----------------|
| 1 | "Where am I right now?" | ??? |
| 2 | "Show me everything in this folder, including hidden files" | ??? |
| 3 | "Go into the Pictures folder" | ??? |
| 4 | "Go back up one folder level" | ??? |
| 5 | "Take me home!" | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `pwd`
2. `ls -a`
3. `cd Pictures`
4. `cd ..`
5. `cd ~`

**Scoring:** Each correct answer = ⭐ 4 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 3: Where Am I? Puzzle! (⭐ 15 XP)

**Instructions:** For each scenario, figure out what `pwd` would show after running the commands.

**Starting location:** `/home/alex`

**Scenario 1:**
```bash
cd Documents
cd school
pwd
```
Answer: ???

**Scenario 2:**
```bash
cd Documents
cd ..
cd Pictures
pwd
```
Answer: ???

**Scenario 3:**
```bash
cd /
cd home
cd alex
cd Music
cd ..
cd Downloads
pwd
```
Answer: ???

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `/home/alex/Documents/school`
2. `/home/alex/Pictures`
3. `/home/alex/Downloads`

**Explanation for Scenario 3:**
- Start: `/home/alex`
- `cd /` → go to root: `/`
- `cd home` → `/home`
- `cd alex` → `/home/alex`
- `cd Music` → `/home/alex/Music`
- `cd ..` → up one level: `/home/alex`
- `cd Downloads` → `/home/alex/Downloads`

**Scoring:** Each correct answer = ⭐ 5 XP (Total: 15 XP)

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
What does `pwd` stand for?

- A) Password
- B) Print Working Directory
- C) Present Working Data
- D) Program Window Display

### Question 2:
What does `ls -a` do that regular `ls` doesn't?

- A) Lists files in alphabetical order
- B) Shows hidden files (files starting with `.`)
- C) Lists files in other folders
- D) Adds colors to the output

### Question 3:
If you are in `/home/alex/Documents/school` and type `cd ../..`, where do you end up?

- A) `/home/alex/Documents`
- B) `/home/alex`
- C) `/home`
- D) `/`

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **B) Print Working Directory** — It prints the full path of where you are.
2. **B) Shows hidden files** — Files starting with `.` are hidden by default!
3. **B) `/home/alex`** — `..` goes up once to `Documents`, `../..` goes up twice to `alex`!

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 You can navigate like a pro!

You now have your three essential navigation tools:

- 🧭 `pwd` — Find out where you are
- 🔦 `ls` — See what's around you
- 🥾 `cd` — Move to a new location

These three commands will be used in almost EVERY terminal session for the rest of your life. They're the foundation of everything!

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 150 XP |
| Activity XP (max) | ⭐ 60 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 240 XP** |

---

## 🔍 Coming Up Next...

In **Lesson 3: File Commands**, you'll learn how to CREATE, COPY, MOVE, and DELETE files and folders using the terminal. You're going to become a file management wizard! 📁✨

**[Next Lesson: File Commands →](lesson_03_file_commands.md)**
