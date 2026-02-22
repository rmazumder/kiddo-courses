# Lesson 9: Project -- The Quiz Board Game

**Module:** 1 -- Electronic Components Basics (FINAL PROJECT)
**Difficulty:** Star-2 Easy-Medium
**Session Time:** 60--75 minutes (longer -- it is a project!)
**Age:** 6--12 years
**XP Available:** 500 XP (the biggest XP haul of the module!)

---

## Your Mission Today

This is it, Circuit Explorer -- the GRAND FINALE of Module 1! You are going to build a real, working **Quiz Board game** using everything you have learned: resistors, LEDs, wires, circuits, and of course, your trusty Magic Measurement Wand. When you are done, you will have a game you can play with friends and family. Let us do this!

---

## Learning Objectives

This project brings together everything from Module 1:
- Components: resistors, LEDs, battery, wires
- Circuits: complete loops, parallel connections
- Breadboard skills
- Multimeter skills: continuity mode for debugging
- Critical thinking to design your own quiz questions

---

## What You Need

| Item | Qty |
|------|-----|
| Cardboard (A3 or larger) | 1 piece |
| 9V battery + clip | 1 |
| LEDs (green + red) | 3 each |
| 330-ohm resistors | 6 |
| Jumper wires or solid copper wire | lots |
| Aluminum foil strips | 10 |
| Brass paper fasteners (split pins) or paperclips | 20 |
| Tape (electrical or masking) | 1 roll |
| Pen/marker for writing questions | 1 |
| Scissors | 1 |
| Multimeter (Magic Measurement Wand) | 1 |
| Hot glue gun (adult handles) | optional |

---

## What Is a Quiz Board?

A quiz board is a classic electronics project where:
- Questions are listed on the left column
- Answers are listed on the right column (scrambled!)
- Hidden wires connect each question to its correct answer on the back
- Touch a question and an answer with two probes -- if correct, the LED lights up!

```
  Quiz Board layout:

  +---------------------------------------------+
  |                                             |
  |  Q1: Unit of resistance?       *  *  A3: Ohm          |
  |                                             |
  |  Q2: What stores charge?       *  *  A1: Capacitor     |
  |                                             |
  |  Q3: Positive LED leg?         *  *  A4: The long leg  |
  |                                             |
  |  Q4: What does LED mean?       *  *  A2: Light Emitting Diode |
  |                                             |
  |              [LED indicator]                |
  |              [Battery box]                  |
  +---------------------------------------------+
```

---

## How to Build It

### Phase 1: Plan the Quiz (10 min)

**Let the kid write their own questions!** This makes them review what they learned.

Suggestions for ages 6--8:
1. What color is the positive wire of a battery? *(Red)*
2. What does a resistor do? *(Slows down current)*
3. Which leg of the LED is longer? *(The positive one)*
4. What tool can see invisible electricity? *(The multimeter / Magic Measurement Wand)*
5. What do you call the path electricity travels? *(A circuit)*

Suggestions for ages 9--12:
1. What is the unit of resistance? *(Ohms)*
2. Which component stores electrical charge? *(Capacitor)*
3. What does the middle leg of a transistor do? *(Controls the transistor -- it is the Base)*
4. What are the three superpowers of the multimeter? *(Voltage, resistance, continuity)*
5. What does LED stand for? *(Light Emitting Diode)*

**Write questions on the left side of the cardboard, scrambled answers on the right side.**

**Award: +30 XP for writing at least 5 quiz questions!**

---

### Phase 2: Make the Connection Points (10 min)

For each question-answer pair:

1. Push a **brass paper fastener** (or paperclip) through the cardboard at each question dot and answer dot
2. Bend the legs flat on the back to hold it in place
3. These are your **contact points** -- the player will touch these with probes

```
  Front of cardboard:           Back of cardboard:

  Q1: [question text]  *         *  A3: [answer text]
                      ^          ^
               paper fastener  paper fastener
               head (front)    head (front)
                      |          |
               legs bent flat on back
```

**Award: +20 XP for installing all connection points!**

---

### Phase 3: Wire the Correct Pairs (10 min)

On the **back** of the cardboard:

Connect each question's fastener to its correct answer's fastener with a wire (or foil strip):

```
  Back view:

  Q1_fastener ---------------------- A1_fastener   (Q1's correct answer)
  Q2_fastener ---------------------- A2_fastener
  Q3_fastener ---------------------- A3_fastener
  Q4_fastener ---------------------- A4_fastener
  Q5_fastener ---------------------- A5_fastener
```

**Use tape to keep wires flat and prevent them crossing to wrong fasteners.**

**Award: +30 XP for wiring all 5 pairs!**

---

### Phase 4: Wand Check -- Test Every Connection! (10 min)

> "Before we add the LED indicator, let us make sure every wire works. Time for your Magic Measurement Wand!"

Set the Wand to **continuity mode**.

**Test each pair from the FRONT of the board:**

1. Touch one probe to Q1's fastener head
2. Touch the other probe to the correct answer's fastener head
3. The Wand should BEEP! That means the hidden wire works.
4. Now touch Q1's fastener to a WRONG answer. No beep! Perfect.

**Do this for all 5 pairs:**

```
| Question | Correct Answer | Beep? | Wrong Answer Tested | No Beep? |
|----------|---------------|-------|--------------------|----|
| Q1       |               |       |                    |    |
| Q2       |               |       |                    |    |
| Q3       |               |       |                    |    |
| Q4       |               |       |                    |    |
| Q5       |               |       |                    |    |
```

> "You just did what professional engineers do: testing before powering on. If any pair does not beep, check the wire on the back -- it might be loose."

**Award: +50 XP for testing all 5 pairs with the Wand!**

---

### Phase 5: Build the Indicator Circuit (15 min)

The indicator sits at the bottom of the board. When a correct match is made, it completes the circuit and lights up.

```
  How it works:

  9V (+) ---- wire to PROBE 1 (held by player)

  PROBE 1 touches Q-fastener
    +--- hidden wire --> correct A-fastener
         PROBE 2 touches A-fastener ---- [330-ohm] ---- GREEN LED ---- 9V (-)

  If CORRECT match: complete circuit -- LED lights!
  If WRONG match:   circuit broken (wires don't connect) -- LED off
```

**Build on breadboard or directly on cardboard:**

```
  9V (+) ---- RED wire (this is PROBE 1)
  GREEN LED ---- 330-ohm ---- BLACK wire (this is PROBE 2) ---- 9V (-)
```

**Probes:** Two wires with bare ends -- the player holds one in each hand and touches the dots.

**Award: +40 XP for building the working indicator circuit!**

---

### Phase 6: Wand-Assisted Debugging (5 min)

> "If the LED does not light for a correct answer, do not panic! Grab your Wand and become a circuit detective."

**Debugging checklist using the Wand:**

1. **Battery check:** Set Wand to DC Volts. Measure the battery. Is it still above 8V?
2. **Wire check:** Set Wand to continuity. Test each probe wire -- does it beep end-to-end?
3. **Connection check:** Test from the fastener head on the front to the wire on the back. Beep?
4. **LED check:** Make sure the LED is not backwards (long leg = +)

> "Debugging is not failing -- it is SOLVING. Every engineer debugs. You are thinking like a real engineer right now!"

**Award: +30 XP for successfully debugging at least one issue (or confirming everything works)!**

---

### Phase 7: Decorate! (5 min)

Let the kid decorate the front of the board:
- Draw a title: "ELECTRONICS QUIZ MASTER!"
- Draw funny illustrations of components
- Color code the question and answer areas
- Add a scoreboard

**Award: +20 XP for decorating the board!**

---

## How to Play

**2-player version:**
1. Player 1 holds the two probe wires, one in each hand
2. Player 2 calls out a question number
3. Player 1 touches a question dot with one probe
4. Player 1 tries to find the matching answer dot with the other probe
5. Green light = CORRECT! Score a point!
6. Switch roles after 5 questions

**Solo version:**
- Race against a timer to match all 5 pairs as fast as possible

**Teach a friend:**
- Let the kid TEACH the questions to a younger sibling or parent
- Teaching is the best way to remember!

---

## Module 1 Final Assessment

After building the quiz board, have the kid answer these (no looking at notes!):

**Component Recognition** -- lay these on the table: resistor, capacitor, LED, transistor, diode, push button, potentiometer, buzzer, multimeter.

> "Point to and name each one."

**Concept Check:**
1. "What does a resistor do?"
2. "Which leg of an LED is the positive leg?"
3. "What is the unit of voltage? Resistance? Current?"
4. "What is a circuit?"
5. "What does a transistor do?"
6. "What are the three superpowers of the Magic Measurement Wand?"

**Wand Skills Check:**
> "Measure this battery for me." (Hand them a 9V battery)
> "Measure this resistor." (Hand them a 1k-ohm or 4.7k-ohm resistor)
> "Test this wire with continuity mode." (Hand them a jumper wire)

**Award: +50 XP for completing the final assessment!**

---

## Module 1 Complete -- Grand Finale!

```
  ======================================================

     MODULE 1 CHAMPION BADGE UNLOCKED!

     _____________________ has mastered
        Electronic Components Basics

     [check] Electricity and Circuits
     [check] Magic Measurement Wand (Multimeter)
     [check] Resistors and Color Codes
     [check] Capacitors
     [check] Diodes and LEDs
     [check] Transistors
     [check] Switches and Potentiometers
     [check] Buzzers and Sound
     [check] Built the Quiz Board!

  ======================================================
```

**Lesson 9 XP Breakdown:**
| Activity | XP |
|----------|-----|
| Write 5 quiz questions | 30 |
| Install connection points | 20 |
| Wire all 5 pairs | 30 |
| Wand Check (test all pairs) | 50 |
| Build indicator circuit | 40 |
| Wand debugging | 30 |
| Decorate | 20 |
| Final assessment | 50 |
| **TOTAL POSSIBLE** | **270** |

---

## Module 1 Total XP Summary

| Lesson | Title | Max XP |
|--------|-------|--------|
| 1 | What is Electricity? | 220 |
| 2 | Meet Your Magic Measurement Wand | 320 |
| 3 | Resistors | 250 |
| 4 | Capacitors | 210 |
| 5 | Diodes and LEDs | 190 |
| 6 | Transistors | 180 |
| 7 | Switches and Potentiometers | 200 |
| 8 | Buzzers and Sound | 190 |
| 9 | Quiz Board Project | 270 |
| **MODULE TOTAL** | | **2,030** |

**XP Ranks:**
- 0--500 XP: Circuit Apprentice
- 501--1,000 XP: Circuit Explorer
- 1,001--1,500 XP: Circuit Builder
- 1,501--1,800 XP: Circuit Engineer
- 1,801--2,030 XP: Circuit Champion!

---

## All Badges Earned in Module 1

| Badge | Lesson |
|-------|--------|
| Circuit Starter | Lesson 1 |
| Wand Wielder | Lesson 2 |
| Color Code Cracker | Lesson 3 |
| Energy Tank Explorer | Lesson 4 |
| Rainbow Builder | Lesson 5 |
| Transistor Tamer | Lesson 6 |
| Dial Master | Lesson 7 |
| Sound Engineer | Lesson 8 |
| Module 1 Champion | Lesson 9 |

---

## Reflection Questions (Talk Through Together)

> "What was the coolest thing you built this module?"
> "What was the hardest part to understand?"
> "Which Magic Measurement Wand superpower is your favorite?"
> "Is there anything you want to explore more before we move on?"
> "What do you think Module 2 will be about?"

---

## What's Next -- Module 2 Preview

> "Now you know all the components AND you know how to use your Magic Measurement Wand like a pro! In Module 2, we are going to learn how to COMBINE components into real circuits -- using proper rules and calculations. We will learn Ohm's Law, series vs. parallel circuits, and build a real blinking lighthouse circuit!"

---

## Parent/Instructor Notes

- This project takes longer than a regular lesson -- plan for 60--75 minutes or split across two sessions.
- The quiz board is a **great keepsake** -- kids often want to show it off to friends and family.
- The Wand-based debugging phase (Phase 6) is perhaps the most valuable learning moment in the entire module. Resist the urge to fix problems for the child -- guide them to use the multimeter to find and fix issues themselves.
- Encourage the kid to **add more questions** over time as they learn more.
- Consider having the child demonstrate the quiz board to another family member and explain how it works -- teaching solidifies learning.
- The XP totals across all 9 lessons can be tallied on a poster or whiteboard. Many kids become deeply motivated by seeing their cumulative score rise.
- Consider laminating the front of the quiz board if you want it to last!
