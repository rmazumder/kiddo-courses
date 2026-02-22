# 🏆 Command Quest — Module 3 Quiz: Exploring the Computer

## 🌟 Mission: Data Detective Test!

Time to prove you're a master file explorer and searcher! 🕵️ This quiz covers everything from viewing files with `cat`, `less`, `head`, and `tail` to finding things with `find` and `grep`. Score high to earn your **🏅 Data Detective Badge!**

**Total XP Available: ⭐ 75 XP**

---

## 📋 Rules

- There are **15 questions** total
- Each question is worth **⭐ 5 XP**
- Try to answer WITHOUT looking back at the lessons
- You need **11 or more correct** to earn the badge!

---

## Section A: Viewing Files (Questions 1-7)

### ❓ Question 1:
Which command shows the ENTIRE contents of a file on the screen at once?

- A) `less file.txt`
- B) `cat file.txt`
- C) `head file.txt`
- D) `tail file.txt`

### ❓ Question 2:
You have a 5,000-line log file and want to browse through it page by page. Which command should you use?

- A) `cat logfile.txt`
- B) `head logfile.txt`
- C) `less logfile.txt`
- D) `tail logfile.txt`

### ❓ Question 3:
What does `head -n 3 story.txt` display?

- A) The last 3 lines of the file
- B) The first 3 lines of the file
- C) Every 3rd line of the file
- D) 3 random lines from the file

### ❓ Question 4:
How do you quit the `less` viewer?

- A) Press `Escape`
- B) Press `q`
- C) Press `Ctrl + C`
- D) Press `x`

### ❓ Question 5:
Which command shows a file with line numbers?

- A) `cat -n file.txt`
- B) `cat -l file.txt`
- C) `less -n file.txt`
- D) `head -l file.txt`

### ❓ Question 6:
You want to see the last 5 lines of `errors.log`. What command do you use?

- A) `head -n 5 errors.log`
- B) `tail -5 errors.log`
- C) `tail -n 5 errors.log`
- D) `cat -5 errors.log`

### ❓ Question 7:
While inside `less`, you want to search for the word "password." What do you type?

- A) `search password`
- B) `find password`
- C) `/password`
- D) `?password`

---

## Section B: Finding Things (Questions 8-15)

### ❓ Question 8:
What does the `find` command search for?

- A) Text inside files
- B) Files and folders by name, type, or other properties
- C) Websites on the internet
- D) Errors in your code

### ❓ Question 9:
What does `grep` search for?

- A) Files by their name
- B) Folders by their size
- C) Text (words or patterns) inside files
- D) Programs installed on your computer

### ❓ Question 10:
Which command finds all `.jpg` files in the current directory and all subdirectories?

- A) `grep "*.jpg" .`
- B) `find . -name "*.jpg"`
- C) `search . *.jpg`
- D) `ls *.jpg`

### ❓ Question 11:
What does the `-r` flag do when used with `grep`?

- A) Reverses the output
- B) Makes it run faster
- C) Searches recursively through all files in all subfolders
- D) Removes matching lines

### ❓ Question 12:
You want to search for the word "pizza" in ALL files inside a folder called `recipes`. Which command is correct?

- A) `find recipes -name "pizza"`
- B) `grep -r "pizza" recipes`
- C) `cat recipes "pizza"`
- D) `search recipes pizza`

### ❓ Question 13:
What does the `*` wildcard mean in `find . -name "report*"`?

- A) Exactly one character
- B) No characters
- C) Any number of any characters (zero or more)
- D) A star character literally

### ❓ Question 14:
Which command would show how many lines in `data.txt` contain the word "error"?

- A) `grep -n "error" data.txt`
- B) `grep -c "error" data.txt`
- C) `grep -i "error" data.txt`
- D) `grep -r "error" data.txt`

### ❓ Question 15:
You want to find the word "URGENT" in a file, but it might be written as "urgent", "Urgent", or "URGENT". Which `grep` flag helps?

- A) `-r` (recursive)
- B) `-n` (line numbers)
- C) `-c` (count)
- D) `-i` (case-insensitive)

---

## 🔑 Answer Key

<details>
<summary>🔐 Click to reveal all answers!</summary>

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | **B)** `cat` | `cat` dumps the whole file to the screen at once |
| 2 | **C)** `less` | `less` lets you browse long files page by page |
| 3 | **B)** The first 3 lines | `head -n 3` shows the first 3 lines |
| 4 | **B)** Press `q` | `q` for quit — the way out of `less`! |
| 5 | **A)** `cat -n` | The `-n` flag adds line numbers |
| 6 | **C)** `tail -n 5` | `tail` shows the end, `-n 5` limits to 5 lines |
| 7 | **C)** `/password` | In `less`, type `/` then the search word |
| 8 | **B)** Files and folders by name, type, etc. | `find` searches the file system |
| 9 | **C)** Text inside files | `grep` looks for text content |
| 10 | **B)** `find . -name "*.jpg"` | `find` with `-name` and wildcard |
| 11 | **C)** Searches recursively | It goes into all subfolders |
| 12 | **B)** `grep -r "pizza" recipes` | `grep -r` searches recursively for text in files |
| 13 | **C)** Any number of any characters | `*` is a wildcard matching everything |
| 14 | **B)** `grep -c` | `-c` counts the number of matching lines |
| 15 | **D)** `-i` (case-insensitive) | `-i` ignores uppercase/lowercase differences |

</details>

---

## 📊 Score Yourself!

| Score | Rank | XP Earned | Badge? |
|-------|------|-----------|--------|
| 15/15 | 🌟 **Master Detective!** | ⭐ 75 XP + 🌟 BONUS 25 XP | 🏅 YES! |
| 11–14 | ⭐ **Senior Detective!** | ⭐ 55–70 XP | 🏅 YES! |
| 7–10 | 🌿 **Junior Detective** | ⭐ 35–50 XP | ❌ Review & retry! |
| 0–6 | 🌱 **Detective Trainee** | ⭐ 0–30 XP | ❌ Re-read lessons & retry! |

---

## 🏅 Badge Unlock!

If you scored **11 or more correct**, congratulations!

```
╔═══════════════════════════════════════╗
║                                       ║
║     🏅 DATA DETECTIVE BADGE 🏅       ║
║                                       ║
║    You can view files and search      ║
║    like a pro detective!              ║
║                                       ║
║    Module 3: COMPLETE ✅              ║
║                                       ║
╚═══════════════════════════════════════╝
```

---

## ➡️ What's Next?

You're almost at the finish line! In Module 4, you'll learn **power user skills** — piping commands together, redirecting output, and editing files right in the terminal. You're about to become a true Command Wizard! 🧙‍♂️

**[Start Module 4: Power User Skills →](../module_04_power_user_skills/lesson_01_pipes_and_redirects.md)**
