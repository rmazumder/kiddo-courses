# ⚡ Command Quest — Module 4, Lesson 1: Pipes and Redirects

## 🌟 Your Mission Today

Welcome to the POWER module, Explorer! 🔥 Today you're going to learn one of the coolest tricks in the terminal — connecting commands together like LEGO blocks! With **pipes** and **redirects**, you can take the output of one command and feed it into another, or save it to a file. This is where you level up from "user" to "power user!"

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `>` and `>>` to redirect output to files
- ✅ Use `|` (pipes) to connect commands together
- ✅ Combine commands to do powerful multi-step operations
- ✅ Use `wc` to count words and lines
- ✅ Use `sort` to sort data

---

## 🪝 Hook: The Assembly Line

Imagine a chocolate factory. 🍫 Instead of one person doing EVERYTHING (mixing, molding, wrapping, boxing), there's an **assembly line**:

```
🥛 Mix ingredients → 🍫 Pour into molds → 📦 Wrap bars → 🎁 Pack into boxes
```

Each worker does ONE thing and passes the result to the next worker.

**That's exactly how pipes work in the terminal!** Each command does one thing, then passes its output to the next command. Simple commands become incredibly powerful when chained together!

---

## 🧠 Setting Up: Create Practice Files

```bash
# Go to practice area
cd ~/command_quest_practice
mkdir -p power_user
cd power_user

# Create a list of animals
echo "zebra" > animals.txt
echo "elephant" >> animals.txt
echo "ant" >> animals.txt
echo "dog" >> animals.txt
echo "cat" >> animals.txt
echo "bear" >> animals.txt
echo "eagle" >> animals.txt
echo "ant" >> animals.txt
echo "fish" >> animals.txt
echo "dog" >> animals.txt

# Create a list of scores
echo "Alice:95" > scores.txt
echo "Bob:72" >> scores.txt
echo "Charlie:88" >> scores.txt
echo "Diana:91" >> scores.txt
echo "Eve:85" >> scores.txt
echo "Frank:72" >> scores.txt
echo "Grace:99" >> scores.txt
```

---

## 🧠 Learning Point 1: Output Redirection with `>` and `>>`

Normally, when you run a command, the output appears on your screen. But what if you want to **save** that output to a file instead?

### `>` — Write to a File (Overwrites!)

The `>` symbol takes the output of a command and writes it to a file. If the file already exists, it **replaces** everything in it!

```bash
echo "Hello, World!" > greeting.txt
```

This creates `greeting.txt` containing "Hello, World!" — nothing appears on screen because it went to the file instead!

```bash
cat greeting.txt
```
```
Hello, World!
```

### ⚠️ Be Careful with `>`!

```bash
echo "Goodbye!" > greeting.txt
cat greeting.txt
```
```
Goodbye!
```

"Hello, World!" is GONE. `>` overwrites the entire file!

### `>>` — Append to a File (Adds to the End!)

The `>>` symbol ADDS to the end of a file without erasing what's already there.

```bash
echo "Line 1" > diary.txt
echo "Line 2" >> diary.txt
echo "Line 3" >> diary.txt
cat diary.txt
```
```
Line 1
Line 2
Line 3
```

> 🔑 **Key Idea:**
> - `>` = **Overwrite** (replaces everything — destructive!)
> - `>>` = **Append** (adds to the end — safe!)

> 🎮 **Analogy:**
> - `>` is like erasing a whiteboard and writing something new
> - `>>` is like adding a new line at the bottom of the whiteboard

### Save Command Output to Files:

You can redirect the output of ANY command!

```bash
# Save the current date to a file
date > today.txt

# Save a directory listing to a file
ls -la > file_list.txt

# Save your username to a file
whoami >> diary.txt
```

---

## 🧠 Learning Point 2: The Pipe `|` — Connect Commands! 🔗

### What it is:
The **pipe** symbol `|` (a vertical bar, usually found above the Enter key on your keyboard — press Shift + Backslash `\`) takes the OUTPUT of one command and feeds it as INPUT to the next command.

### Syntax:
```bash
command1 | command2
```

The output of `command1` gets "piped" directly into `command2`!

> 🎮 **Analogy:** A pipe is like a conveyor belt in a factory. The first machine creates something, and the conveyor belt (pipe) carries it to the next machine for more work!

### Example 1: Sort a File and Display It

```bash
cat animals.txt | sort
```
```
ant
ant
bear
cat
dog
dog
eagle
elephant
fish
zebra
```

What happened? `cat` printed the file contents, but instead of going to the screen, the pipe sent them to `sort`, which arranged them alphabetically!

### Example 2: Find Unique Lines

```bash
cat animals.txt | sort | uniq
```
```
ant
bear
cat
dog
eagle
elephant
fish
zebra
```

Now there are no duplicates! We piped through TWO commands: first `sort` (to put duplicates next to each other), then `uniq` (to remove duplicate lines).

### Example 3: Count the Unique Animals

```bash
cat animals.txt | sort | uniq | wc -l
```
```
8
```

There are 8 unique animals! We added `wc -l` (word count — count lines) at the end.

---

## 🧠 Learning Point 3: Useful Commands to Use with Pipes

### `sort` — Sort Lines Alphabetically

```bash
sort animals.txt
```

Sort also has useful options:
| Flag | What It Does |
|------|-------------|
| `sort` | Sort alphabetically (A→Z) |
| `sort -r` | Sort in reverse (Z→A) |
| `sort -n` | Sort numerically (1, 2, 10 — not 1, 10, 2) |

### `uniq` — Remove Duplicate Lines

```bash
sort animals.txt | uniq
```

> ⚠️ **Important:** `uniq` only removes ADJACENT duplicates. Always `sort` first!

| Flag | What It Does |
|------|-------------|
| `uniq` | Remove duplicate lines |
| `uniq -c` | Count how many times each line appears |

```bash
sort animals.txt | uniq -c
```
```
      2 ant
      1 bear
      1 cat
      2 dog
      1 eagle
      1 elephant
      1 fish
      1 zebra
```

### `wc` — Count Words, Lines, Characters

```bash
wc animals.txt
```
```
 10  10  56 animals.txt
```

This means: **10 lines, 10 words, 56 characters**

| Flag | What It Does |
|------|-------------|
| `wc -l` | Count lines only |
| `wc -w` | Count words only |
| `wc -c` | Count characters only |

### `sort` + `grep` Combo:
```bash
grep "dog" animals.txt | wc -l
```
```
2
```

"How many lines contain 'dog'?" — Answer: 2!

---

## 🧠 Learning Point 4: Powerful Pipe Chains

The REAL power comes from chaining multiple commands. Here are some amazing examples:

### Example: "What are the top 3 animals alphabetically?"
```bash
sort animals.txt | uniq | head -n 3
```
```
ant
bear
cat
```

### Example: "How many files are in my home directory?"
```bash
ls ~ | wc -l
```

### Example: "Which lines in scores.txt contain a score above 90?"
```bash
grep "9[0-9]\|100" scores.txt
```
```
Alice:95
Diana:91
Grace:99
```

### Example: "Save a sorted, unique list of animals to a new file"
```bash
sort animals.txt | uniq > sorted_animals.txt
cat sorted_animals.txt
```
```
ant
bear
cat
dog
eagle
elephant
fish
zebra
```

You can combine pipes AND redirects! The pipe processes the data, and `>` saves the final result!

---

## 🧠 Quick Reference: Pipes and Redirects

```
╔══════════════════════════════════════════════════════════╗
║          📋 PIPES & REDIRECTS CHEAT SHEET                ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  REDIRECTS:                                              ║
║  command > file.txt     Write output to file (overwrite) ║
║  command >> file.txt    Append output to file             ║
║                                                          ║
║  PIPES:                                                  ║
║  cmd1 | cmd2            Send cmd1 output to cmd2          ║
║  cmd1 | cmd2 | cmd3     Chain multiple commands           ║
║                                                          ║
║  USEFUL COMBO COMMANDS:                                  ║
║  sort                   Sort lines alphabetically         ║
║  sort -r                Sort in reverse                   ║
║  uniq                   Remove duplicate lines            ║
║  uniq -c                Count duplicates                  ║
║  wc -l                  Count lines                       ║
║  wc -w                  Count words                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎮 Activity 1: Pipe Builder Challenge! (⭐ 30 XP)

**Instructions:** Build the correct pipe chain to answer each question. Use the `animals.txt` and `scores.txt` files.

| # | Question | Your Command |
|---|----------|-------------|
| 1 | Sort the animals in reverse alphabetical order | ??? |
| 2 | How many TOTAL lines are in animals.txt? | ??? |
| 3 | List the unique animals and count how many times each appears | ??? |
| 4 | Sort the scores file and save the result to `sorted_scores.txt` | ??? |
| 5 | How many unique animals are there? | ??? |
| 6 | Show only the first 3 animals after sorting alphabetically | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `sort -r animals.txt`
2. `wc -l animals.txt` or `cat animals.txt | wc -l`
3. `sort animals.txt | uniq -c`
4. `sort scores.txt > sorted_scores.txt`
5. `sort animals.txt | uniq | wc -l`
6. `sort animals.txt | head -n 3`

**Scoring:** Each correct = ⭐ 5 XP (Total: 30 XP)

</details>

---

## 🎮 Activity 2: Redirect Challenge! (⭐ 20 XP)

**Instructions:** Complete each task using `>` or `>>`.

| # | Task | Your Command |
|---|------|-------------|
| 1 | Save the text "My Adventure Log" to a new file called `log.txt` | ??? |
| 2 | Add the current date to `log.txt` (without erasing the title!) | ??? |
| 3 | Add the text "Chapter 1: The Beginning" to `log.txt` | ??? |
| 4 | View the contents of `log.txt` | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `echo "My Adventure Log" > log.txt`
2. `date >> log.txt`
3. `echo "Chapter 1: The Beginning" >> log.txt`
4. `cat log.txt`

Your `log.txt` should look something like:
```
My Adventure Log
Fri Jan 17 14:30:00 EST 2025
Chapter 1: The Beginning
```

**Scoring:** Each correct = ⭐ 5 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 3: Pipe Puzzle! (⭐ 15 XP)

**Instructions:** Figure out what each pipe chain produces WITHOUT running it. Then verify by running it!

**Puzzle 1:**
```bash
echo "hello world" | wc -w
```
What does this output? ???

**Puzzle 2:**
```bash
cat animals.txt | grep "a" | wc -l
```
What does this output? ???

**Puzzle 3:**
```bash
cat animals.txt | sort | tail -n 1
```
What does this output? ???

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `2` — "hello world" has 2 words
2. `5` — Lines containing "a": bear, cat, eagle, ant, ant = 5 lines
3. `zebra` — After sorting alphabetically, the last animal is "zebra"

**Scoring:** Each correct = ⭐ 5 XP (Total: 15 XP)

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
What's the difference between `>` and `>>`?

- A) `>` is faster
- B) `>` overwrites the file, `>>` appends to the end
- C) `>>` overwrites the file, `>` appends
- D) They do the same thing

### Question 2:
What does the pipe symbol `|` do?

- A) Saves output to a file
- B) Deletes the output
- C) Sends the output of one command as input to the next command
- D) Pauses the command

### Question 3:
What does `cat file.txt | sort | uniq | wc -l` do?

- A) Deletes duplicate lines in the file
- B) Counts the number of unique lines in the file
- C) Sorts the file and saves it
- D) Prints the file backwards

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **B) `>` overwrites, `>>` appends** — Be careful with `>` — it erases first!
2. **C) Sends output to the next command** — Like a conveyor belt!
3. **B) Counts unique lines** — It reads, sorts, removes duplicates, then counts!

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 You're now a Power User!

You've learned three game-changing concepts:
- ➡️ `>` and `>>` — Redirect output to files
- 🔗 `|` — Pipe commands together
- 🛠️ `sort`, `uniq`, `wc` — Powerful data processing tools

These skills separate beginners from power users. You're well on your way to becoming a Command Wizard!

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 200 XP |
| Activity XP (max) | ⭐ 65 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 295 XP** |

---

## 🔍 Coming Up Next...

In **Lesson 2: Text Editing**, you'll learn to edit files directly in the terminal using text editors like `nano`! No more just viewing files — now you'll change them! 📝

**[Next Lesson: Text Editing →](lesson_02_text_editing.md)**

---

## Navigation

| | |
|:---|---:|
| [← Module Overview](README.md) | [📝 Command Quest — Module 4, Lesson 2: Text Editing in the Terminal →](lesson_02_text_editing.md) |
