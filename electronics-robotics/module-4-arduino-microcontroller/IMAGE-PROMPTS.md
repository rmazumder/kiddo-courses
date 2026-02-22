# Module 4 -- Image Generation Prompts
**Module:** Arduino Microcontroller (Lessons 25--34)
**Images folder:** `module-4-arduino-microcontroller/images/`
**Total images:** 26

---

## Table of Contents

- [Lesson 25: What is a Microcontroller?](#lesson-25-what-is-a-microcontroller) (3 images)
- [Lesson 26: First Sketch -- Blink External LED](#lesson-26-first-sketch----blink-external-led) (2 images)
- [Lesson 27: Variables and Serial Monitor](#lesson-27-variables-and-serial-monitor) (3 images)
- [Lesson 28: Reading Digital Inputs (Buttons)](#lesson-28-reading-digital-inputs-buttons) (3 images)
- [Lesson 29: Analog Inputs](#lesson-29-analog-inputs) (2 images)
- [Lesson 30: PWM Dimming LEDs](#lesson-30-pwm-dimming-leds) (3 images)
- [Lesson 31: For Loops and Arrays](#lesson-31-for-loops-and-arrays) (3 images)
- [Lesson 32: Piezo Buzzer and Tones](#lesson-32-piezo-buzzer-and-tones) (2 images)
- [Lesson 33: LCD Display (16x2 with I2C)](#lesson-33-lcd-display-16x2-with-i2c) (3 images)
- [Lesson 34: Project -- Digital Piano](#lesson-34-project----digital-piano) (2 images)

---

## Lesson 25: What is a Microcontroller?

### Filename: `lesson-25-arduino-labeled-diagram.png`
**Place in lesson:** Before the pin-by-pin tour in Step 2, "Meet the Arduino Uno"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large, clean top-view diagram of an Arduino Uno board with every major section labeled. The USB port on the left is labeled "USB (Teaching Cable)" in blue with a cartoon cable plugging in. The top pin header shows digital pins 0 through 13, each labeled by number, with PWM-capable pins (3, 5, 6, 9, 10, 11) marked with a tilde symbol and a yellow star. The bottom-right header shows analog pins A0 through A5 labeled in blue. The power header shows pins labeled "5V" (red/orange), "3.3V" (red/orange), "GND" (green), and "Vin." The reset button is labeled "Reset" and the power LED is labeled "Power LED" in red/orange. The large ATmega328 chip in the center is labeled "The Brain (Microcontroller)." A cheerful cartoon robot sits on top of the board pointing at the brain chip. Use color coding: red/orange for power pins, blue for signal/data pins, green for ground pins, yellow for PWM-capable pins. Labels only, no paragraphs.

### Filename: `lesson-25-hidden-computers.png`
**Place in lesson:** Before Step 1, "Hook -- Spot the Hidden Computers"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A busy cartoon room scene showing everyday objects that contain hidden microcontrollers. A car dashboard has a glowing brain icon inside labeled "~100 computers!" A microwave on a kitchen counter has a tiny brain icon labeled "1 computer." An electric toothbrush in a cup has a brain icon labeled "1 computer." A TV remote on a couch has a brain icon labeled "1 computer." A washing machine has a brain icon labeled "1 computer." A game controller has a brain icon labeled "1 computer." Each brain icon is drawn as a small, friendly cartoon chip with a smiley face and tiny glowing yellow eyes. A cheerful cartoon kid stands in the middle of the room with a magnifying glass, discovering each hidden brain. A large counter in the corner reads "Total: 100+ computers in this room!" Use color coding: yellow for all brain/chip icons glowing, red/orange for power indicators on devices, blue for data connections, green for safe/ground elements. Labels only, no paragraphs.

### Filename: `lesson-25-robot-brain-analogy.png`
**Place in lesson:** Before the "Big Idea" paragraph in Step 1
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A friendly cartoon robot shown in a cutaway view revealing its internal structure as an analogy for the Arduino. The robot's head contains a glowing brain labeled "Processor (The Brain)" in yellow. Its chest has a filing cabinet labeled "Memory" in blue. Its left arm ends in an LED and is labeled "Output Pin" in yellow. Its right arm has a button sensor and is labeled "Input Pin" in blue. A USB cable plugs into the robot's back labeled "USB = Teaching Cable" in red/orange. The robot's feet are grounded with a green wire labeled "GND." A cheerful cartoon kid holds the USB cable like a leash, with a speech bubble saying "I teach it what to do!" The robot has friendly eyes and is waving. Use color coding: red/orange for power and USB, blue for input pins and memory, yellow for output pins and the brain glow, green for ground. Labels only, no paragraphs.

---

## Lesson 26: First Sketch -- Blink External LED

### Filename: `lesson-26-setup-vs-loop.png`
**Place in lesson:** Before the code explanation in Step 3, "Understand the Code"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A two-panel comparison showing the setup() and loop() concept. Left panel labeled "setup() -- Runs ONCE" shows a cartoon kid's morning routine: waking up, brushing teeth, and getting dressed, drawn as three sequential steps inside a single blue box with a "1x" badge. Right panel labeled "loop() -- Runs FOREVER" shows the same cartoon kid breathing in and out in a circular arrow pattern, drawn inside a yellow box with an infinity symbol badge. Between the panels, a large arrow flows from left to right labeled "First setup, then loop forever." Below, a simplified code snippet shows "void setup() { ... }" in a blue code block and "void loop() { ... }" in a yellow code block, connected by an arrow. A cheerful cartoon Arduino board character watches from the corner. Use color coding: blue for setup elements (one-time), yellow for loop elements (repeating), red/orange for the Arduino power indicator. Labels only, no paragraphs.

### Filename: `lesson-26-blink-wiring.png`
**Place in lesson:** Before the wiring steps in Step 2, "Build the Circuit"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled wiring diagram showing an Arduino Uno connected to a breadboard with an external LED circuit. A red/orange jumper wire runs from Arduino digital Pin 7 to a row on the breadboard. A 330-ohm resistor (labeled "330 ohm" with color bands shown) connects from that row to the next row. An LED sits in the next row with its long leg (+, anode) toward the resistor side and its short leg (-, cathode) labeled clearly. A green jumper wire runs from the LED's cathode row back to the Arduino GND pin. The LED glows yellow. The Arduino board is drawn in simplified form with Pin 7 and GND clearly highlighted. A cheerful cartoon cat points at the LED with a speech bubble reading "Pin 7 controls me!" Use color coding: red/orange for the signal wire from Pin 7, green for the ground wire, yellow for the LED glow, blue for the resistor current path. Labels only, no paragraphs.

---

## Lesson 27: Variables and Serial Monitor

### Filename: `lesson-27-variable-boxes.png`
**Place in lesson:** Before the code examples in Step 2, "What Are Variables?"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. Three large, colorful storage boxes sitting on a wooden shelf, each representing a different variable type. Box 1 is red/orange, labeled "int age" on the front with the number "8" visible inside, and a tag reading "Whole numbers." Box 2 is blue, labeled "String name" on the front with the word "Alex" visible inside on a slip of paper, and a tag reading "Text." Box 3 is yellow, labeled "bool isOn" on the front with a bright light bulb icon showing "true" inside, and a tag reading "True or False." Each box has a hinged lid that is partially open so you can see the contents. Above the shelf, a sign reads "Arduino's Memory Shelf." A cheerful cartoon robot is placing a new value into one of the boxes. Use color coding: red/orange for integer/number boxes, blue for string/text boxes, yellow for boolean boxes, green for the shelf/ground. Labels only, no paragraphs.

### Filename: `lesson-27-serial-monitor.png`
**Place in lesson:** Before the Serial Monitor activity in Step 3, "The Serial Monitor"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A cartoon laptop screen showing the Arduino Serial Monitor window. The monitor displays several lines of text from the Arduino: "Hello! I am Arduino," "Counter: 1," "Counter: 2," "Counter: 3," each appearing as if typed one after another in a dark console with bright green text. A USB cable in blue connects the laptop to an Arduino Uno board sitting beside it. The Arduino has a cartoon speech bubble with a waveform inside, representing data traveling through the USB cable. Small blue data dots travel along the cable from Arduino to laptop. The Serial Monitor window toolbar shows the baud rate "9600" highlighted in yellow. A cheerful cartoon kid sits at the laptop with wide, excited eyes reading the messages. Use color coding: blue for the USB cable and data flow, yellow for the highlighted baud rate and signal, red/orange for the Arduino power LED, green for the text on screen. Labels only, no paragraphs.

### Filename: `lesson-27-counter-sketch-flow.png`
**Place in lesson:** Before the counting experiment in Step 4, "Build a Counter"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A flowchart showing how a counting sketch works in Arduino. Step 1: a blue box labeled "setup()" contains "Serial.begin(9600)" and "int counter = 0." An arrow flows down to Step 2: a yellow box labeled "loop()" contains three sub-steps shown as smaller boxes inside: "counter = counter + 1" (a red/orange box with a +1 icon), then "Serial.println(counter)" (a blue box with a speech bubble icon), then "delay(1000)" (a green box with a clock icon showing 1 second). A large curved arrow loops from the bottom of the yellow box back to its top, labeled "Repeat forever." On the right side, a cartoon Serial Monitor window shows "1, 2, 3, 4, 5..." scrolling. A cheerful cartoon owl sits on top of the flowchart. Use color coding: blue for setup and serial communication, yellow for the loop box, red/orange for the counter increment, green for the delay/timing. Labels only, no paragraphs.

---

## Lesson 28: Reading Digital Inputs (Buttons)

### Filename: `lesson-28-pullup-logic.png`
**Place in lesson:** Before the wiring diagram in Step 2, "How Buttons Work with Arduino"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A two-panel diagram showing how INPUT_PULLUP works with a button. Left panel labeled "NOT PRESSED": a cartoon Arduino pin is connected to a gentle upward pull by a spring-like resistor labeled "Internal Pull-Up Resistor" going to a red/orange 5V cloud at the top. The button below is open (not touching). The pin reads "HIGH (5V)" shown in a red/orange badge. A cartoon current arrow tries to go down but the open button blocks it. Right panel labeled "PRESSED": the same layout but the button is now closed, creating a green path directly to a green GND cloud at the bottom. The current flows down through the button (shown as blue arrows) and the pin reads "LOW (0V)" shown in a green badge. A cheerful cartoon kid presses the button in the right panel. Use color coding: red/orange for 5V/HIGH state, green for GND/LOW state, blue for current flow arrows, yellow for the pin indicator. Labels only, no paragraphs.

### Filename: `lesson-28-if-else-fork.png`
**Place in lesson:** Before the if/else code explanation in Step 3, "Write the Code"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A cartoon road that splits into a fork, representing an if/else decision. At the fork, a large diamond-shaped sign reads "Button Pressed?" in yellow. The left road is labeled "YES (LOW)" and leads to a bright town with a glowing yellow LED labeled "LED ON!" and a cheerful cartoon kid celebrating. The right road is labeled "NO (HIGH)" and leads to a quiet town with a gray, unlit LED labeled "LED OFF" and a cartoon kid waiting patiently. A cartoon Arduino board character stands at the fork like a traffic officer, checking the button state. Above the fork, a simplified code snippet shows "if (buttonState == LOW) { LED ON } else { LED OFF }" in a clean code block. Use color coding: yellow for the decision diamond and the active LED path, blue for the current flow on the YES path, green for the ground connections, red/orange for the power source. Labels only, no paragraphs.

### Filename: `lesson-28-button-wiring.png`
**Place in lesson:** Before the build steps in Step 2, after the pull-up explanation
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean, labeled wiring diagram showing an Arduino Uno connected to a breadboard with a push button and LED. The push button connects Arduino Pin 2 to GND via a green wire, with "INPUT_PULLUP" labeled in a callout bubble near Pin 2 (no external resistor needed). A separate circuit shows Pin 7 connected via a red/orange wire to a 330-ohm resistor, then to an LED glowing yellow, then to GND via a green wire. The Arduino board is simplified with Pin 2, Pin 7, and GND clearly highlighted. The button is drawn large with labels showing "Press = connects Pin 2 to GND" and "Release = Pin 2 pulled HIGH by internal resistor." A cheerful cartoon robot presses the button with one hand while pointing at the LED with the other. Use color coding: red/orange for the LED signal wire, green for ground wires and button-to-GND connection, blue for the internal pull-up path (shown as a dotted line inside the Arduino), yellow for the LED glow. Labels only, no paragraphs.

---

## Lesson 29: Analog Inputs

### Filename: `lesson-29-digital-vs-analog.png`
**Place in lesson:** Before Step 1, "Hook -- The Light Switch Problem"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A side-by-side comparison of digital versus analog. Left side labeled "Digital (ON/OFF Only)": a simple wall light switch in two positions -- UP labeled "ON (HIGH = 5V)" in red/orange with a bright yellow light bulb, and DOWN labeled "OFF (LOW = 0V)" in green with a gray light bulb. A big "2 values" badge sits below. Right side labeled "Analog (Any Value In Between)": a dimmer knob/slider that smoothly goes from 0 to 1023, with a gradient bar showing dark at 0, medium brightness in the middle, and full brightness at 1023. The light bulb above the dimmer shows a smooth gradient from dim to bright in yellow. A big "1024 values!" badge sits below. A cheerful cartoon kid stands between both sides, turning the analog dimmer knob with a look of delight. Use color coding: red/orange for the ON/HIGH states, green for the OFF/LOW/zero states, yellow for the output light brightness gradient, blue for the analog value scale numbers. Labels only, no paragraphs.

### Filename: `lesson-29-potentiometer-reading.png`
**Place in lesson:** Before the measurement comparison in Step 4, "Wand Check"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A three-stage diagram showing a potentiometer connected to an Arduino analog pin. On the left, a large cartoon potentiometer knob has three wires: the left leg goes to a red/orange 5V rail, the right leg goes to a green GND rail, and the center wiper leg goes via a blue wire to Arduino pin A0. In the middle, the Arduino board is shown with pin A0 highlighted and a thought bubble showing "analogRead(A0)." On the right, a cartoon laptop shows the Serial Monitor displaying changing values. Three snapshots of the knob are shown: turned fully left reading "0" on the monitor, turned to the middle reading "512," and turned fully right reading "1023." Below each knob position, a voltage label shows "0V," "2.5V," and "5V" respectively. A cheerful cartoon owl perches on the potentiometer. Use color coding: red/orange for the 5V power connection, green for the GND connection, blue for the signal wire and data flow, yellow for the Serial Monitor output values. Labels only, no paragraphs.

---

## Lesson 30: PWM Dimming LEDs

### Filename: `lesson-30-pwm-signal-patterns.png`
**Place in lesson:** Before the code walkthrough in Step 2, "PWM Explained"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. Four horizontal bar charts stacked vertically, each showing a different PWM duty cycle as a repeating on/off pattern over time. Row 1 labeled "analogWrite(255) -- Full Brightness": solid yellow bars with no gaps, an LED icon on the right glowing full bright yellow. Row 2 labeled "analogWrite(127) -- Half Brightness": alternating yellow bars and gray gaps of equal width, an LED icon at medium brightness. Row 3 labeled "analogWrite(64) -- Quarter Brightness": narrow yellow bars with wide gray gaps, an LED icon at dim brightness. Row 4 labeled "analogWrite(0) -- OFF": all gray bars with no yellow, an LED icon that is dark gray. Each row has a percentage badge: "100% ON," "50% ON," "25% ON," "0% ON." A time axis runs along the bottom labeled "Time." A cheerful cartoon kid waves their hand fast in front of the LED to demonstrate the blur effect. Use color coding: yellow for ON bars and LED glow, gray for OFF periods, red/orange for the power line, blue for timing labels. Labels only, no paragraphs.

### Filename: `lesson-30-brightness-dial.png`
**Place in lesson:** Before the potentiometer-controlled brightness experiment in Step 4
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large circular dial in the center labeled "analogWrite Brightness" with numbers around the edge from 0 at the bottom (green, labeled "OFF") through 64, 127, 191, to 255 at the top (red/orange, labeled "FULL BRIGHT"). A pointer on the dial points to about 180. Around the dial, five LED icons at different brightness levels correspond to dial positions: fully dark gray at 0, dim yellow at 64, medium yellow at 127, bright yellow at 191, and blazing yellow with glow rays at 255. An Arduino board is connected to the dial with a wire from a PWM pin (marked with a tilde ~) in blue. A cheerful cartoon robot turns the dial knob. Use color coding: red/orange for the maximum/power end of the dial, green for the zero/off end, yellow for LED brightness levels, blue for the PWM signal wire. Labels only, no paragraphs.

### Filename: `lesson-30-fade-circuit.png`
**Place in lesson:** Before the fade code in Step 3, "Build the Fade Effect"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A wiring diagram showing an Arduino Uno connected to a breadboard with an LED fade circuit. A blue wire runs from Arduino PWM Pin 9 (highlighted with a tilde ~ symbol and a yellow star labeled "PWM Pin") to a 330-ohm resistor on the breadboard. The resistor connects to an LED that is shown in mid-fade with a gradient glow from dim to bright in yellow. A green wire connects from the LED cathode back to Arduino GND. To the right, a small animation sequence shows the LED in five frames: dark, dim, medium, bright, full glow, then back down, labeled "Fade In... Fade Out..." with curved arrows showing the breathing pattern. The code "analogWrite(9, brightness);" appears in a small code callout. A cheerful cartoon firefly character floats near the LED. Use color coding: blue for the PWM signal wire, yellow for the LED glow gradient, green for the ground wire, red/orange for the Arduino power LED. Labels only, no paragraphs.

---

## Lesson 31: For Loops and Arrays

### Filename: `lesson-31-stair-climbing-loop.png`
**Place in lesson:** Before the for loop explanation in Step 2, "What Is a For Loop?"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A cartoon staircase with six steps, each step numbered 0 through 5, representing a for loop counting from 0 to 5. A cheerful cartoon kid climbs the stairs, currently standing on step 3. Each step has a label: step 0 says "i = 0 (Start)," step 1 says "i = 1," step 2 says "i = 2," and so on up to step 5 which says "i = 5 (Stop!)." At the bottom of the stairs, a sign reads "for (int i = 0; i < 6; i++)" with three parts color-coded: "i = 0" in green labeled "Start here," "i < 6" in red/orange labeled "Keep going until...," and "i++" in blue labeled "Step up by 1." At the top of the stairs, a finish flag and a yellow LED glow. Each step lights up in yellow as the kid passes it. Use color coding: green for the starting condition, red/orange for the stopping condition, blue for the increment step, yellow for each activated step/LED. Labels only, no paragraphs.

### Filename: `lesson-31-array-boxes.png`
**Place in lesson:** Before the array code example in Step 3, "What Is an Array?"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A row of six colorful boxes sitting on a shelf, representing the array "int leds[] = {3, 5, 6, 9, 10, 11}." Each box is labeled on top with its index number: [0], [1], [2], [3], [4], [5]. Inside each box, the pin number is written large: 3, 5, 6, 9, 10, 11. Below the shelf, six LEDs are drawn, each connected by a colored wire to its corresponding box: LED on pin 3 connects to box [0], LED on pin 5 connects to box [1], and so on. The shelf has a large label reading "leds[]" on the front. A cartoon robot hand reaches for box [2] with a callout showing "leds[2] = 6" meaning "get pin 6." A cheerful cartoon kid points at the array with a speech bubble reading "One name, six values!" Use color coding: each box is a different bright color from the rainbow, yellow for the LED glows, blue for the connecting wires, red/orange for the array name label. Labels only, no paragraphs.

### Filename: `lesson-31-knight-rider-sequence.png`
**Place in lesson:** Before the Knight Rider code in Step 4, "Build the Knight Rider Scanner"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A six-LED light bar at the top of the image shows the Knight Rider scanning effect. Six LEDs are arranged in a horizontal row, each labeled with its pin number (3, 5, 6, 9, 10, 11) and array index ([0] through [5]). Three frames of animation are shown vertically: Frame 1 shows LED [2] lit in bright yellow with a motion trail to the left, labeled "i = 2, scanning right." Frame 2 shows LED [4] lit in bright yellow with a trail, labeled "i = 4, scanning right." Frame 3 shows LED [3] lit in bright yellow with a trail going left, labeled "i = 3, scanning back left." Blue arrows show the sweep direction between frames. Above the light bar, a for loop counter shows "for (int i = 0; i < 6; i++)" with the current value of i highlighted in red/orange for each frame. A cheerful cartoon car with a glowing front scanner bar drives below. Use color coding: yellow for the active LED and glow trails, blue for the sweep direction arrows, red/orange for the loop counter highlight, green for inactive LEDs. Labels only, no paragraphs.

---

## Lesson 32: Piezo Buzzer and Tones

### Filename: `lesson-32-frequency-pitch-chart.png`
**Place in lesson:** Before the note frequency table in Step 2, "Wire the Buzzer"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A colorful frequency-to-pitch chart showing one octave of musical notes from C4 to C5. On the left, a simplified musical staff shows eight notes ascending. Each note has a horizontal bar extending to the right, forming a bar chart where bar length represents frequency. The bars are rainbow-colored from red (C4 = 262 Hz) through orange (D4 = 294 Hz), yellow (E4 = 330 Hz), green (F4 = 349 Hz), teal (G4 = 392 Hz), blue (A4 = 440 Hz), indigo (B4 = 494 Hz), to violet (C5 = 523 Hz). Each bar is labeled with the note name and its frequency in Hz. A cartoon sound wave gets tighter/faster as pitch increases, shown as a visual along the right side. A cheerful cartoon bird sits on the musical staff singing. At the bottom, a label reads "Higher Hz = Higher Pitch!" Use color coding: rainbow gradient for the note bars, yellow sound wave lines emanating from higher notes, blue for the frequency numbers. Labels only, no paragraphs.

### Filename: `lesson-32-buzzer-wiring.png`
**Place in lesson:** Before the wiring instructions in Step 2, "Wire the Buzzer"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean wiring diagram showing an Arduino Uno connected to a piezo buzzer on a breadboard. A blue wire runs from Arduino digital Pin 8 (labeled "Pin 8 -- tone() output") to the positive leg of the piezo buzzer, which is drawn as a round, friendly cartoon disc with a smiley face. A green wire runs from the buzzer's other leg to Arduino GND. Yellow cartoon sound waves radiate outward from the buzzer in concentric arcs, labeled "Sound!" A small code callout shows "tone(8, 440);" with "440 Hz = Note A" labeled beside it. To the right, a second small diagram shows a push button connected to Pin 2 for triggering notes on demand, labeled "Optional: Button to play." A cheerful cartoon kid covers one ear playfully while the buzzer plays. Use color coding: blue for the signal wire from Pin 8, green for the ground wire, yellow for the sound waves, red/orange for the Arduino power LED. Labels only, no paragraphs.

---

## Lesson 33: LCD Display (16x2 with I2C)

### Filename: `lesson-33-i2c-before-after.png`
**Place in lesson:** Before the I2C wiring steps in Step 2, "The I2C Shortcut"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A dramatic before-and-after comparison of LCD wiring. Left panel labeled "WITHOUT I2C Backpack": a cartoon Arduino is connected to an LCD display by a chaotic tangle of 12 colored wires going in every direction, with a stressed cartoon kid trying to manage all the connections. The wires are labeled "12 wires! Messy!" Right panel labeled "WITH I2C Backpack": the same Arduino connects to the same LCD display through a tiny blue board on the back of the LCD (the I2C backpack), using only 4 clean, neat wires labeled "SDA" (blue), "SCL" (yellow), "VCC" (red/orange), and "GND" (green). A happy, relaxed cartoon kid gives a thumbs up. A large arrow between the panels shows the transformation with a label reading "I2C Backpack = Shortcut!" Use color coding: red/orange for VCC wire, green for GND wire, blue for SDA data wire, yellow for SCL clock wire. Labels only, no paragraphs.

### Filename: `lesson-33-lcd-cursor-positions.png`
**Place in lesson:** Before the cursor positioning code in Step 4, "Position Your Text"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A large 16x2 LCD display showing "Hello World!" on the top row and "Counter: 42" on the bottom row in blocky LCD-style font. The display has a grid overlay showing all 32 character positions. The top-left corner is labeled "(0,0)" in red/orange, the top-right corner is labeled "(15,0)," the bottom-left corner is labeled "(0,1)," and the bottom-right corner is labeled "(15,1)" in blue. Column numbers 0 through 15 run along the top edge, and row numbers 0 and 1 are shown on the left edge. A cursor blink icon sits at position (11,1) in yellow. A cartoon magnifying glass zooms in on one character cell showing how "lcd.setCursor(column, row)" maps to a position. A cheerful cartoon robot types on a tiny keyboard connected to the LCD. Use color coding: red/orange for the (0,0) start position, blue for the column/row labels, yellow for the cursor position and text highlight, green for the LCD backlight glow. Labels only, no paragraphs.

### Filename: `lesson-33-lcd-wiring.png`
**Place in lesson:** Before the wiring steps in Step 3, "Wire the LCD"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A clean wiring diagram showing an Arduino Uno connected to a 16x2 LCD display with an I2C backpack using only four wires. The I2C backpack is shown as a small blue circuit board soldered to the back of the LCD. Four wires are clearly labeled and color-coded: GND (green wire) from LCD to Arduino GND, VCC (red/orange wire) from LCD to Arduino 5V, SDA (blue wire) from LCD to Arduino pin A4, and SCL (yellow wire) from LCD to Arduino pin A5. The LCD screen shows "Ready!" in blocky characters with a green backlight glow. Each Arduino pin (GND, 5V, A4, A5) is highlighted on the board. A cheerful cartoon kid holds up the LCD displaying "Only 4 wires!" Use color coding: red/orange for VCC/power wire, green for GND wire, blue for SDA data wire, yellow for SCL clock wire. Labels only, no paragraphs.

---

## Lesson 34: Project -- Digital Piano

### Filename: `lesson-34-piano-layout.png`
**Place in lesson:** Before Phase 2 wiring in "Plan the Piano Layout"
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A horizontal row of eight push buttons styled as piano keys, each labeled with its musical note name and frequency. From left to right: C4 (262 Hz) in red, D4 (294 Hz) in orange, E4 (330 Hz) in yellow, F4 (349 Hz) in green, G4 (392 Hz) in teal, A4 (440 Hz) in blue, B4 (494 Hz) in indigo, C5 (523 Hz) in violet. Above each button, a small LED in a matching color glows. Below each button, the Arduino pin number is shown. Above the entire row, a musical staff shows the eight notes ascending. At the bottom, a cartoon piezo buzzer emits yellow sound waves, and a small LCD display shows "Note: A4 440Hz." A cheerful cartoon kid plays the buttons like a piano with both hands, musical notes floating in the air above. Use color coding: rainbow gradient across the eight keys, yellow for sound waves, blue for data connections, red/orange for power indicators. Labels only, no paragraphs.

### Filename: `lesson-34-system-diagram.png`
**Place in lesson:** Before Phase 2, as an overview of all connections
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6-12. Friendly cartoon style, no dark or scary elements. A complete system wiring overview for the digital piano project, arranged as a colorful block diagram. In the center, an Arduino Uno board is drawn large with all used pins labeled. On the left side, eight push buttons are arranged vertically, each connected to a digital pin (Pins 2-9) via blue input wires, labeled "8 Piano Buttons (C4-C5)." On the top right, eight LEDs in rainbow colors are connected to digital pins via yellow output wires, labeled "8 Note LEDs." On the bottom right, a piezo buzzer connects to Pin 11 via a blue wire with yellow sound waves coming out, labeled "Buzzer (tone output)." Below the buzzer, a 16x2 LCD display connects via four I2C wires (SDA, SCL, VCC, GND) labeled "LCD Display (note name)." Power and ground rails run along the bottom in red/orange and green. A cheerful cartoon orchestra conductor stands on top of the Arduino waving a baton. Use color coding: red/orange for power rails, green for ground rails, blue for input wires and data connections, yellow for output wires and LED glows. Labels only, no paragraphs.
