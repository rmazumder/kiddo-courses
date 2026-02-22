# 📚 Command Quest — Module 1, Lesson 2: The File System

## 🌟 Your Mission Today

Welcome back, Explorer! 🗺️ Today you're going to discover how your computer keeps track of millions of files without ever losing a single one. You'll learn about files, folders, paths, and extensions — the invisible organization system that makes everything work!

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Explain what a **file** and a **folder** (directory) are
- ✅ Understand **file extensions** and what they mean
- ✅ Read and write a **file path**
- ✅ Describe how the **file system** is organized like a tree

---

## 🪝 Hook: The World's Biggest Library

Imagine a library with **billions** of books. No librarian. No catalog. Books are just thrown in a giant pile on the floor.

Could you find the book you need? 😱 No way!

Now imagine that same library, but perfectly organized:
- Books are sorted into **sections** (Science, History, Fiction...)
- Each section has **shelves**
- Each shelf has **labeled books**
- Every book has an **address** so you can find it instantly

**That's exactly what your computer's file system does!** Your computer might have hundreds of thousands of files, but it can find any one of them in less than a second. Let's learn how! ⚡

---

## 🧠 Learning Point 1: What Are Files?

A **file** is a collection of information saved with a name. That's it!

Everything on your computer is stored as a file:

| What You See | The File |
|-------------|----------|
| A photo of your dog | `dog_photo.jpg` |
| Your homework essay | `homework.docx` |
| Your favorite song | `cool_song.mp3` |
| A video game save | `save_game.dat` |
| This lesson! | `lesson_02_file_system.md` |

> 🎮 **Analogy:** A file is like a **book** in a library. Each book has a title (file name) and contains information inside it.

### 📛 File Names

Every file has a name with two parts:

```
  my_photo.jpg
  --------+---
  name    | extension
```

1. **The Name** — What you call it (e.g., `my_photo`)
2. **The Extension** — A short code after the dot that tells the computer what TYPE of file it is (e.g., `.jpg`)

---

## 🧠 Learning Point 2: File Extensions — The Secret Code

The **file extension** is like a label on a jar — it tells you (and the computer) what's inside!

### Common File Extensions:

| Extension | What It Is | Icon Analogy |
|-----------|-----------|--------------|
| `.txt` | Plain text file | 📝 A simple note |
| `.doc` / `.docx` | Word document | 📄 A fancy letter |
| `.pdf` | PDF document (can't easily edit) | 📋 A printed poster |
| `.jpg` / `.png` | Image/photo | 🖼️ A photograph |
| `.mp3` / `.wav` | Audio/music file | 🎵 A music CD |
| `.mp4` / `.mov` | Video file | 🎬 A movie DVD |
| `.html` | Web page | 🌐 A website page |
| `.py` | Python program | 🐍 A code script |
| `.md` | Markdown file (like this lesson!) | 📝 A formatted note |
| `.zip` | Compressed (squished) file | 📦 A packed suitcase |

> 🔑 **Key Idea:** The extension tells the computer which program to use to open the file. A `.mp3` opens in a music player. A `.jpg` opens in a photo viewer. Change the extension, and the computer gets confused!

---

## 🧠 Learning Point 3: Folders (Directories)

A **folder** (also called a **directory**) is a container that holds files and other folders.

> 🎮 **Analogy:** If files are books, then folders are **bookshelves**. And just like a big library has sections with shelves inside them, folders can contain MORE folders inside them!

### Why Folders Matter:

Without folders, all your files would be in one giant pile — like dumping every book in a library on the floor. Folders help you:

- 🗂️ **Organize** — Keep related files together
- 🔍 **Find things** — Know where to look
- 🧹 **Stay tidy** — Avoid a digital mess!

---

## 🧠 Learning Point 4: The File System Tree

Your computer organizes everything in a **tree structure** — like a family tree, but for files!

```
🌳 / (Root - the very top!)
├── 📁 home
│   └── 📁 alex (your user folder)
│       ├── 📁 Documents
│       │   ├── 📄 homework.docx
│       │   └── 📄 book_report.pdf
│       ├── 📁 Pictures
│       │   ├── 🖼️ vacation.jpg
│       │   └── 🖼️ dog.png
│       ├── 📁 Music
│       │   └── 🎵 cool_song.mp3
│       ├── 📁 Downloads
│       │   └── 📦 game_installer.zip
│       └── 📁 Desktop
│           └── 📄 notes.txt
├── 📁 usr
│   └── 📁 bin (where programs live)
└── 📁 etc (system settings)
```

### Key Vocabulary:

- **Root** `/` — The very top of the tree. Everything starts here. (On Windows, this is `C:\`)
- **Home Directory** `~` — YOUR personal folder. This is where your Documents, Pictures, and Desktop folders live.
- **Parent Directory** — The folder ONE level UP from where you are
- **Subdirectory** — A folder INSIDE another folder (a child folder)

> 🎮 **Analogy:** Think of it like your home address:
> - **Country** = Root (`/`)
> - **City** = Home folder (`/home/alex`)
> - **Street** = A subfolder (`/home/alex/Documents`)
> - **House** = The file (`/home/alex/Documents/homework.docx`)

---

## 🧠 Learning Point 5: File Paths — The Address System

A **file path** is the complete address of a file — it tells the computer exactly where to find it.

### Example Path:

```
/home/alex/Documents/homework.docx
```

Let's break it down:

| Part | Meaning |
|------|---------|
| `/` | Start at the root (top of the tree) |
| `home/` | Go into the "home" folder |
| `alex/` | Go into Alex's folder |
| `Documents/` | Go into the "Documents" folder |
| `homework.docx` | Here's the file! |

### Two Types of Paths:

**1. Absolute Path** — The FULL address from the root
```
/home/alex/Documents/homework.docx
```
> Like saying: "123 Oak Street, Springfield, IL, USA"

**2. Relative Path** — The address from WHERE YOU ARE right now
```
Documents/homework.docx
```
> Like saying: "Go down the hall, second door on the left" (only works if you know where you're starting!)

### Special Path Shortcuts:

| Symbol | Meaning | Example |
|--------|---------|---------|
| `/` | Root directory (the very top) | `/home/alex` |
| `~` | Your home directory | `~/Documents` = `/home/alex/Documents` |
| `.` | The current directory (where you are now) | `./file.txt` |
| `..` | The parent directory (one level up) | `../Pictures` |

---

## 🎮 Activity 1: Read the Map! (⭐ 20 XP)

**Instructions:** Look at this file tree and answer the questions below.

```
🌳 /
├── 📁 home
│   └── 📁 maya
│       ├── 📁 Documents
│       │   ├── 📄 story.txt
│       │   └── 📁 school
│       │       ├── 📄 math_hw.pdf
│       │       └── 📄 science_project.docx
│       ├── 📁 Pictures
│       │   ├── 🖼️ cat.jpg
│       │   └── 🖼️ sunset.png
│       └── 📁 Music
│           └── 🎵 playlist.mp3
```

**Questions:**

1. What is the absolute path to `cat.jpg`?
2. What is the absolute path to `math_hw.pdf`?
3. If Maya is currently in her `Documents` folder, what is the RELATIVE path to `cat.jpg`?
4. How many folders (directories) are in this tree? (Count them all!)
5. What is the parent directory of the `school` folder?

<details>
<summary>🔑 Click to Check Your Answers!</summary>

1. `/home/maya/Pictures/cat.jpg`
2. `/home/maya/Documents/school/math_hw.pdf`
3. `../Pictures/cat.jpg` (go up one level with `..`, then into Pictures)
4. **7 folders**: `/`, `home`, `maya`, `Documents`, `school`, `Pictures`, `Music`
5. `Documents` (or the full path: `/home/maya/Documents`)

**Scoring:** Each correct = ⭐ 4 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 2: Extension Detective! (⭐ 20 XP)

**Instructions:** For each file below, write down:
- (A) What TYPE of file it is
- (B) What program might open it

| # | File Name | Type? | Opens With? |
|---|----------|-------|-------------|
| 1 | `birthday_party.mp4` | ??? | ??? |
| 2 | `recipe.txt` | ??? | ??? |
| 3 | `selfie.png` | ??? | ??? |
| 4 | `my_game.py` | ??? | ??? |
| 5 | `album.zip` | ??? | ??? |

<details>
<summary>🔑 Click to Check Your Answers!</summary>

| # | File Name | Type | Opens With |
|---|----------|------|------------|
| 1 | `birthday_party.mp4` | Video file | Video player (VLC, QuickTime) |
| 2 | `recipe.txt` | Text file | Text editor (Notepad, TextEdit) |
| 3 | `selfie.png` | Image file | Image viewer (Photos, Preview) |
| 4 | `my_game.py` | Python program | Python interpreter or code editor |
| 5 | `album.zip` | Compressed archive | File manager or unzip program |

**Scoring:** Each fully correct row = ⭐ 4 XP (Total: 20 XP)

</details>

---

## 🎮 Activity 3: Design Your Own File System! (⭐ 20 XP)

**Instructions:** Imagine you're organizing files for a school project about the solar system. Create a file tree on paper (or type it out) that includes:

**Requirements:**
- A main project folder called `solar_system_project`
- At least 3 subfolders (e.g., `images`, `research`, `presentation`)
- At least 6 files with proper extensions
- Use realistic file names and the correct extensions

**Example start:**
```
📁 solar_system_project
├── 📁 images
│   ├── 🖼️ earth.jpg
│   └── ...
├── 📁 research
│   └── ...
└── ...
```

> 🌟 **Bonus (+10 XP):** Include at least 4 different file extensions in your tree!

---

## ⚡ Quick Quiz — Earn Bonus XP! (⭐ 30 XP)

### Question 1:
What does a file extension tell the computer?

- A) How big the file is
- B) When the file was created
- C) What type of file it is and how to open it
- D) Who created the file

### Question 2:
What does the symbol `~` represent in a file path?

- A) The root directory
- B) The current directory
- C) Your home directory
- D) The parent directory

### Question 3:
In the path `/home/alex/Music/song.mp3`, what is the parent directory of `song.mp3`?

- A) `/home`
- B) `/home/alex`
- C) `/home/alex/Music`
- D) `/`

<details>
<summary>🔑 Click to Check Your Quiz Answers!</summary>

1. **C) What type of file it is and how to open it** — The extension is a code that tells the computer which program should open the file.
2. **C) Your home directory** — The tilde `~` is a shortcut for your personal home folder (like `/home/alex`).
3. **C) `/home/alex/Music`** — The parent directory is the folder directly containing the file.

**Scoring:** Each correct answer = ⭐ 10 XP

</details>

---

## 🏅 Lesson Complete!

### 🎉 Fantastic work, Explorer!

You've mastered the file system! You now understand:

- What files and folders are
- How file extensions work as secret type codes
- How the file system is organized like a tree
- How to read and write file paths (absolute and relative)

### Your Rewards:

| Reward | Amount |
|--------|--------|
| Lesson XP | ⭐ 100 XP |
| Activity XP (max) | ⭐ 60 XP |
| Quiz XP (max) | ⭐ 30 XP |
| **Possible Total** | **⭐ 190 XP** |

---

## 🔍 Coming Up Next...

Before moving to Module 2, test your knowledge with the **[Module 1 Quiz!](quiz_01.md)** Then get ready to meet the most powerful tool on your computer — the **Terminal!** 🧙‍♂️

**[Next: Module 1 Quiz →](quiz_01.md)**

---

## Navigation

| | |
|:---|---:|
| [← 🖥️ Command Quest — Module 1, Lesson 1: Computer Basics](lesson_01_computer_basics.md) | [Module Overview →](README.md) |
