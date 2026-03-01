# Module 6 — Robotics Projects: Image Generation Prompts

This file contains image generation prompts for all lessons in Module 6.
Generate each image and save it to the `images/` folder, then the images
will be embedded into each lesson file.

Total images: 22

---

## Lesson 43: Robot Basics — Chassis, Motors, Power

### Filename: `lesson-43-robot-chassis-assembly.png`

**Place in lesson:** Before the chassis assembly step, where the student first sees the robot parts laid out.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a 2-wheel robot chassis kit exploded into labeled parts: two DC motors labeled "LEFT MOTOR" and "RIGHT MOTOR" in red/orange, a plastic chassis plate labeled "SKELETON", two wheels labeled "WHEELS", and a small caster wheel labeled "BALANCE WHEEL". Use a cartoon kid character kneeling next to the parts with wide excited eyes, like assembling a LEGO set. Color coding: red/orange for power-carrying motors, gray for mechanical parts, green for the caster. Labels only, no paragraph text. Cheerful, discovery-oriented mood.

### Filename: `lesson-43-differential-drive-steering.png`

**Place in lesson:** Before the differential drive steering explanation, showing how robots turn.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a top-down view of a small cartoon robot using the tank/differential drive analogy: LEFT side shows a fast-spinning wheel labeled "FAST" and right side shows a slow wheel labeled "SLOW", with a curved arrow showing the robot turning right. Use three panels side by side: FORWARD (both wheels same speed, blue arrows), TURN RIGHT (left faster in orange, right slower in gray), SPIN IN PLACE (left forward orange, right backward red). Cheerful robot face in the center looking curious. Labels only, no paragraph text.

### Filename: `lesson-43-l298n-motor-wiring.png`

**Place in lesson:** Before the L298N wiring diagram, showing how motors connect to the driver.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show the L298N motor driver as a cartoon "traffic control booth" with two labeled output channels: OUT1/OUT2 in blue going to the LEFT motor, OUT3/OUT4 in yellow going to the RIGHT motor. The motor power supply (battery pack) connects in red/orange at "VCC MOTOR" and the Arduino connects in blue at "IN1/IN2/IN3/IN4". Label every pin and wire directly on the image. Use the analogy of a traffic cop directing two lanes of car traffic. Cheerful cartoon Arduino character holding a remote. Labels only, no paragraph text.

---

## Lesson 44: Robot Movement Functions

### Filename: `lesson-44-movement-functions-code.png`

**Place in lesson:** Before the section introducing Arduino movement functions, to show the concept of reusable commands.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show four large cartoon command buttons like a video game controller, each labeled with a robot function: a green FORWARD() button with an up arrow, a red BACKWARD() button with a down arrow, a blue TURN_LEFT() button with a left arrow, and a yellow TURN_RIGHT() button with a right arrow. A cartoon kid's hand is pressing the FORWARD() button. Use the analogy of a TV remote control — pressing one button = giving the robot one clear instruction. Each button has a small icon of a robot reacting to it. Labels only, no paragraph text.

### Filename: `lesson-44-square-path-program.png`

**Place in lesson:** Before the section where students program the robot to drive a square, to visualize the path.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a bird's-eye view of a floor with a dotted blue square path. A tiny cartoon robot follows the path with arrows at each corner showing: "forward(1000ms)", "turnRight(500ms)", repeating 4 times. Number each corner 1–4 with orange circles. The path forms a perfect square. A cartoon kid with a clipboard stands to the side cheering. Use a light grid background to suggest measured movement. Labels only, no paragraph text.

---

## Lesson 45: Line-Following Robot

### Filename: `lesson-45-ir-sensor-how-it-works.png`

**Place in lesson:** Before the IR sensor explanation, showing how the sensor detects white vs black surfaces.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show two side-by-side panels: LEFT panel shows an IR sensor above a WHITE surface — the sensor fires an IR beam (drawn as a dotted red arrow), the white surface bounces it back (blue return arrow), and the sensor outputs HIGH labeled in green. RIGHT panel shows the same sensor above a BLACK surface — the beam fires but is absorbed (no return arrow, shown as X), output reads LOW in red. Use the analogy of a flashlight in a mirror room vs a flashlight aimed at black velvet. Label: "WHITE = reflect = HIGH" and "BLACK = absorb = LOW". Cheerful cartoon sensor with eyes. Labels only, no paragraph text.

### Filename: `lesson-45-line-following-algorithm.png`

**Place in lesson:** Before the line-following if-else logic section, to show how the two sensors guide the robot.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a top-down robot view from below, with two IR sensors labeled "LEFT SENSOR" and "RIGHT SENSOR" underneath. Draw a black line track. Use three scenario panels: BOTH ON LINE = go straight (both sensors blue), LEFT DRIFTS OFF = turn left (left sensor red, right sensor blue), RIGHT DRIFTS OFF = turn right (right sensor red, left sensor blue). Use the analogy of an ant following a scent trail — include a tiny cartoon ant following the same line next to the robot for fun. Labels only, no paragraph text.

---

## Lesson 46: Obstacle-Avoiding Robot

### Filename: `lesson-46-ultrasonic-bat-analogy.png`

**Place in lesson:** Before the HC-SR04 explanation, to introduce the echolocation analogy.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a side-by-side comparison: LEFT side has a cartoon bat emitting sound waves (yellow arcs) that bounce off a tree and return to the bat's ears. RIGHT side shows an HC-SR04 sensor on a robot: the TRIG pin fires a blue ultrasonic pulse, it hits a box (labeled "OBSTACLE"), and the echo returns in orange to the ECHO pin. Label: "TRIG = shout" and "ECHO = listen" and "distance = (time × speed of sound) ÷ 2". Both characters look cheerful and curious. Labels only, no paragraph text.

### Filename: `lesson-46-obstacle-scan-decision.png`

**Place in lesson:** Before the obstacle avoidance decision tree, to show the robot's three-step decision process.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a top-down robot with a servo-mounted HC-SR04 sensor on its nose. Draw a three-panel flowchart inside thought bubbles above the robot: Step 1: "Obstacle detected!" (red exclamation, robot stops), Step 2: "Scan left... scan right..." (servo arrow sweeping, distance values shown), Step 3: "Choose the clearest path!" (green check on the wider side). Use the analogy of a person stopping at an intersection and looking both ways before crossing. Labels only, no paragraph text.

---

## Lesson 47: Buzzer and LEDs — Robot Personality

### Filename: `lesson-47-robot-personality-states.png`

**Place in lesson:** Before the section connecting LED states to robot behavior, to show what each light means.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a cute cartoon robot face with four emotion states side by side: FORWARD (green LED eyes glowing, happy smile, labeled "GO!"), REVERSE (red LED eyes, cautious look, labeled "BACKING UP!"), OBSTACLE DETECTED (yellow/amber LED flashing, surprised look, labeled "WAIT!"), STARTUP (rainbow shimmer on LEDs, excited face, labeled "HELLO!"). Use the analogy of traffic lights — same colors, same meaning. Each state has a colored glow around the robot. Labels only, no paragraph text.

### Filename: `lesson-47-tone-melody-buzzer.png`

**Place in lesson:** Before the tone() melody programming section, to show musical notes as robot sound.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a cartoon robot with a passive buzzer on its chest, emitting musical notes in colorful waves. Draw a simple piano keyboard analogy: each key labeled with a note name (C4, D4, E4, G4, A4) and its corresponding tone() frequency value (262, 294, 330, 392, 440). A small cartoon conductor wave wand directs the notes. An Arduino labeled "tone(pin, frequency, duration)" is shown sending the signal in blue. Labels only, no paragraph text. Cheerful, musical, energetic mood.

---

## Lesson 48: Remote-Controlled Robot (Bluetooth)

### Filename: `lesson-48-bluetooth-walkie-talkie.png`

**Place in lesson:** Before the HC-05 Bluetooth module explanation, to introduce wireless communication analogy.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a side-by-side analogy: LEFT side has two kids talking with walkie-talkies, with blue radio wave arcs between them. RIGHT side shows a smartphone with a Bluetooth app sending the same blue wave arcs to an HC-05 module mounted on a robot. Label the smartphone side: "YOUR PHONE = Remote", the HC-05 side: "HC-05 = Robot Ear", and the Arduino side: "ARDUINO = Robot Brain". Both setups look identical in concept. A cheerful cartoon robot receives a command and drives forward. Labels only, no paragraph text.

### Filename: `lesson-48-hc05-wiring-diagram.png`

**Place in lesson:** Before the HC-05 wiring step, showing safe voltage divider connection.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show the HC-05 module as a labeled cartoon character with four pins: VCC (red, 5V from Arduino), GND (green, ground), TXD (orange, goes to Arduino RX), RXD (yellow, receives signal through a voltage divider — two resistors labeled "1kΩ" and "2kΩ" shown clearly). Draw a small warning shield icon on the RXD line labeled "3.3V MAX — use resistors!". Use a cartoon "translator" character between the Arduino and HC-05 to represent the voltage divider converting 5V to 3.3V. Labels only, no paragraph text. Cheerful mood.

---

## Lesson 49: Robot Arm Introduction (Servo-Based)

### Filename: `lesson-49-dof-human-arm.png`

**Place in lesson:** Before the degrees of freedom explanation, to show DOF using a human arm analogy.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a cartoon human arm next to a robot arm, both side by side. The human arm has three labeled joints: SHOULDER (rotates up/down, blue arc), ELBOW (bends forward/back, orange arc), WRIST (rotates, yellow arc). The robot arm has three matching labeled servo motors in the same positions with the same color arcs. An annotation reads "Each joint = 1 DOF" with a small counter: "3 servos = 3 DOF". Include a cartoon child making the same arm motion as the robot. Labels only, no paragraph text. Cheerful, curious mood.

### Filename: `lesson-49-potentiometer-servo-control.png`

**Place in lesson:** Before the potentiometer control section, showing how a knob controls servo angle.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a large cartoon potentiometer knob labeled "CONTROL KNOB" on the left, connected by a blue signal wire to an Arduino (labeled "map() function"), which then sends an orange PWM signal wire to a servo motor on the right. As the knob turns (0°, 90°, 180° shown in three small panels), the servo arm matches the same angle. Use the analogy of a car steering wheel: turning the wheel = turning the servo. Label each step of the signal chain. Labels only, no paragraph text. Cheerful, interactive mood.

### Filename: `lesson-49-robot-arm-pickup-sequence.png`

**Place in lesson:** Before the preset positions programming section, showing the arm's pick-and-place sequence.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a four-panel storyboard of a popsicle-stick robot arm: Panel 1 "HOME" — arm upright, gripper open; Panel 2 "REACH" — arm extends forward toward a small eraser on a table; Panel 3 "GRAB" — gripper closes around the eraser; Panel 4 "PLACE" — arm lifts and moves to a new spot, drops eraser. Number each panel 1–4 in orange circles. The robot arm looks happy with cartoon eyes. A cartoon kid cheers in the background. Labels only, no paragraph text. Exciting, triumphant mood.

---

## Lesson 50: Final Capstone Project — Your Robot Challenge

### Filename: `lesson-50-four-capstone-choices.png`

**Place in lesson:** Before the four capstone project options, to give students a visual overview of their choices.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show four equal-sized panels, each representing one capstone project: Panel 1 — FIREFIGHTING ROBOT (tiny robot with fan, detecting flame sensor, red/orange glow); Panel 2 — MAZE RUNNER (robot with ultrasonic sensor navigating a cardboard maze top-down view, blue path lines); Panel 3 — ROBOT BUTLER (robot holding a tray approaching a person, yellow glowing LEDs for eyes, smiling); Panel 4 — ART ROBOT (robot with a marker attached, drawing colorful spirals on paper). Each panel has the project name in bold at the top. Fun, colorful, equal energy for each option. Labels only, no paragraph text.

### Filename: `lesson-50-design-build-test-cycle.png`

**Place in lesson:** Before the project planning section, to show the engineering design process.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a circular design loop with five colorful stations connected by arrows: 1 "PLAN IT" (pencil and notepad, blue), 2 "BUILD IT" (screwdriver and components, orange), 3 "CODE IT" (laptop with Arduino IDE, green), 4 "TEST IT" (robot moving, checkmarks, yellow), 5 "FIX IT" (wrench and thinking emoji, red) — then back to PLAN. A cartoon kid robot engineer stands in the center looking proud. Label each station clearly. Use a spinning gear or cycle arrow in the center. Labels only, no paragraph text. Inspiring, confident mood.

### Filename: `lesson-50-course-completion-celebration.png`

**Place in lesson:** At the very end of the lesson, as the final celebratory image before the badge block.

**Image generation prompt:**
Bright, colorful flat-design illustration for kids ages 6–12. Friendly cartoon style, no dark or scary elements. Show a joyful graduation scene: a cartoon child in a tiny graduation cap holding their completed robot up in the air, surrounded by confetti, stars, and XP coins raining down. The robot has glowing LED eyes and a big smile. In the background, a banner reads "ROBOT MASTER!" in bold colorful letters. Six golden shields/badges float around them, one for each module (labeled M1 through M6). The sky is bright and celebratory. No dark elements, pure triumph and joy. Labels only, no paragraph text.
