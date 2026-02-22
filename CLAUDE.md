# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A collection of 5 self-contained kids' coding and electronics courses (ages 6–14), structured as gamified Markdown curriculum. There is no build system, no dependencies, and no compilation step — all content is static Markdown, images, and Python scripts.

## Courses

| Folder | Subject | Modules |
|--------|---------|---------|
| `python_course/` | Python programming | 8 |
| `computer_course/` | How computers work | 4 |
| `electronics-robotics/` | Electronics + Arduino + Robotics | 6 |
| `how_the_internet_works/` | Networking fundamentals | 5 |
| `raspberry_pi_explorer/` | Raspberry Pi projects | 4 |

## Naming Conventions

`electronics-robotics` uses **hyphens**: `module-1-name/`, `lesson-01-name.md`

All other courses use **underscores**: `module_01_name/`, `lesson_01_name.md`

## Content Architecture

### Lesson File Structure (Markdown courses)

Every lesson `.md` follows this section order:
1. Metadata block (Module, Difficulty, Session Time, Age, XP Available)
2. `## Your Mission Today`
3. `## Learning Objectives`
4. `## What You Need`
5. `## How to Teach This Lesson` (numbered Steps with time, dialogue, XP awards)
6. `## Quick Quiz`
7. Badge unlock block (ASCII art)
8. XP Breakdown table
9. `## Coming Up Next...`
10. `## Troubleshooting` (where applicable)
11. `## Navigation` footer (Previous ← | → Next)

### Python Course Structure (different from others)

Lessons are **directories**, not files. Each lesson dir contains `.py` example files and an `exercise_*.py`. Each module has a `quiz_and_challenge/` subdirectory with `quiz.py` and `challenge.py`.

### Electronics-Robotics Assets

Images live in `module-X-name/images/` and are referenced as `images/filename.png` (relative). When adding images, always place them in the `images/` subfolder and use the `images/` prefix in the Markdown reference.

## Gamification System

All courses share the same XP + badge pattern:
- Each **step** within a lesson awards XP (`**Award: +XX XP**`)
- Each **lesson** unlocks one badge (shown as ASCII art block at the end)
- Each **module** has a README with a lesson table, XP totals, badge tracker, and XP rank progression
- When adding a new lesson, update the module README: lesson table, total XP, badge list, and XP rank thresholds

## Image Workflow

When adding images to a lesson:
1. Place image files in `module-X-name/images/`
2. Reference as `![Alt Text](images/filename.png)` — never a bare filename
3. Position images **before** the ASCII diagram they illustrate, not after
4. For cross-module reuse (e.g., Ohm's Law appears in Module 1 and Module 2): reference with relative path `../module-1-name/images/filename.png` — never duplicate the image file

### Image Prompt Generation

When creating a new lesson or adding images to an existing lesson, always generate image prompts. Each prompt must specify:
- **Filename**: `lesson-NN-descriptive-name.png`
- **Placement**: which step/heading it precedes in the lesson
- **Prompt content**: art style (bright flat-design, kid-friendly, ages 6–12), the electronics concept, the lesson's analogy as the visual metaphor, labeled components, consistent color coding (red/orange = power, blue = current, green = ground), and a cheerful mood with cartoon characters

Aim for 2–4 images per lesson. Use the `kiddo-course-builder` agent for full prompt generation.

## Lesson Numbering

If a lesson is inserted mid-sequence:
- Rename all subsequent lesson files (`lesson-04-` → `lesson-05-` etc.)
- Rename corresponding image files in `images/` to match
- Update image path references inside renamed lesson files
- Update lesson number headings inside the files
- Update all `## Coming Up Next...` sections in the chain
- Update the module README: lesson table, badge table, total XP, XP rank thresholds
