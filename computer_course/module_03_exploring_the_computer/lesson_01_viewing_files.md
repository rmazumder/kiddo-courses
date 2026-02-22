# 🔍 Command Quest — Module 3, Lesson 1: Viewing Files

## 🌟 Your Mission Today

Detective, it's time to learn how to **peek inside files** without opening a whole application! 🕵️ The terminal has several powerful commands for reading files — from seeing everything at once to peeking at just the first or last few lines. By the end of this lesson, you'll be able to read any file right from the command line!

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ View the entire contents of a file with `cat`
- ✅ Browse through long files with `less`
- ✅ Peek at the beginning of a file with `head`
- ✅ Peek at the end of a file with `tail`
- ✅ Know which command to use and when

---

## 🪝 Hook: The Newspaper Dilemma

Imagine you get a 500-page newspaper. 📰 Sometimes you want to:

1. **Read the whole thing** — sit down and read every page (`cat`)
2. **Browse through it** — flip through page by page (`less`)
3. **Read just the headlines** — check the front page only (`head`)
4. **Check the sports scores** — skip to the last page (`tail`)

You wouldn't read all 500 pages just to check the sports score, right? The terminal gives you tools for each situation!

---

## 🧠 Setting Up: Create Practice Files

Let's create some files to practice with! Open your terminal and type:

```bash
# Go to your practice area
cd ~/command_quest_practice

# Create a practice folder for this lesson
mkdir -p detective_files
cd detective_files

# Create a file with some content using echo
echo "Line 1: The treasure is hidden" > clues.txt
echo "Line 2: Look under the old oak tree" >> clues.txt
echo "Line 3: Dig three feet down" >> clues.txt
echo "Line 4: Watch out for the guard dog" >> clues.txt
echo "Line 5: The password is 'opensesame'" >> clues.txt
echo "Line 6: The treasure chest is red" >> clues.txt
echo "Line 7: Inside you will find gold coins" >> clues.txt
echo "Line 8: And a mysterious map" >> clues.txt
echo "Line 9: The map leads to another treasure" >> clues.txt
echo "Line 10: But that's a quest for another day" >> clues.txt
```

> 📝 **Note:** The `>` symbol creates a new file and writes to it. The `>>` symbol ADDS to an existing file. You'll learn more about these in Module 4!

Now let's create a longer file:

```bash
# Create a longer story file
for i in {1..50}; do echo "Line $i: This is line number $i of the story." >> long_story.txt; done
```

This creates a file with 50 lines! (Don't worry about the `for` loop — you'll learn about that later!)

---

## 🧠 Command 1: `cat` — See Everything! 📖

### What it stands for: Con**cat**enate (meaning "link together")

### What it does:
Prints the ENTIRE contents of a file to the screen.

### Basic Usage:
```bash
cat clues.txt
```

### Output:
```
Line 1: The treasure is hidden
Line 2: Look under the old oak tree
Line 3: Dig three feet down
Line 4: Watch out for the guard dog
Line 5: The password is 'opensesame'
Line 6: The treasure chest is red
Line 7: Inside you will find gold coins
Line 8: And a mysterious map
Line 9: The map leads to another treasure
Line 10: But that's a quest for another day
```

Everything in the file appears on your screen!

### Show Line Numbers:
```bash
cat -n clues.txt
```

```
     1  Line 1: The treasure is hidden
     2  Line 2: Look under the old oak tree
     3  Line 3: Dig three feet down
     ...
```

The `-n` flag adds line numbers — super useful for long files!

### View Multiple Files:
```bash
cat clues.txt long_story.txt
```

This shows both files, one after the other. That's the "concatenate" part — linking files together!

### When to Use `cat`:
- ✅ Short files (under 50 lines)
- ✅ When you need to see everything at once
- ❌ NOT great for very long files (the text scrolls by too fast!)

> 🎮 **Analogy:** `cat` is like dumping a box of letters on a table — you see everything at once. Great for a small box, overwhelming for a huge one!

---

## 🧠 Command 2: `less` — Browse Page by Page! 📚

### What it does:
Opens a file in a scrollable viewer. You can move up and down through the file at your own pace.

### Basic Usage:
```bash
less long_story.txt
```

Your terminal transforms into a file viewer! The file doesn't just scroll by — you CONTROL the navigation.

### Navigation Keys Inside `less`:

| Key | What It Does |
|-----|-------------|
| `Space` or `f` | Next page (forward) |
| `b` | Previous page (back) |
| `↓` or `j` | Down one line |
| `↑` or `k` | Up one line |
| `g` | Jump to the BEGINNING of the file |
| `G` (Shift+g) | Jump to the END of the file |
| `/searchword` | Search for text (type `/` then the word) |
| `n` | Jump to NEXT search result |
| `q` | QUIT and go back to the terminal |

### Example: Searching in `less`:
```bash
less long_story.txt
```
Then type:
```
/line 25
```
It jumps right to where "line 25" appears! Press `n` to find the next occurrence.

> ⚠️ **Important:** Press `q` to quit! If you feel "stuck" in `less`, just press `q` and you're back to normal.

### When to Use `less`:
- ✅ Long files (more than one screen of text)
- ✅ When you want to search within a file
- ✅ When you want to browse at your own pace

> 🎮 **Analogy:** `less` is like opening a book — you can flip forward, flip backward, jump to any page, and search for a word. When you're done, you close the book (`q`)!

### Fun Fact:
There's also a command called `more` (the original pager), but `less` is better. Programmers joke: "Less is more!" 😄

---

## 🧠 Command 3: `head` — Peek at the Top! 🎩

### What it does:
Shows only the FIRST few lines of a file. By default, it shows the first 10 lines.

### Basic Usage:
```bash
head long_story.txt
```

### Output (first 10 lines):
```
Line 1: This is line number 1 of the story.
Line 2: This is line number 2 of the story.
Line 3: This is line number 3 of the story.
...
Line 10: This is line number 10 of the story.
```

### Show a Specific Number of Lines:
```bash
head -n 3 clues.txt
```

```
Line 1: The treasure is hidden
Line 2: Look under the old oak tree
Line 3: Dig three feet down
```

The `-n 3` means "show me only the first 3 lines!"

### When to Use `head`:
- ✅ When you just want a quick preview of a file
- ✅ Checking what format a file is in
- ✅ Looking at the beginning of log files

> 🎮 **Analogy:** `head` is like reading the first page of a book to see if you're interested!

---

## 🧠 Command 4: `tail` — Peek at the Bottom! 🦚

### What it does:
Shows only the LAST few lines of a file. By default, it shows the last 10 lines.

### Basic Usage:
```bash
tail long_story.txt
```

### Output (last 10 lines):
```
Line 41: This is line number 41 of the story.
Line 42: This is line number 42 of the story.
...
Line 50: This is line number 50 of the story.
```

### Show a Specific Number of Lines:
```bash
tail -n 3 clues.txt
```

```
Line 8: And a mysterious map
Line 9: The map leads to another treasure
Line 10: But that's a quest for another day
```

### When to Use `tail`:
- ✅ Checking the end of a file
- ✅ Looking at the most recent entries in a log file
- ✅ Seeing the last few lines of any file

> 🎮 **Analogy:** `tail` is like flipping to the last page of a book to see how the story ends!

---

## 🧠 Quick Comparison: When to Use Each Command

```
╔═══════════════════════════════════════════════════════════╗
║          📋 FILE VIEWING CHEAT SHEET                      ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  cat file.txt         Show entire file at once            ║
║  cat -n file.txt      Show file with line numbers         ║
║  less file.txt        Browse file page by page (q=quit)   ║
║  head file.txt        Show first 10 lines                 ║
║  head -n 5 file.txt   Show first 5 lines                  ║
║  tail file.txt        Show last 10 lines                  ║
║  tail -n 5 file.txt   Show last 5 lines                   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

| Situation | Best Command |
|-----------|-------------|
| Short file, want to see everything | `cat` |
| Long file, want to browse | `less` |
| Just want to see the start | `head` |
| Just want to see the end | `tail` |
| Need line numbers | `cat -n` |
| Need to search inside a file | `less` (then `/searchword`) |

---

## 🎮 Activity 1: Detective Reading Challenge! (⭐ 25 XP)

**Instructions:** Use the practice files you created. Run each command and write down what you see.

| # | Command | What Did You See? |
|---|---------|------------------|
| 1 | `cat clues.txt` | ??? |
| 2 | `head -n 2 clues.txt` | ??? |
| 3 | `tail -n 3 clues.txt` | ??? |
| 4 | `cat -n clues.txt` | ??? |
| 5 | `head -n 1 long_story.txt` | ??? |

**Scoring:**
- All 5 completed = ⭐ 25 XP
- 3-4 completed = ⭐ 15 XP

---

## 🎮 Activity 2: Choose Your Weapon! (⭐ 20 XP)

**Instructions:** For each scenario, choose the BEST command to use.

| # | Scenario | Best Command? |
|---|----------|---------------|
| 1 | You want to quickly check what's inside a short config file (5 lines) | `cat` / `less` / `head` / `tail` |
| 2 | You have a 10,000-line log file and want to search for the word "error" | `cat` / `less` / `head` / `tail` |
| 3 | You want to see the most recent 5 entries in a log file | `cat` / `less` / `head` / `tail` |
| 4 | You want to preview what type of data is in a file by looking at the first few lines | `cat` / `less` / `head` / `tail` |
| 5 | You want to see a file with line numbers | `cat -n` / `less` / `head` / `tail` |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. **`cat`** — Short file, just dump it all to the screen!
2. **`less`** — Long file + searching = `less` is perfect (use `/error` to search)
3. **`tail -n 5`** — The last 5 lines = the most recent entries
4. **`head`** — Just peek at the beginning
5. **`cat -n`** — The `-n` flag adds line numbers

**Scoring:** Each correct = ⭐ 4 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 3: Less Explorer Challenge! (⭐ 15 XP)

**Instructions:** Open the long story file with `less`:

```bash
less long_story.txt
```

Now complete these challenges:

| # | Challenge | How? |
|---|-----------|------|
| 1 | Jump to the end of the file | Press ??? |
| 2 | Jump back to the beginning | Press ??? |
| 3 | Search for "line 30" | Type ??? |
| 4 | Go to the next search result | Press ??? |
| 5 | Quit less | Press ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. Press `G` (Shift + g)
2. Press `g`
3. Type `/line 30`
4. Press `n`
5. Press `q`

**Scoring:** Each correct = ⭐ 3 XP (Total: 15 XP)

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
Which command would you use to see the first 5 lines of a file called `data.txt`?

- A) `cat 5 data.txt`
- B) `head -n 5 data.txt`
- C) `tail -n 5 data.txt`
- D) `less -5 data.txt`

### Question 2:
You're inside `less` and want to quit. Which key do you press?

- A) `x`
- B) `Escape`
- C) `q`
- D) `Ctrl + C`

### Question 3:
What does `cat -n file.txt` do differently from `cat file.txt`?

- A) It reverses the file
- B) It counts the words
- C) It adds line numbers to the output
- D) It only shows numbers in the file

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **B) `head -n 5 data.txt`** — `head` shows the beginning, `-n 5` limits it to 5 lines!
2. **C) `q`** — The universal "quit" key in `less`!
3. **C) It adds line numbers** — The `-n` flag numbers each line!

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 You're a File Reading Expert!

You now have four ways to look inside files:

- 📖 `cat` — Dump everything to the screen
- 📚 `less` — Browse page by page with search
- 🎩 `head` — Peek at the beginning
- 🦚 `tail` — Peek at the end

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 150 XP |
| Activity XP (max) | ⭐ 60 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 240 XP** |

---

## 🔍 Coming Up Next...

In **Lesson 2: Finding Things**, you'll learn to use `find` and `grep` — two incredibly powerful commands that let you search for files and text like a super-detective! 🔍🕵️

**[Next Lesson: Finding Things →](lesson_02_finding_things.md)**
