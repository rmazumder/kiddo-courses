# 🕵️ Command Quest — Module 3, Lesson 2: Finding Things

## 🌟 Your Mission Today

Detective, this is the BIG one! 🔍 Today you're going to learn two of the most powerful search commands in the terminal: `find` and `grep`. `find` locates files by name and location. `grep` searches INSIDE files for specific text. Together, they make you an unstoppable data detective!

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `find` to search for files and folders by name
- ✅ Use `grep` to search for text inside files
- ✅ Combine options to create powerful searches
- ✅ Know when to use `find` vs. `grep`

---

## 🪝 Hook: The Library Detective

Imagine you're a detective in the world's biggest library. 📚 You need to solve two types of mysteries:

**Mystery Type 1:** "Where is the book called 'Dragon Adventures'?"
> You need to search by the **title on the spine** (the file name). That's `find`!

**Mystery Type 2:** "Which book contains the word 'treasure' on any page?"
> You need to search by the **words inside the book** (the file contents). That's `grep`!

`find` = searches for file NAMES
`grep` = searches for text INSIDE files

---

## 🧠 Setting Up: Create a Mystery Scene

Let's build a detective scenario to practice with!

```bash
# Go to your practice area
cd ~/command_quest_practice

# Create a mystery scene
mkdir -p mystery/suspects mystery/evidence mystery/evidence/photos
touch mystery/suspects/alice.txt
touch mystery/suspects/bob.txt
touch mystery/suspects/charlie.txt
touch mystery/evidence/fingerprints.txt
touch mystery/evidence/witness_report.txt
touch mystery/evidence/photos/crime_scene.jpg
touch mystery/evidence/photos/suspect_photo.png
touch mystery/secret_diary.txt
touch mystery/clue_note.md

# Add content to some files
echo "Alice was at the park at 3pm. She saw a red car." > mystery/suspects/alice.txt
echo "Bob was at home watching TV. He has a blue car." > mystery/suspects/bob.txt
echo "Charlie was at the store buying groceries. He drives a red truck." > mystery/suspects/charlie.txt
echo "Fingerprints found on the window belong to someone with small hands." > mystery/evidence/fingerprints.txt
echo "A witness saw a red vehicle leave the scene at 3:15pm." > mystery/evidence/witness_report.txt
echo "Dear diary, I saw something suspicious today. A red car was speeding away." > mystery/secret_diary.txt
echo "CLUE: The suspect drives a red vehicle and was seen near the park." > mystery/clue_note.md
```

---

## 🧠 Command 1: `find` — Search for Files! 🔎

### What it does:
Searches for files and folders by their NAME, TYPE, SIZE, or other properties.

### Basic Usage:
```bash
find [where to look] [what to look for]
```

### Example: Find ALL Files in a Folder
```bash
find mystery
```

This lists EVERYTHING inside the `mystery` folder — all files and subfolders:
```
mystery
mystery/suspects
mystery/suspects/alice.txt
mystery/suspects/bob.txt
mystery/suspects/charlie.txt
mystery/evidence
mystery/evidence/fingerprints.txt
mystery/evidence/witness_report.txt
mystery/evidence/photos
mystery/evidence/photos/crime_scene.jpg
mystery/evidence/photos/suspect_photo.png
mystery/secret_diary.txt
mystery/clue_note.md
```

### Find by Name:
```bash
find mystery -name "alice.txt"
```
```
mystery/suspects/alice.txt
```

Found it! 🎉

### Find by Name Pattern (Wildcards):

The `*` character means "anything" — it's a wildcard!

```bash
# Find all .txt files
find mystery -name "*.txt"
```
```
mystery/suspects/alice.txt
mystery/suspects/bob.txt
mystery/suspects/charlie.txt
mystery/evidence/fingerprints.txt
mystery/evidence/witness_report.txt
mystery/secret_diary.txt
```

```bash
# Find all image files (.jpg and .png)
find mystery -name "*.jpg"
find mystery -name "*.png"
```

```bash
# Find files that start with "s"
find mystery -name "s*"
```
```
mystery/suspects
mystery/evidence/photos/suspect_photo.png
mystery/secret_diary.txt
```

### Find by Type:

```bash
# Find only FOLDERS (directories)
find mystery -type d
```
```
mystery
mystery/suspects
mystery/evidence
mystery/evidence/photos
```

```bash
# Find only FILES (not folders)
find mystery -type f
```
This shows only files, not directories!

### `find` Quick Reference:

| Command | What It Does |
|---------|-------------|
| `find . -name "file.txt"` | Find a file by exact name |
| `find . -name "*.txt"` | Find all .txt files |
| `find . -name "report*"` | Find files starting with "report" |
| `find . -type d` | Find only directories (folders) |
| `find . -type f` | Find only files |
| `find . -name "*.txt" -type f` | Find only .txt files (not folders) |

> 📝 **Note:** The `.` means "start searching from the current directory." You can replace it with any path!

> 🎮 **Analogy:** `find` is like a librarian who searches the SHELVES for books. Tell them the title (or part of it), and they'll find where the book is located!

---

## 🧠 Command 2: `grep` — Search INSIDE Files! 🔬

### What it stands for: **G**lobal **R**egular **E**xpression **P**rint

### What it does:
Searches for specific TEXT inside files and shows you which lines contain that text.

### Basic Usage:
```bash
grep "search word" filename
```

### Example: Search for "red" in the suspect files:
```bash
grep "red" mystery/suspects/alice.txt
```
```
Alice was at the park at 3pm. She saw a red car.
```

Found it! Alice's file mentions "red"!

### Search in ALL Files in a Folder:
```bash
grep -r "red" mystery
```

The `-r` flag means **recursive** — search in ALL files in ALL subfolders!

```
mystery/suspects/alice.txt:Alice was at the park at 3pm. She saw a red car.
mystery/suspects/charlie.txt:Charlie was at the store buying groceries. He drives a red truck.
mystery/evidence/witness_report.txt:A witness saw a red vehicle leave the scene at 3:15pm.
mystery/secret_diary.txt:Dear diary, I saw something suspicious today. A red car was speeding away.
mystery/clue_note.md:CLUE: The suspect drives a red vehicle and was seen near the park.
```

Five matches! Every file that contains the word "red" is shown, along with the matching line! 🕵️

### Case-Insensitive Search:
```bash
grep -i "clue" mystery/clue_note.md
```

The `-i` flag ignores case — it finds "CLUE", "clue", "Clue", etc.

### Show Line Numbers:
```bash
grep -n "red" mystery/suspects/alice.txt
```
```
1:Alice was at the park at 3pm. She saw a red car.
```

The `-n` flag shows which LINE NUMBER the match is on!

### Count Matches:
```bash
grep -c "red" mystery/suspects/alice.txt
```
```
1
```

The `-c` flag just counts how many lines contain the match.

### Combine Flags:
```bash
grep -rn "red" mystery
```

This searches recursively (`-r`) AND shows line numbers (`-n`) for every match!

### `grep` Quick Reference:

| Command | What It Does |
|---------|-------------|
| `grep "word" file.txt` | Search for "word" in one file |
| `grep -r "word" folder/` | Search in ALL files in a folder |
| `grep -i "word" file.txt` | Case-insensitive search |
| `grep -n "word" file.txt` | Show line numbers |
| `grep -c "word" file.txt` | Count matching lines |
| `grep -rn "word" folder/` | Recursive + line numbers |
| `grep -ri "word" folder/` | Recursive + case-insensitive |

> 🎮 **Analogy:** If `find` is a librarian who searches the shelves, `grep` is a speed-reader who opens every book and highlights every sentence that contains your search word!

---

## 🧠 `find` vs. `grep` — Know the Difference!

| Feature | `find` | `grep` |
|---------|--------|--------|
| **Searches for** | File/folder NAMES | Text INSIDE files |
| **Question it answers** | "Where is the file called...?" | "Which files contain the word...?" |
| **Analogy** | Looking at book spines on a shelf | Reading pages inside books |

### When to Use Each:

| Situation | Use |
|-----------|-----|
| "Where is my homework file?" | `find . -name "homework*"` |
| "Which files mention pizza?" | `grep -r "pizza" .` |
| "Find all .jpg images" | `find . -name "*.jpg"` |
| "Which config files have my username?" | `grep -r "alex" .` |

---

## 🎮 Activity 1: Solve the Mystery! (⭐ 30 XP)

**Instructions:** Use `find` and `grep` to answer these detective questions about the mystery files you created.

**Question 1:** Find ALL `.txt` files in the mystery folder.
```bash
# Your command here: ???
```

**Question 2:** Which suspect files mention a "car"?
```bash
# Your command here: ???
```

**Question 3:** Find all image files (`.jpg` and `.png`).
```bash
# Your command here: ???
```

**Question 4:** Search ALL mystery files for the word "park".
```bash
# Your command here: ???
```

**Question 5:** Based on the evidence: Who is the most likely suspect?
Hint: Use `grep -r "red" mystery` and `grep -r "park" mystery` to find clues!

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `find mystery -name "*.txt"`
2. `grep -r "car" mystery/suspects/` (Alice and Bob mention cars!)
3. `find mystery -name "*.jpg"` and `find mystery -name "*.png"` (or `find mystery -name "*.jpg" -o -name "*.png"`)
4. `grep -r "park" mystery`
5. **Alice** is the most likely suspect!
   - The clue says the suspect drives a **red vehicle** and was near the **park**
   - Alice **was at the park** and she **saw a red car** (maybe it's HER car!)
   - The witness saw a red vehicle leave at 3:15pm, and Alice was there at 3pm

**Scoring:** Each correct command = ⭐ 5 XP, solving the mystery = ⭐ 5 XP (Total: 30 XP)

</details>

---

## 🎮 Activity 2: Find vs. Grep Challenge! (⭐ 20 XP)

**Instructions:** For each question, decide whether you should use `find` or `grep`, then write the command.

| # | Question | find or grep? | Command |
|---|----------|--------------|---------|
| 1 | "Where is the file called witness_report.txt?" | ??? | ??? |
| 2 | "Which files contain the word 'suspicious'?" | ??? | ??? |
| 3 | "Find all .md files" | ??? | ??? |
| 4 | "Which files mention the time '3pm'?" | ??? | ??? |
| 5 | "Find all folders in the mystery directory" | ??? | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. **find** — `find mystery -name "witness_report.txt"`
2. **grep** — `grep -r "suspicious" mystery`
3. **find** — `find mystery -name "*.md"`
4. **grep** — `grep -r "3pm" mystery`
5. **find** — `find mystery -type d`

**Scoring:** Each fully correct row = ⭐ 4 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 3: Create Your Own Mystery! (⭐ 20 XP)

**Instructions:** Create your own mystery scenario!

1. Make a folder called `my_mystery` inside `command_quest_practice`
2. Create at least 3 "suspect" files with descriptions
3. Create at least 2 "evidence" files with clues
4. Hide a secret word (like "guilty") in exactly ONE suspect file
5. Challenge a friend (or yourself!) to use `find` and `grep` to:
   - Find all the suspect files
   - Search for the secret word
   - Identify the guilty suspect!

> 🌟 **Bonus (+10 XP):** Write down the `find` and `grep` commands someone would need to solve your mystery!

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
What is the main difference between `find` and `grep`?

- A) `find` is faster
- B) `find` searches file NAMES, `grep` searches file CONTENTS
- C) `find` only works on Mac, `grep` only works on Windows
- D) There is no difference

### Question 2:
What does the `-r` flag do in `grep -r "hello" folder/`?

- A) Reverses the search
- B) Searches only the root directory
- C) Searches recursively through all files in all subfolders
- D) Makes the search case-sensitive

### Question 3:
Which command finds all `.py` (Python) files in the current directory and its subfolders?

- A) `grep "*.py" .`
- B) `find . -name "*.py"`
- C) `search . *.py`
- D) `look "*.py"`

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **B) `find` = file names, `grep` = file contents** — Two different types of searching!
2. **C) Searches recursively through all subfolders** — Without `-r`, grep only searches the specified file.
3. **B) `find . -name "*.py"`** — `find` with `-name` and a wildcard pattern!

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 You're now a Data Detective!

You've mastered two incredibly powerful search tools:

- 🔎 `find` — Search for files by name, type, and location
- 🔬 `grep` — Search inside files for specific text

These commands are used by professional developers and system administrators EVERY DAY. You now have skills that most adults don't!

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 150 XP |
| Activity XP (max) | ⭐ 70 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 250 XP** |

---

## 🔍 Coming Up Next...

Take the **[Module 3 Quiz](quiz_03.md)** to earn your Data Detective badge! Then get ready for Module 4 where you'll learn POWER USER skills — piping commands together and editing files right in the terminal! ⚡

**[Next: Module 3 Quiz →](quiz_03.md)**
