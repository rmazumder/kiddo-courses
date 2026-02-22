# 📁 Command Quest — Module 2, Lesson 3: File Commands

## 🌟 Your Mission Today

Now that you can navigate like a GPS expert, it's time to learn the REAL magic — creating, copying, moving, and deleting files and folders with nothing but typed commands! 🪄 By the end of this lesson, you'll be able to build and organize your own file kingdoms!

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create new folders with `mkdir`
- ✅ Create new files with `touch`
- ✅ Copy files with `cp`
- ✅ Move and rename files with `mv`
- ✅ Delete files and folders with `rm`

---

## 🪝 Hook: The Construction Crew

Imagine you're in charge of building a brand-new city. You need to:

- 🏗️ **Build buildings** (create folders and files)
- 📋 **Make copies of blueprints** (copy files)
- 🚚 **Move buildings to new locations** (move files)
- 🏷️ **Rename streets** (rename files)
- 💥 **Demolish old buildings** (delete files)

In the terminal, you have commands for ALL of these things. Let's meet your construction crew! 🏗️

---

## 🧠 Setting Up: Create a Practice Area

Before we start, let's create a safe practice area so we don't accidentally mess with important files!

```bash
# Go to your home directory
cd ~

# Create a practice folder
mkdir command_quest_practice

# Go into it
cd command_quest_practice

# Confirm you're in the right place
pwd
```

You should see something like: `/home/alex/command_quest_practice`

> ⚠️ **IMPORTANT:** Always practice in this folder! This keeps your real files safe.

---

## 🧠 Command 1: `mkdir` — Build New Folders! 🏗️

### What it stands for: **M**a**k**e **Dir**ectory

### What it does:
Creates a new, empty folder.

### Basic Usage:

```bash
mkdir my_games
```

This creates a folder called `my_games` in your current location!

### Verify it worked:
```bash
ls
```
```
my_games
```
It's there! 🎉

### Create Multiple Folders at Once:
```bash
mkdir photos music videos
```
This creates THREE folders in one command!

```bash
ls
```
```
my_games  music  photos  videos
```

### Create Nested Folders (Folders Inside Folders):
```bash
mkdir -p school/math/homework
```

The `-p` flag (short for "parents") creates the WHOLE path at once! It creates `school`, then `math` inside it, then `homework` inside that!

```
📁 school
└── 📁 math
    └── 📁 homework
```

> 🎮 **Analogy:** `mkdir` is like building a new room in your house. `mkdir -p` is like building a whole wing with multiple rooms at once!

### Naming Rules:
- ✅ Use underscores or hyphens: `my_folder` or `my-folder`
- ✅ Use lowercase: `documents`
- ❌ Avoid spaces: `my folder` causes problems! (use `my_folder` instead)
- ❌ Avoid special characters: `?`, `*`, `&`, etc.

---

## 🧠 Command 2: `touch` — Create New Files! 📄

### What it does:
Creates a new, empty file. (Technically, it updates the timestamp of a file, but if the file doesn't exist, it creates one!)

### Basic Usage:
```bash
touch my_notes.txt
```

This creates an empty file called `my_notes.txt`!

### Verify:
```bash
ls
```
```
my_games  music  my_notes.txt  photos  videos
```

### Create Multiple Files:
```bash
touch todo.txt ideas.txt reminders.txt
```

### Create Files in Specific Folders:
```bash
touch school/math/homework/assignment1.txt
```

This creates `assignment1.txt` inside the `school/math/homework` folder (which we made earlier with `mkdir -p`).

> 🎮 **Analogy:** If `mkdir` builds rooms, `touch` places empty notebooks on the desk inside those rooms!

---

## 🧠 Command 3: `cp` — Copy Files! 📋

### What it stands for: **C**o**p**y

### What it does:
Makes a duplicate of a file (the original stays where it is).

### Basic Usage:
```bash
cp my_notes.txt my_notes_backup.txt
```

Now you have TWO files — the original and a copy:
```bash
ls
```
```
my_notes.txt  my_notes_backup.txt  ...
```

### Copy a File Into a Folder:
```bash
cp my_notes.txt music/
```
This puts a copy of `my_notes.txt` inside the `music` folder.

### Copy a Folder (and Everything Inside It):
```bash
cp -r school school_backup
```

The `-r` flag means **recursive** — it copies the folder AND everything inside it (all subfolders and files).

> ⚠️ **Important:** You MUST use `-r` when copying folders! Without it, the computer will refuse.

> 🎮 **Analogy:** `cp` is like a photocopier. It makes an exact copy while keeping the original!

### `cp` Quick Reference:

| Command | What It Does |
|---------|-------------|
| `cp file.txt copy.txt` | Copies file with a new name |
| `cp file.txt folder/` | Copies file into a folder |
| `cp -r folder/ backup/` | Copies entire folder |

---

## 🧠 Command 4: `mv` — Move and Rename! 🚚

### What it stands for: **M**o**v**e

### What it does:
Moves a file to a new location OR renames it. (Yes, one command does both!)

### Moving a File:
```bash
mv todo.txt music/
```
This MOVES `todo.txt` into the `music` folder. The original is gone from the current location — it's been moved!

### Renaming a File:
```bash
mv ideas.txt brilliant_ideas.txt
```
This RENAMES `ideas.txt` to `brilliant_ideas.txt`. Same file, new name!

> 🔑 **Key Idea:** How does the computer know if you're moving or renaming?
> - If the destination is a **folder** → it MOVES the file there
> - If the destination is a **new name** → it RENAMES the file

### Moving and Renaming at the Same Time:
```bash
mv reminders.txt music/song_ideas.txt
```
This moves `reminders.txt` into the `music` folder AND renames it to `song_ideas.txt`!

### Move a Folder:
```bash
mv music videos/music_collection
```

> 🎮 **Analogy:** `mv` is like picking up a book and putting it on a different shelf. Or taking off the cover and giving it a new title!

### `mv` Quick Reference:

| Command | What It Does |
|---------|-------------|
| `mv file.txt folder/` | Moves file into folder |
| `mv oldname.txt newname.txt` | Renames the file |
| `mv file.txt folder/newname.txt` | Moves AND renames |
| `mv folder1 folder2` | Moves/renames a folder |

---

## 🧠 Command 5: `rm` — Delete! 💥

### What it stands for: **R**e**m**ove

### What it does:
Permanently deletes a file. There is **no trash can** — it's GONE forever!

> ⚠️ **DANGER ZONE:** `rm` is the most powerful (and dangerous) command you'll learn. There is NO undo! Always double-check before deleting!

### Delete a File:
```bash
rm my_notes_backup.txt
```

The file is gone. No "Are you sure?" No trash. Gone! 💨

### Delete a Folder (and Everything Inside):
```bash
rm -r school_backup
```

The `-r` flag (recursive) deletes the folder and ALL its contents.

### Safe Delete — Ask First:
```bash
rm -i important_file.txt
```

The `-i` flag (interactive) asks you "Are you sure?" before deleting. You type `y` for yes or `n` for no.

```
rm: remove regular file 'important_file.txt'? y
```

> 💡 **Pro Tip for Beginners:** Always use `rm -i` until you're very comfortable with the command!

### `rm` Quick Reference:

| Command | What It Does |
|---------|-------------|
| `rm file.txt` | Deletes a file (permanent!) |
| `rm -i file.txt` | Deletes with confirmation prompt |
| `rm -r folder/` | Deletes a folder and everything in it |
| `rm -ri folder/` | Deletes folder with confirmation for each item |

### ⛔ THE GOLDEN RULE:

```
NEVER, EVER run: rm -r /
```

This would try to delete EVERYTHING on your computer from the root down. Modern systems have protections, but **never, ever try this**. It's the terminal equivalent of setting your house on fire!

> 🎮 **Analogy:** `rm` is like a shredder. Once you put paper through it, you can't tape it back together. Always think before you shred!

---

## 🧠 Command Summary Card

Here's your quick reference card — save this!

```
╔══════════════════════════════════════════════════════════╗
║              📋 FILE COMMANDS CHEAT SHEET                ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  mkdir folder_name      Create a new folder              ║
║  mkdir -p a/b/c         Create nested folders             ║
║  touch file.txt         Create a new empty file           ║
║  cp src dst             Copy a file                       ║
║  cp -r src dst          Copy a folder                     ║
║  mv src dst             Move or rename                    ║
║  rm file.txt            Delete a file (PERMANENT!)        ║
║  rm -r folder/          Delete a folder (PERMANENT!)      ║
║  rm -i file.txt         Delete with safety prompt         ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎮 Activity 1: Build a Kingdom! (⭐ 30 XP)

**Instructions:** You're going to build a mini file kingdom using ONLY terminal commands! Follow each step in order.

Make sure you're in your practice folder first:
```bash
cd ~/command_quest_practice
```

**Your Quest — Type each command:**

```bash
# Step 1: Create the kingdom folder
mkdir my_kingdom

# Step 2: Enter the kingdom
cd my_kingdom

# Step 3: Create three areas
mkdir castle village forest

# Step 4: Create rooms inside the castle
mkdir -p castle/throne_room castle/library castle/kitchen

# Step 5: Create some files
touch castle/throne_room/crown.txt
touch castle/library/spellbook.txt
touch castle/kitchen/recipe.txt
touch village/shop.txt
touch village/inn.txt
touch forest/treasure_map.txt

# Step 6: Verify your kingdom!
ls
ls castle
ls castle/throne_room
```

**Write down what you see after each `ls` command!**

**Bonus Challenge (+10 XP):** Add 3 more files and 1 more folder of your own choosing!

---

## 🎮 Activity 2: File Management Mission! (⭐ 25 XP)

**Instructions:** You're still in `my_kingdom`. Complete these file operations!

| Step | Task | Command to Type |
|------|------|----------------|
| 1 | Copy the spellbook to the village | `cp castle/library/spellbook.txt village/` |
| 2 | Rename the treasure map to "X_marks_the_spot.txt" | ??? (figure this out!) |
| 3 | Move the recipe from the kitchen to the village inn | ??? (figure this out!) |
| 4 | Create a backup of the entire castle | ??? (figure this out!) |
| 5 | Delete the backup castle | ??? (figure this out!) |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `cp castle/library/spellbook.txt village/` (given)
2. `mv forest/treasure_map.txt forest/X_marks_the_spot.txt`
3. `mv castle/kitchen/recipe.txt village/` (or `mv castle/kitchen/recipe.txt village/inn_recipe.txt`)
4. `cp -r castle castle_backup`
5. `rm -r castle_backup`

**Scoring:** Each correct step = ⭐ 5 XP (Total: 25 XP)

</details>

---

## 🎮 Activity 3: Command Translator! (⭐ 15 XP)

**Instructions:** Translate each English sentence into the correct terminal command.

| # | English | Terminal Command |
|---|---------|-----------------|
| 1 | "Create a folder called 'projects'" | ??? |
| 2 | "Create an empty file called 'readme.txt'" | ??? |
| 3 | "Copy 'notes.txt' and name the copy 'notes_backup.txt'" | ??? |
| 4 | "Rename 'old_name.txt' to 'new_name.txt'" | ??? |
| 5 | "Delete the file 'junk.txt' with a safety prompt" | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `mkdir projects`
2. `touch readme.txt`
3. `cp notes.txt notes_backup.txt`
4. `mv old_name.txt new_name.txt`
5. `rm -i junk.txt`

**Scoring:** Each correct = ⭐ 3 XP (Total: 15 XP)

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
What does `mkdir -p projects/2024/january` do?

- A) Creates only the `january` folder
- B) Creates all three folders (projects, 2024, and january) in a nested structure
- C) Creates three separate folders at the same level
- D) Deletes the folders

### Question 2:
What's the difference between `cp` and `mv`?

- A) There is no difference
- B) `cp` makes a copy (original stays), `mv` moves it (original is gone from old location)
- C) `cp` is for files, `mv` is for folders
- D) `cp` is faster than `mv`

### Question 3:
Why is `rm` considered dangerous?

- A) It's very slow
- B) It only works on Tuesdays
- C) It permanently deletes files with no undo or trash can
- D) It requires internet access

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **B) Creates all three folders in a nested structure** — The `-p` flag creates the whole path!
2. **B) `cp` makes a copy, `mv` moves it** — Copy = duplicate, Move = relocate!
3. **C) It permanently deletes with no undo** — Always double-check before using `rm`!

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 You're now a file management wizard!

You can now:
- 🏗️ Build folders with `mkdir`
- 📄 Create files with `touch`
- 📋 Copy files and folders with `cp`
- 🚚 Move and rename with `mv`
- 💥 Delete (carefully!) with `rm`

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 150 XP |
| Activity XP (max) | ⭐ 70 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 250 XP** |

---

## 🔍 Coming Up Next...

Test your skills with the **[Module 2 Quiz!](quiz_02.md)** Then in Module 3, you'll learn to LOOK INSIDE files and SEARCH for things — the real detective work begins! 🔍

**[Next: Module 2 Quiz →](quiz_02.md)**
