# 🏆 Command Quest — Module 4: FINAL PROJECT

## 🌟 The Grand Quest: Build a Digital Kingdom!

Congratulations, Explorer! 🎊 You've learned every skill in Command Quest. Now it's time to prove you're a true **Command Wizard** by completing this epic final project!

You'll combine ALL the skills you've learned across every module to build, explore, investigate, and document a **complete digital kingdom** — entirely from the terminal!

---

## 🎯 Project Goals

In this project, you will:

- ✅ Create a complex folder structure (Module 2 skills)
- ✅ Create and edit files (Module 2 + Module 4 skills)
- ✅ Navigate through directories (Module 2 skills)
- ✅ View file contents (Module 3 skills)
- ✅ Search for files and text (Module 3 skills)
- ✅ Use pipes and redirects (Module 4 skills)
- ✅ Edit files with nano (Module 4 skills)

**Total XP Available: ⭐ 500 XP**

---

## 📋 Project Rules

1. Do EVERYTHING from the terminal — no clicking allowed!
2. Follow each phase in order
3. Check off each task as you complete it
4. At the end, you'll verify your work by running some check commands

---

## 🏗️ Phase 1: Build the Kingdom (⭐ 100 XP)

### Step 1: Set Up Your Project Base

```bash
cd ~/command_quest_practice
mkdir digital_kingdom
cd digital_kingdom
```

### Step 2: Create the Kingdom Structure

Create the following folder structure using `mkdir` commands. Use `mkdir -p` where it helps!

```
digital_kingdom/
├── castle/
│   ├── throne_room/
│   ├── library/
│   ├── armory/
│   └── dungeon/
├── village/
│   ├── market/
│   ├── inn/
│   └── blacksmith/
├── forest/
│   ├── clearing/
│   ├── cave/
│   └── river/
├── academy/
│   ├── classes/
│   └── records/
└── archives/
```

<details>
<summary>💡 Hint: Possible commands</summary>

```bash
mkdir -p castle/throne_room castle/library castle/armory castle/dungeon
mkdir -p village/market village/inn village/blacksmith
mkdir -p forest/clearing forest/cave forest/river
mkdir -p academy/classes academy/records
mkdir archives
```

</details>

### Step 3: Verify Your Structure

```bash
find . -type d | sort
```

You should see all the directories listed!

**Checklist:**
- [ ] Created all 15 directories
- [ ] Verified with `find . -type d`

---

## 📜 Phase 2: Populate the Kingdom (⭐ 100 XP)

### Step 1: Create Castle Files

```bash
# Royal decree in the throne room
echo "ROYAL DECREE: All citizens shall learn the Terminal!" > castle/throne_room/decree.txt
echo "By order of the Command Wizard" >> castle/throne_room/decree.txt

# Books in the library
echo "Chapter 1: The History of Computing" > castle/library/history_book.txt
echo "The first computers filled entire rooms." >> castle/library/history_book.txt
echo "They used vacuum tubes and punch cards." >> castle/library/history_book.txt
echo "Today, your phone is more powerful than those early computers!" >> castle/library/history_book.txt

echo "Spell: ls - reveals hidden items" > castle/library/spellbook.txt
echo "Spell: cd - teleports to new locations" >> castle/library/spellbook.txt
echo "Spell: grep - finds hidden text" >> castle/library/spellbook.txt
echo "Spell: pipe - chains spells together" >> castle/library/spellbook.txt

# Weapons in the armory
echo "Keyboard of Speed - Type commands faster" > castle/armory/weapons.txt
echo "Shield of Sudo - Administrative protection" >> castle/armory/weapons.txt
echo "Wand of Grep - Search through anything" >> castle/armory/weapons.txt

# Secret in the dungeon
echo "SECRET: The master password is 'permission_granted'" > castle/dungeon/secret.txt
```

### Step 2: Create Village Files

```bash
# Market inventory
echo "Apples: 50" > village/market/inventory.txt
echo "Bread: 30" >> village/market/inventory.txt
echo "Cheese: 20" >> village/market/inventory.txt
echo "Dragon Fruit: 5" >> village/market/inventory.txt
echo "Enchanted Water: 10" >> village/market/inventory.txt

# Guest book at the inn
echo "Guest 1: Alice the Explorer - arrived Monday" > village/inn/guestbook.txt
echo "Guest 2: Bob the Builder - arrived Tuesday" >> village/inn/guestbook.txt
echo "Guest 3: Charlie the Coder - arrived Wednesday" >> village/inn/guestbook.txt
echo "Guest 4: Diana the Detective - arrived Thursday" >> village/inn/guestbook.txt
echo "Guest 5: Eve the Enchantress - arrived Friday" >> village/inn/guestbook.txt

# Blacksmith orders
echo "Order 1: Sword for the knight - COMPLETE" > village/blacksmith/orders.txt
echo "Order 2: Shield for the guard - IN PROGRESS" >> village/blacksmith/orders.txt
echo "Order 3: Armor for the explorer - PENDING" >> village/blacksmith/orders.txt
```

### Step 3: Create Forest Files

```bash
# Creatures in the clearing
echo "A friendly fox watches from the bushes." > forest/clearing/creatures.txt
echo "Butterflies dance in the sunlight." >> forest/clearing/creatures.txt
echo "A wise old owl sits in the oak tree." >> forest/clearing/creatures.txt

# Treasure in the cave
echo "TREASURE MAP" > forest/cave/treasure_map.txt
echo "Start at the castle gates" >> forest/cave/treasure_map.txt
echo "Walk north to the forest" >> forest/cave/treasure_map.txt
echo "Find the cave behind the waterfall" >> forest/cave/treasure_map.txt
echo "Look for the red X on the ground" >> forest/cave/treasure_map.txt
echo "Dig three feet down" >> forest/cave/treasure_map.txt
echo "The treasure is yours!" >> forest/cave/treasure_map.txt

# River log
echo "Day 1: River is calm. Fish spotted: 12" > forest/river/log.txt
echo "Day 2: Light rain. Fish spotted: 8" >> forest/river/log.txt
echo "Day 3: Storm! Fish spotted: 0" >> forest/river/log.txt
echo "Day 4: Clear skies. Fish spotted: 15" >> forest/river/log.txt
echo "Day 5: Perfect day. Fish spotted: 20" >> forest/river/log.txt
```

### Step 4: Create Academy Files

```bash
# Class roster
echo "Terminal 101 - Students: Alice, Bob, Charlie" > academy/classes/roster.txt
echo "File System 201 - Students: Diana, Eve, Frank" >> academy/classes/roster.txt
echo "Pipe Master 301 - Students: Grace, Henry, Iris" >> academy/classes/roster.txt

# Student grades
echo "Alice:95" > academy/records/grades.txt
echo "Bob:82" >> academy/records/grades.txt
echo "Charlie:91" >> academy/records/grades.txt
echo "Diana:88" >> academy/records/grades.txt
echo "Eve:97" >> academy/records/grades.txt
echo "Frank:73" >> academy/records/grades.txt
echo "Grace:100" >> academy/records/grades.txt
echo "Henry:85" >> academy/records/grades.txt
echo "Iris:90" >> academy/records/grades.txt
```

**Checklist:**
- [ ] Created all castle files (4 files)
- [ ] Created all village files (3 files)
- [ ] Created all forest files (3 files)
- [ ] Created all academy files (2 files)

---

## 🔍 Phase 3: Explore and Investigate (⭐ 100 XP)

Now use your detective skills to answer these questions. **Write down each command you use AND the answer!**

### Investigation 1: How many total files are in the kingdom?
```bash
# Your command here (hint: find + wc)
```

### Investigation 2: What's in the royal decree?
```bash
# Your command here (hint: cat)
```

### Investigation 3: Find all .txt files in the kingdom
```bash
# Your command here (hint: find)
```

### Investigation 4: Which files mention "Alice"?
```bash
# Your command here (hint: grep -r)
```

### Investigation 5: How many guests are at the inn?
```bash
# Your command here (hint: wc -l)
```

### Investigation 6: Sort the academy grades and find the top 3 students
```bash
# Your command here (hint: sort + tail or head)
```

### Investigation 7: What is the secret in the dungeon?
```bash
# Your command here
```

### Investigation 8: How many fish were spotted in total across all river log days?
```bash
# Read the file, add up the fish numbers manually from what you see
```

### Investigation 9: Find all files that contain the word "treasure"
```bash
# Your command here (hint: grep -r)
```

### Investigation 10: How many spells are in the spellbook?
```bash
# Your command here (hint: wc -l)
```

<details>
<summary>🔑 Click to Check Example Commands and Answers!</summary>

1. `find . -type f | wc -l` → **12 files**
2. `cat castle/throne_room/decree.txt` → Royal decree about learning Terminal
3. `find . -name "*.txt"` → Lists all 12 .txt files
4. `grep -r "Alice" .` → Found in guestbook.txt, roster.txt, and grades.txt
5. `wc -l village/inn/guestbook.txt` → **5 guests**
6. `sort -t: -k2 -n academy/records/grades.txt | tail -n 3` → Grace (100), Eve (97), Alice (95)
7. `cat castle/dungeon/secret.txt` → The password is 'permission_granted'
8. `cat forest/river/log.txt` → 12 + 8 + 0 + 15 + 20 = **55 fish**
9. `grep -r "treasure" .` → Found in treasure_map.txt (and possibly elsewhere)
10. `wc -l castle/library/spellbook.txt` → **4 spells**

</details>

**Scoring:** Each correct investigation = ⭐ 10 XP (Total: 100 XP)

---

## 📋 Phase 4: Organize and Manage (⭐ 100 XP)

### Task 1: Create an Archive (⭐ 20 XP)

Create a sorted, unique report of all files in the kingdom:

```bash
find . -type f | sort > archives/file_report.txt
cat archives/file_report.txt
```

### Task 2: Back Up the Castle Library (⭐ 20 XP)

```bash
cp -r castle/library castle/library_backup
ls castle/library_backup
```

### Task 3: Create a Kingdom Summary (⭐ 30 XP)

Use `nano` to create a summary document:

```bash
nano archives/kingdom_summary.txt
```

Write the following inside (you can customize it!):

```
=================================
  DIGITAL KINGDOM SUMMARY REPORT
=================================

Kingdom Name: [Your Kingdom Name]
Ruler: [Your Name], the Command Wizard
Date: [Today's Date]

Areas:
- Castle (4 rooms: throne room, library, armory, dungeon)
- Village (3 buildings: market, inn, blacksmith)
- Forest (3 areas: clearing, cave, river)
- Academy (2 sections: classes, records)
- Archives (reports and backups)

Total Files: [number]
Total Directories: [number]

Skills Used to Build This Kingdom:
- mkdir, touch, echo (creation)
- cd, ls, pwd (navigation)
- cat, head, tail, less (viewing)
- find, grep (searching)
- sort, uniq, wc (data processing)
- pipes and redirects (power moves)
- nano (text editing)

Status: COMPLETE!
```

Save and exit nano (`Ctrl+O`, `Enter`, `Ctrl+X`).

### Task 4: Create a Completion Log (⭐ 30 XP)

```bash
echo "=== KINGDOM COMPLETION LOG ===" > archives/completion_log.txt
echo "" >> archives/completion_log.txt
echo "Completed by: $(whoami)" >> archives/completion_log.txt
echo "Date: $(date)" >> archives/completion_log.txt
echo "" >> archives/completion_log.txt
echo "File count:" >> archives/completion_log.txt
find . -type f | wc -l >> archives/completion_log.txt
echo "" >> archives/completion_log.txt
echo "Directory count:" >> archives/completion_log.txt
find . -type d | wc -l >> archives/completion_log.txt
echo "" >> archives/completion_log.txt
echo "All files:" >> archives/completion_log.txt
find . -type f | sort >> archives/completion_log.txt
```

View your completion log:
```bash
cat archives/completion_log.txt
```

**Checklist:**
- [ ] Created file report in archives
- [ ] Backed up the library
- [ ] Created kingdom summary with nano
- [ ] Created completion log with pipes and redirects

---

## ✅ Phase 5: Verification (⭐ 100 XP)

Run these commands to verify your kingdom is complete. Each check that passes earns XP!

### Check 1: Directory Count (⭐ 20 XP)
```bash
echo "Directories: $(find . -type d | wc -l)"
# Should be 16 or more (15 original + library_backup)
```

### Check 2: File Count (⭐ 20 XP)
```bash
echo "Files: $(find . -type f | wc -l)"
# Should be 15 or more (12 original + 3 archive files + backup files)
```

### Check 3: Can You Find the Secret? (⭐ 20 XP)
```bash
grep -r "password" .
# Should find the secret in the dungeon!
```

### Check 4: Library Backup Exists? (⭐ 20 XP)
```bash
ls castle/library_backup/
# Should show spellbook.txt and history_book.txt
```

### Check 5: Kingdom Summary Exists? (⭐ 20 XP)
```bash
head -n 5 archives/kingdom_summary.txt
# Should show the first 5 lines of your summary
```

---

## 🏅 PROJECT COMPLETE!

### 🎉🎊🎉 CONGRATULATIONS, COMMAND WIZARD! 🎉🎊🎉

You did it! You've completed the entire Command Quest course and built a Digital Kingdom using nothing but terminal commands!

### Your Final Project Rewards:

| Phase | XP |
|-------|-----|
| Phase 1: Build the Kingdom | ⭐ 100 XP |
| Phase 2: Populate the Kingdom | ⭐ 100 XP |
| Phase 3: Explore and Investigate | ⭐ 100 XP |
| Phase 4: Organize and Manage | ⭐ 100 XP |
| Phase 5: Verification | ⭐ 100 XP |
| **TOTAL** | **⭐ 500 XP** |

---

## 🧙‍♂️ You Are Now a Command Wizard!

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║          🧙‍♂️ GRAND COMMAND WIZARD BADGE 🧙‍♂️              ║
║                                                           ║
║     You have completed Command Quest and mastered         ║
║     the art of the Terminal!                              ║
║                                                           ║
║     Skills Mastered:                                      ║
║     ✅ Computer Fundamentals                              ║
║     ✅ File System Navigation                             ║
║     ✅ Terminal Commands                                  ║
║     ✅ File Management                                    ║
║     ✅ File Viewing & Searching                           ║
║     ✅ Pipes & Redirects                                  ║
║     ✅ Text Editing                                       ║
║                                                           ║
║     Title: 🧙‍♂️ Grand Command Wizard                      ║
║     Course: COMPLETE ✅                                   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🚀 What's Next? Keep Learning!

Your terminal journey doesn't end here! Here are some exciting topics to explore:

| Topic | What You'll Learn |
|-------|-----------------|
| **Bash Scripting** | Write programs that run terminal commands automatically! |
| **Git & GitHub** | Save your code and collaborate with others |
| **Python Programming** | Write real programs using a powerful language |
| **Linux System Administration** | Manage entire computer systems |
| **Web Development** | Build websites with HTML, CSS, and JavaScript |

### Recommended Next Steps:
1. Practice the commands daily — repetition builds mastery!
2. Try customizing your terminal (colors, prompt, aliases)
3. Learn about `bash` scripting (writing mini-programs in the terminal)
4. Start learning Git for version control
5. Explore Python — it works beautifully with the terminal!

---

> *"The expert was once a beginner. Keep exploring, keep learning, keep commanding!"* 🧙‍♂️

**Thank you for completing Command Quest! See the [Achievements page](../achievements.md) for your full badge collection!** 🏆
