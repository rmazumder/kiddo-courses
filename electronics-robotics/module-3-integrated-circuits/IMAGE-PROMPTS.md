# Module 3 -- Image Generation Prompts
**Module:** Integrated Circuits (Lessons 17--24)
**Images folder:** `module-3-integrated-circuits/images/`
**Total images:** 21

---

## Table of Contents

- [Lesson 17: What is an Integrated Circuit?](#lesson-17-what-is-an-integrated-circuit) (3 images)
- [Lesson 18: 555 Timer Astable -- Blinker Mode](#lesson-18-555-timer-astable----blinker-mode) (3 images)
- [Lesson 19: 555 Timer Monostable -- One-Shot Mode](#lesson-19-555-timer-monostable----one-shot-mode) (3 images)
- [Lesson 20: Logic Gates AND, OR, NOT](#lesson-20-logic-gates-and-or-not) (3 images)
- [Lesson 21: Logic Gates NAND, NOR, XOR](#lesson-21-logic-gates-nand-nor-xor) (3 images)
- [Lesson 22: Seven-Segment Display](#lesson-22-seven-segment-display) (2 images)
- [Lesson 23: Counter LED Chaser](#lesson-23-counter-led-chaser) (2 images)
- [Lesson 24: Digital Dice Project](#lesson-24-digital-dice-project) (2 images)

---

## Lesson 17: What is an Integrated Circuit?

### Filename: `lesson-17-city-on-a-chip.png`
**Place in lesson:** Before Step 2, at the start of "The City Analogy" section
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A giant magnifying glass hovers over a black IC chip, revealing a miniature cartoon city inside the chip: tiny houses labeled "Transistor," roads labeled "Wire," bridges labeled "Resistor," and streetlights labeled "Diode," all printed on a green silicon landscape. A cheerful cartoon kid in safety goggles holds the magnifying glass with a look of wonder. Use color coding: red/orange paths for power lines, blue paths for signal roads, green ground areas, and yellow streetlights for outputs. The outer chip has eight metal legs sticking out, labeled "Pins." All text is short labels only, no paragraphs.

### Filename: `lesson-17-555-pin-diagram.png`
**Place in lesson:** Before the Pin 1 identification activity in Step 2
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large, clean top-view diagram of a 555 timer IC chip with the U-shaped notch clearly visible at the top and a dot near Pin 1. Each of the eight pins is labeled with its number and name: Pin 1 GND (green), Pin 2 TRIGGER (blue), Pin 3 OUTPUT (yellow), Pin 4 RESET (blue), Pin 5 CONTROL (blue), Pin 6 THRESHOLD (blue), Pin 7 DISCHARGE (blue), Pin 8 VCC (red/orange). A friendly cartoon robot points at Pin 1 with a speech bubble reading "Start here!" The counting direction (counter-clockwise) is shown with curved arrows. Use color coding: red/orange for power pin 8, green for ground pin 1, yellow for output pin 3, blue for all other signal pins. Labels only, no paragraphs.

### Filename: `lesson-17-ic-on-breadboard.png`
**Place in lesson:** Before the wiring steps in Step 4, "Hands-On -- Place the IC on the Breadboard"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A top-down view of a breadboard showing a 555 IC chip straddling the center gap correctly, with the notch facing up. The left row of pins sits on the left side and the right row on the right side, each in its own row of holes. Two jumper wires are shown: a red/orange wire from Pin 8 to the positive power rail labeled "VCC +9V," and a green wire from Pin 1 to the negative rail labeled "GND." A cheerful cartoon cat wearing a lab coat gives a thumbs-up and a label reads "Straddle the gap!" The center gap is highlighted with a glowing outline and labeled "Center Gap." Use color coding: red/orange for power rail and wire, green for ground rail and wire. Labels only, no paragraphs.

---

## Lesson 18: 555 Timer Astable -- Blinker Mode

### Filename: `lesson-18-heartbeat-pulse.png`
**Place in lesson:** Before Step 1, "Hook -- The Heartbeat of Electronics"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A split scene showing the heartbeat analogy: on the left, a cheerful cartoon kid places a hand on their chest with a red heart pulsing outward (labeled "Thump... Thump..."). On the right, a 555 timer chip with a matching red pulse wave coming out of Pin 3 labeled "OUTPUT," and the wave goes into an LED that alternates between a bright yellow glow labeled "ON" and a dim gray state labeled "OFF." A continuous pulse waveform connects both sides along the bottom, labeled "Astable = never stops." Use color coding: red/orange for the heartbeat and power, yellow for the LED output glow, blue for the pulse wave signal. Labels only, no paragraphs.

### Filename: `lesson-18-bucket-trap-door.png`
**Place in lesson:** Before the circuit diagram in Step 2, "The Bucket Analogy"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A four-panel comic strip showing the bucket analogy for the 555 astable circuit. Panel 1: a bucket with a narrow hose at the top labeled "R1 + R2 (Resistors)" slowly filling with blue water labeled "Capacitor Charging." Panel 2: the water reaches a red line near the top labeled "2/3 VCC" and a trap door flips open, labeled "555 Flips!" Panel 3: the water dumps out through a pipe labeled "R2 (Discharge)" while an LED nearby turns yellow and is labeled "LED ON." Panel 4: the bucket is nearly empty at a green line labeled "1/3 VCC" and starts filling again, labeled "Repeat Forever!" A cheerful cartoon robot watches the cycle with a clipboard. Use color coding: red/orange for threshold lines, blue for water/current, green for ground/bottom, yellow for LED output. Labels only, no paragraphs.

### Filename: `lesson-18-astable-circuit-labeled.png`
**Place in lesson:** Before the step-by-step wiring instructions in Step 3, "Build the Blinker Circuit"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled schematic-style breadboard wiring diagram of the 555 astable blinker circuit. The 555 IC chip sits in the center straddling the gap with all pins numbered. Component labels are large and clear: R1 (1k-ohm) in red/orange connecting VCC to Pin 7, R2 (10k-ohm) in red/orange connecting Pin 7 to Pin 6, C1 (47uF capacitor) in blue connecting Pin 2/6 to GND, a small C2 (0.01uF) in blue on Pin 5 to GND, and an LED with a 330-ohm resistor on Pin 3 glowing yellow labeled "OUTPUT." The positive power rail is red/orange labeled "+9V" and the ground rail is green labeled "GND." A cheerful cartoon fox with a screwdriver stands beside the breadboard. Use color coding: red/orange for resistors and power, blue for capacitors and current path, green for ground, yellow for the LED output. Labels only, no paragraphs.

---

## Lesson 19: 555 Timer Monostable -- One-Shot Mode

### Filename: `lesson-19-egg-timer-analogy.png`
**Place in lesson:** Before the circuit diagram in Step 2, "The Egg Timer Analogy"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large, cheerful cartoon egg timer character with a friendly face, arms, and legs. The timer's dial is labeled with "R" and "C" values on the rotating knob (showing "100k" and "47uF" as settings). Three stages are shown left to right: Stage 1, a hand twists the knob labeled "Button Press = Start!" Stage 2, the timer is counting down with a blue progress arc and a yellow LED glowing above it, labeled "Output HIGH -- LED ON." Stage 3, the timer rings "DING!" with the LED now gray, labeled "Time Up -- Output LOW." A cheerful cartoon kid watches the three stages. Use color coding: red/orange for the power/start action, blue for the timing arc/current, yellow for the LED output, green for the finished/ground state. Labels only, no paragraphs.

### Filename: `lesson-19-voltage-timeline.png`
**Place in lesson:** Before the measurement activity in Step 5, "Wand Check -- Measure the Timed Pulse"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large, clean voltage-over-time graph showing the monostable one-shot pulse. The horizontal axis is labeled "Time" with tick marks, and the vertical axis is labeled "Voltage" with "0V" at the bottom (green) and "~9V" at the top (red/orange). The timeline shows three phases: first a flat line at 0V labeled "Waiting," then a vertical jump up when a cartoon button is pressed labeled "Button Press! Trigger," then a flat HIGH line at 9V labeled "Output HIGH -- LED ON (5.17 seconds)," then a vertical drop back to 0V labeled "Time Up -- LED OFF." Below the main graph, a smaller blue curve shows the capacitor voltage slowly rising from 0V to a dashed line labeled "2/3 VCC" during the HIGH period. A cheerful cartoon owl with a multimeter points at the graph. Labels only, no paragraphs.

### Filename: `lesson-19-monostable-circuit.png`
**Place in lesson:** Before the step-by-step wiring in Step 3, "Build the One-Shot Circuit"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled breadboard wiring diagram of the 555 monostable circuit. The 555 IC sits in the center with all pins numbered. Key components are labeled: R (100k-ohm) in red/orange between VCC and Pin 6/7, C (47uF) in blue between Pin 6/7 and GND with a "+" polarity mark shown, a push button connecting Pin 2 to GND with a 10k pull-up resistor to VCC in red/orange, and a 330-ohm resistor plus LED on Pin 3 glowing yellow labeled "OUTPUT." Pin 4 (RESET) connects to VCC with a red/orange wire. The positive power rail is red/orange labeled "+9V" and the ground rail is green labeled "GND." A cheerful cartoon bear holds a stopwatch. Use color coding: red/orange for resistors and power, blue for the capacitor and current path, green for ground, yellow for the LED output. Labels only, no paragraphs.

---

## Lesson 20: Logic Gates AND, OR, NOT

### Filename: `lesson-20-three-gate-comic.png`
**Place in lesson:** Before Step 2, as the visual introduction to all three gates after the Hook
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A three-panel comic strip introducing the three basic logic gates using analogies. Panel 1 "AND": a treasure chest with two locks, two cheerful cartoon kids each holding a key labeled "A" and "B," and the chest only opens when both keys are inserted; a mini truth table shows "Both keys = OPEN!" Panel 2 "OR": a room with two doors labeled "Door A" and "Door B," a cartoon kid walks through one door with a label "Either door = IN!" and a mini truth table beside it. Panel 3 "NOT": a cartoon kid looks in a magic mirror; the kid's hand is up (labeled "1") but the reflection's hand is down (labeled "0"), with a label "Mirror shows OPPOSITE!" Each panel has a colored header: AND in red/orange, OR in blue, NOT in yellow. Use color coding throughout. Labels only, no paragraphs.

### Filename: `lesson-20-truth-tables-visual.png`
**Place in lesson:** Before the Wand Check in Step 5, as a summary reference of all three truth tables
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. Three large, side-by-side truth tables for AND, OR, and NOT gates, each styled as a colorful card. The AND card has a red/orange border and shows inputs A and B with the output column, with the single "1" output row highlighted in yellow. The OR card has a blue border and shows inputs A and B with output, with three "1" output rows highlighted in yellow. The NOT card has a green border and shows one input column and one output column with the two opposite values highlighted. Above each card is the gate's standard logic symbol drawn in a friendly, rounded cartoon style. A cheerful cartoon robot stands between the cards pointing at them like a teacher. LED icons beside each output row show yellow glow for "1" and gray for "0." Use color coding: red/orange for AND, blue for OR, green for NOT, yellow for active outputs. Labels only, no paragraphs.

### Filename: `lesson-20-and-gate-breadboard.png`
**Place in lesson:** Before the build instructions for the AND gate in Step 2
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled breadboard wiring diagram showing the 7408 AND gate IC on a breadboard with the notch facing up. Pin 14 is connected to a red/orange power rail labeled "+5V" and Pin 7 to a green ground rail labeled "GND." Two push buttons labeled "Input A" and "Input B" connect to Pins 1 and 2 through red/orange wires, each with a 10k pull-down resistor shown in blue going to GND. Pin 3 (Output) connects through a 330-ohm resistor to an LED glowing yellow, labeled "Output LED." Both buttons are shown in the "pressed" position with the LED ON, and a small truth table callout shows "A=1, B=1, OUT=1." A cheerful cartoon dog wearing goggles watches the circuit. Use color coding: red/orange for power and input wires, blue for pull-down resistors and current, green for ground, yellow for the output LED. Labels only, no paragraphs.

---

## Lesson 21: Logic Gates NAND, NOR, XOR

### Filename: `lesson-21-gate-family-reunion.png`
**Place in lesson:** Before Step 1, "Hook -- The Gate Family Reunion"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A "family reunion" scene showing six cartoon gate characters standing together on a grassy field under a banner reading "The Gate Family." Each character is shaped like its standard logic symbol with a friendly face, arms, and legs. AND (red/orange, strong arms) stands next to NAND (red/orange with a "rebel" leather jacket and an inversion bubble on its nose). OR (blue, wide open arms) stands next to NOR (blue with arms crossed and an inversion bubble). NOT (green, holding a mirror) stands next to XOR (yellow, wearing detective sunglasses). Each character has a name tag and its truth table printed on its chest like a t-shirt design. A cheerful cartoon kid stands in front taking a group photo. Use color coding: red/orange for AND/NAND, blue for OR/NOR, green for NOT, yellow for XOR. Labels only, no paragraphs.

### Filename: `lesson-21-xor-hallway-light.png`
**Place in lesson:** Before the XOR build section in Step 4
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A four-panel diagram showing the XOR gate as a hallway light with two switches. Each panel shows a simple hallway with a light bulb in the center and two toggle switches labeled "Switch A" and "Switch B" on opposite walls. Panel 1: both switches DOWN (0,0), light OFF (gray bulb). Panel 2: Switch A UP, Switch B DOWN (1,0), light ON (yellow glowing bulb). Panel 3: Switch A DOWN, Switch B UP (0,1), light ON (yellow glowing bulb). Panel 4: both switches UP (1,1), light OFF (gray bulb). Below the panels is a truth table matching each scenario. A label reads "XOR = Different positions means LIGHT ON!" A cheerful cartoon cat stands in the hallway. Use color coding: red/orange for switch wires, blue for current flow paths, yellow for the lit bulb, green for ground connections. Labels only, no paragraphs.

### Filename: `lesson-21-nand-as-not.png`
**Place in lesson:** Before the "NAND is Universal" demonstration in Step 2
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A visual proof that a NAND gate can act as a NOT gate. On the left, a large cartoon NAND gate character (red/orange, wearing a rebel jacket) has both its inputs tied together with a blue wire, labeled "Inputs joined together." An arrow points right to a cartoon NOT gate character (green, holding a mirror), with an equals sign between them and the label "NAND becomes NOT!" Below, a mini truth table shows: Input 0 tied to both A and B gives Output 1, and Input 1 tied to both gives Output 0, matching the NOT behavior. A cheerful cartoon kid holds a banner reading "NAND is the Universal Gate!" with smaller icons of AND, OR, and NOT gates all built from NAND gates shown as tiny diagrams. Use color coding: red/orange for NAND, green for NOT, blue for connecting wires, yellow for output signals. Labels only, no paragraphs.

---

## Lesson 22: Seven-Segment Display

### Filename: `lesson-22-segments-labeled.png`
**Place in lesson:** Before Step 2, "Which Segments Make Which Numbers?"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large 7-segment display drawn in the center with each segment clearly labeled: segment "a" at the top (red/orange), "b" upper-right (red/orange), "c" lower-right (blue), "d" at the bottom (blue), "e" lower-left (green), "f" upper-left (green), and "g" in the middle (yellow). Next to the large display, a grid shows all ten digits 0 through 9, each drawn as a small 7-segment display with the active segments filled in brightly and inactive segments shown as faint gray outlines. Each small display has its digit number below it. A cheerful cartoon robot points at the large display with labels showing "7 bars = any digit!" A label at the top reads "The 7-Segment Display." Use color coding: segments use a rainbow scheme to distinguish them, with active segments in bright colors and inactive in light gray. Labels only, no paragraphs.

### Filename: `lesson-22-bcd-decoder.png`
**Place in lesson:** Before the 7447 decoder wiring in Step 3
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A block diagram showing how a BCD decoder drives a 7-segment display. On the left, four large push buttons or DIP switches are labeled "Bit 3," "Bit 2," "Bit 1," "Bit 0" with binary values (each showing 0 or 1). Arrows flow into a large friendly box in the center shaped like the 7447 IC, labeled "BCD Decoder (7447)" with a smiling face. Arrows flow out from the decoder to a 7-segment display on the right showing the digit "5" with segments a, c, d, f, g lit up in yellow. Below the display, a conversion label reads "0101 (binary) = 5 (decimal)." A cheerful cartoon kid flips the switches while watching the display change. Use color coding: red/orange for the input switches and power, blue for the signal arrows/current flow, yellow for the lit segments on the display, green for ground connections. Labels only, no paragraphs.

---

## Lesson 23: Counter LED Chaser

### Filename: `lesson-23-train-block-diagram.png`
**Place in lesson:** Before Step 2, "Meet the 4017 Decade Counter"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A cartoon train diagram representing the 555 + 4017 LED chaser circuit. The locomotive at the left is shaped like a 555 timer IC labeled "555 Timer Engine" with puffs of red/orange smoke labeled "Clock Pulses." Connected behind it is a ticket counter car shaped like the 4017 IC labeled "4017 Ticket Counter" with a display showing numbers 0 through 9 cycling. Behind the counter car are ten small train station platforms in a row, each with an LED on top labeled "LED 0" through "LED 9." Only one LED glows yellow at a time (LED 3 in this frame), and a blue arrow shows the direction of the light sweep. A cheerful cartoon conductor waves from the 555 engine. Tracks run underneath labeled "Signal Path." Use color coding: red/orange for the 555 clock engine and power, blue for the signal/current flow arrows, yellow for the active LED, green for the ground rail/tracks. Labels only, no paragraphs.

### Filename: `lesson-23-chaser-wiring.png`
**Place in lesson:** Before the step-by-step wiring in Step 3, "Build the LED Chaser"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled breadboard wiring diagram showing the complete 555 + 4017 LED chaser circuit. The 555 timer IC is on the left side of the breadboard with R1 (1k-ohm) and R2 (10k-ohm) in red/orange and C1 (10uF) in blue, connected in astable configuration. Pin 3 (Output) of the 555 connects via a blue wire to Pin 14 (Clock) of the 4017 on the right side. The 4017 IC has ten output wires, each going through a 330-ohm resistor to an LED. The ten LEDs are arranged in a row at the top of the breadboard, and the third LED glows yellow to show the chase effect. Power rails are labeled: red/orange "+9V" and green "GND." Both ICs show pin numbers. A cheerful cartoon fox stands beside the breadboard holding a disco ball. Use color coding: red/orange for power and resistors, blue for clock signal and capacitors, yellow for the active LED, green for ground. Labels only, no paragraphs.

---

## Lesson 24: Digital Dice Project

### Filename: `lesson-24-dice-face-layout.png`
**Place in lesson:** Before the LED assignment table in Phase 1, "Plan the Dice Face"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large square dice face showing the standard seven LED positions arranged in a 3x3 grid, with corner and center positions labeled A through G: A (top-left), B (top-right), C (middle-left), G (center), D (middle-right), E (bottom-left), F (bottom-right). Six smaller dice faces surround the large one in a row, each showing a different dice number from 1 to 6 with the correct LEDs lit in yellow and unlit LEDs in gray. Each small face is labeled with its number and which LEDs are on: "1: G," "2: B, E," "3: B, G, E," "4: A, B, E, F," "5: A, B, G, E, F," "6: A, B, C, D, E, F." A cheerful cartoon kid rolls an imaginary dice. Use color coding: yellow for active/lit LEDs, gray for inactive positions, red/orange border on the main dice face, blue labels for LED names. Labels only, no paragraphs.

### Filename: `lesson-24-system-block-diagram.png`
**Place in lesson:** Before Phase 2 wiring, after the "How the Digital Dice Works" block diagram
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A complete system block diagram for the digital dice project, flowing left to right. Block 1: a large push button labeled "ROLL Button" in red/orange with a cartoon hand pressing it. Arrow flows to Block 2: a 555 timer IC labeled "555 Fast Clock" in red/orange with a tiny pulse wave above it. Arrow flows to Block 3: a 4017 counter IC labeled "4017 Counter (1-6)" in blue with numbers 1 through 6 cycling inside. Arrow flows to Block 4: a group of diodes labeled "LED Pattern Logic" in yellow with criss-crossing wires. Arrow flows to Block 5: seven LEDs arranged in a dice pattern inside a cardboard dice housing, showing the number 5 with five yellow glowing LEDs. At the bottom, a power supply block shows a 9V battery in red/orange connected to everything. A cheerful cartoon robot displays the finished dice project. Use color coding: red/orange for power and the 555, blue for the 4017 counter and signal flow, yellow for the LED pattern logic and outputs, green for ground connections. Labels only, no paragraphs.
