# Module 5 -- Image Generation Prompts
**Module:** Sensors and Actuators (Lessons 35--42)
**Images folder:** `module-5-sensors-and-actuators/images/`
**Total images:** 22

---

## Table of Contents

| Lesson | Title | Images |
|--------|-------|--------|
| 35 | Temperature Sensor (DHT11) | 3 |
| 36 | Light Sensor (LDR) | 3 |
| 37 | Ultrasonic Distance Sensor (HC-SR04) | 3 |
| 38 | Servo Motors | 3 |
| 39 | DC Motors and L298N Driver | 3 |
| 40 | IR Sensor and Remote Control | 2 |
| 41 | PIR Motion Sensor | 2 |
| 42 | Smart Room Project | 3 |

---

## Lesson 35: Temperature Sensor (DHT11)

### Filename: `lesson-35-dht11-module-pinout.png`
**Place in lesson:** Before Step 2 (How the DHT11 Works), to introduce the physical sensor and its pins.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large, zoomed-in DHT11 sensor module (the small blue box with holes) in the center, drawn in a cheerful cartoon style. Three pins extend from the bottom, each labeled with a color-coded tag: VCC in red, DATA in blue, and GND in black. A smiling cartoon robot nurse character stands beside the sensor holding a giant digital thermometer, reinforcing the analogy that the DHT11 is like a digital doctor's thermometer that sends signals instead of showing numbers. Add small labels reading "Temperature" and "Humidity" with friendly icons (a sun and a water droplet) pointing to the sensor's holes. Background is a clean, light gradient.

### Filename: `lesson-35-thermometer-to-arduino-flow.png`
**Place in lesson:** Before the wiring diagram in Step 3 (Wiring the DHT11), to show the concept before the physical build.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a three-stage left-to-right flow diagram illustrating how the DHT11 works like a digital doctor's thermometer sending signals. Stage 1 (left): a cartoon thermometer with a warm room background, labeled "Sensor Reads Temperature." Stage 2 (center): the DHT11 module connected to an Arduino Uno with a blue data wire, labeled "Sends Digital Signal." Stage 3 (right): an Arduino connected to a green LCD screen showing "22 C / 55%" and a red LED glowing, labeled "Arduino Displays and Alerts." Use red/orange wires for power connections, blue wire for the data line, and green highlight on the LCD output. A cheerful cartoon kid watches the LCD with an excited expression.

### Filename: `lesson-35-temperature-alert-system.png`
**Place in lesson:** Before Step 5 (Challenge -- Temperature Alert System), to preview the alert build.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a cartoon temperature alert system on a breadboard. A DHT11 sensor on the left sends a blue signal line to an Arduino Uno in the center. On the right, three LEDs are arranged vertically like a traffic light: green LED at the bottom labeled "Cool (below 20 C)," yellow LED in the middle labeled "Comfortable (20--28 C)," and red LED at the top labeled "HOT! (above 28 C)" glowing brightly with small alarm lines radiating from it. The red LED has a yellow warning triangle icon beside it. A cheerful cartoon kid character fans themselves dramatically next to the red LED. All power wires are red/orange, signal wires are blue, and ground wires are black.

---

## Lesson 36: Light Sensor (LDR)

### Filename: `lesson-36-ldr-magic-sunglasses.png`
**Place in lesson:** Before Step 2 (How an LDR Works), to introduce the resistance-changes-with-light concept through the magic sunglasses analogy.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show the "magic sunglasses" analogy as a two-panel side-by-side comparison. Left panel: a bright sunny outdoor scene with a cheerful cartoon kid wearing clear/transparent sunglasses, and a large LDR component below labeled "Bright Light = Low Resistance (100 ohm)." The LDR appears open and clear with lots of tiny electron arrows flowing through it easily. Right panel: the same kid in a dark room wearing pitch-black opaque sunglasses, with the LDR below labeled "Darkness = High Resistance (500k ohm+)." The LDR appears dark and blocked with very few electron arrows struggling through. A color-coded resistance slide runs along the bottom connecting both panels, going from green (low resistance) through yellow to red (high resistance).

### Filename: `lesson-36-ldr-resistance-chart.png`
**Place in lesson:** Before the resistance measurement activity in Step 2, to provide a visual reference for expected LDR values.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large vertical "brightness-to-resistance slide" chart, like a colorful thermometer or slider. At the top: a bright cartoon sun icon with the label "Direct Sunlight = ~100 ohm" in green. In the middle: a ceiling lamp icon with the label "Indoor Room Light = ~10k ohm" in yellow. At the bottom: a moon-and-stars icon with the label "Darkness = 500k ohm+" in dark blue. Beside the slider, show three small cartoon LDR components at each level, with the squiggly line pattern on top clearly visible. A smiling cartoon robot character holds a multimeter (labeled "Magic Measurement Wand") with probes touching an LDR, and the display reads "10,000." Use green for low-resistance zones, yellow for mid-range, and blue/purple for high-resistance zones.

### Filename: `lesson-36-voltage-divider-with-ldr.png`
**Place in lesson:** Before Step 3 (Building the Voltage Divider Circuit), to explain how changing resistance produces a changing voltage the Arduino can read.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a clear, labeled voltage divider circuit with an LDR on top and a fixed 10k-ohm resistor on the bottom. The circuit connects between a red 5V rail (labeled "5V" in red/orange) and a black GND rail (labeled "GND" in black). The midpoint between the two components has a blue wire going to an Arduino analog pin, labeled "Vout to A0" in blue. Show two small side panels: one with a sun icon where the LDR is small/clear and the Vout arrow points high (labeled "Bright = Low R = High Vout"), and one with a moon icon where the LDR is large/dark and the Vout arrow points low (labeled "Dark = High R = Low Vout"). A cheerful cartoon kid gives a thumbs-up next to the circuit. Label the output voltage in green as the "signal Arduino reads."

---

## Lesson 37: Ultrasonic Distance Sensor (HC-SR04)

### Filename: `lesson-37-hc-sr04-two-eyes.png`
**Place in lesson:** Before Step 2 (How Ultrasonic Sensing Works), to introduce the sensor's two cylinders and their roles.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large, friendly HC-SR04 ultrasonic sensor drawn to look like a cartoon face with two big "eyes" (the two silver ultrasonic cylinders). The left eye is labeled "Transmitter -- Sends Sound Pulse" with small blue sound wave arcs radiating outward from it. The right eye is labeled "Receiver -- Catches the Echo" with sound wave arcs coming back toward it. Below the sensor face, four pins are clearly labeled: VCC (red), Trig (blue), Echo (blue), GND (black). Above the sensor, show the swimming pool echo analogy: a small cartoon figure clapping near a pool wall, with curved sound lines bouncing off the wall and returning, and a stopwatch labeled "Time = Distance!" A dotted arc shows the sound traveling out and bouncing back with a formula label "Distance = Time x Speed of Sound / 2."

### Filename: `lesson-37-pool-echo-distance.png`
**Place in lesson:** Before the distance calculation explanation in Step 2, to reinforce the echo timing concept with the pool analogy.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a cartoon swimming pool viewed from the side. A cheerful cartoon kid stands at one end and claps their hands, with blue sound wave arcs traveling across the pool toward the far wall. The sound waves bounce off the wall and return as dotted blue arcs. A large, friendly stopwatch character floats above the pool showing the time measurement. Three labeled distances are shown: "Close Wall = Fast Echo" (short pool, small time), "Medium Wall = Medium Echo" (medium pool), and "Far Wall = Slow Echo" (long pool, big time). Below the pool, show the matching HC-SR04 scenario: the sensor sending a pulse to an object at a measured distance with the label "Same idea -- sound bounces back, Arduino calculates distance!"

### Filename: `lesson-37-parking-sensor-build.png`
**Place in lesson:** Before Step 5 (Challenge -- Parking Sensor), to preview the parking sensor project with its distance-based LED feedback.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a cartoon parking sensor system. On the left, an HC-SR04 sensor faces a toy car approaching from the right. Between them, three zones are marked on the ground with colored bands: green zone (far, labeled "> 30 cm"), yellow zone (medium, labeled "15--30 cm"), and red zone (close, labeled "< 15 cm"). Above each zone, the matching LED is lit: a green LED for the far zone, a yellow LED for the medium zone, and a red LED for the close zone (shown glowing brightly with warning lines). A small buzzer icon next to the red zone shows "BEEP BEEP BEEP!" in a speech bubble. The Arduino sits in the center connecting to all components with color-coded wires (red for power, blue for signal, green for output LEDs). A cheerful cartoon kid drives the toy car toward the sensor.

---

## Lesson 38: Servo Motors

### Filename: `lesson-38-servo-position-clock-hand.png`
**Place in lesson:** Before Step 2 (How a Servo Works -- The Clock Hand Analogy), to show the 0-to-180-degree range using the clock hand metaphor.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large, colorful semicircular dial (like a speedometer or protractor) representing the servo's 180-degree range. A clock-hand style pointer extends from the center pivot. Three key positions are highlighted and labeled: "0 degrees = Far Left" (pointer at the left end, green dot), "90 degrees = Center" (pointer straight up, blue dot), and "180 degrees = Far Right" (pointer at the right end, green dot). Small intermediate tick marks show 30, 45, 60, 120, 135, and 150 degrees. At the bottom, a cartoon SG90 servo motor is drawn with its horn attached to the pointer. A cheerful cartoon robot character holds a TV remote and "commands" the servo to different angles with speech bubbles saying "Go to 90!" The servo's three wires are labeled: red/orange (VCC), brown/black (GND), and yellow/blue (Signal).

### Filename: `lesson-38-servo-internals.png`
**Place in lesson:** Before the explanation of how servos hold position in Step 2, to show the internal feedback mechanism.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a cartoon cross-section cutaway of an SG90 servo motor, as if the case has been sliced open to reveal the inside. Label four key internal parts with callout arrows: (1) "DC Motor" -- a small motor at the bottom drawn in orange, labeled "spins fast," (2) "Gear Train" -- a series of interlocking cartoon gears in different colors, labeled "slows down and adds strength," (3) "Position Sensor (Potentiometer)" -- a small dial at the output shaft, labeled "tells the brain where the arm is right now," (4) "Control Circuit (Brain)" -- a small green circuit board, labeled "compares command vs. actual position." A feedback loop arrow circles from the position sensor back to the control circuit with the label "Am I at the right angle yet?" The servo horn sits on top of the output shaft. A cheerful cartoon kid peers into the cutaway with a magnifying glass.

### Filename: `lesson-38-servo-sweep-demo.png`
**Place in lesson:** Before Step 3 (Wiring and First Sweep), to visualize what the sweep program will look like in action.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a time-lapse style illustration of a servo motor sweeping from 0 to 180 degrees and back. The servo is mounted on a breadboard connected to an Arduino Uno. Five ghost/shadow positions of the servo horn are shown in a fan pattern: 0 degrees (far left, light blue), 45 degrees (light green), 90 degrees (bright yellow, largest/most opaque), 135 degrees (light green), and 180 degrees (far right, light blue). Curved arrows indicate the back-and-forth sweeping motion. The Arduino displays a small code snippet label: "for angle 0 to 180." Three wires connect the servo to Arduino: red/orange wire to 5V, brown/black wire to GND, yellow wire to pin 9 (labeled in blue as "Signal"). A cheerful cartoon kid watches the sweeping servo with amazement stars around their head.

---

## Lesson 39: DC Motors and L298N Driver

### Filename: `lesson-39-garden-hose-vs-fire-hose.png`
**Place in lesson:** Before Step 1 (Hook -- Why Not Just Connect the Motor to Arduino?), to introduce the current limitation problem using the fire hose analogy.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a two-panel side-by-side comparison. Left panel labeled "Arduino Alone = Garden Hose": a cartoon Arduino Uno tries to push water through a tiny garden hose (labeled "40 mA max") toward a large DC motor. The motor barely moves, with a sad face and a tiny drip of water reaching it. The Arduino looks strained with sweat drops. Right panel labeled "L298N + Battery = Fire Hose": the Arduino whispers a small blue signal to an L298N motor driver module, which connects to a large battery pack (red/orange power lines). The L298N blasts a massive fire-hose stream of current (labeled "up to 2A!") at the DC motor, which spins happily with a big grin and motion lines. A cheerful cartoon kid stands between the panels pointing at the L298N saying "Use a helper!"

### Filename: `lesson-39-l298n-module-labeled.png`
**Place in lesson:** Before Step 2 (Meet the L298N Motor Driver), to provide a clear reference diagram of the module's connections.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large, clearly labeled top-down view of the L298N motor driver module. Label every important connection with color-coded callout arrows: Motor A output terminals (green, left side) labeled "To Motor A," Motor B output terminals (green, right side) labeled "To Motor B," 12V power input (red/orange) labeled "Battery Power IN (6--12V)," GND terminal (black) labeled "Ground (shared with Arduino)," 5V output (red, small) labeled "5V OUT (can power Arduino)," IN1 and IN2 pins (blue) labeled "Motor A Direction (from Arduino)," IN3 and IN4 pins (blue) labeled "Motor B Direction (from Arduino)," ENA pin (blue) labeled "Motor A Speed (PWM)," ENB pin (blue) labeled "Motor B Speed (PWM)." A small cartoon robot character stands next to the module holding a clipboard with a checklist. The module is drawn slightly larger than real life for clarity, with the heat sink visible on top.

### Filename: `lesson-39-motor-direction-truth-table.png`
**Place in lesson:** Before Step 3 (Controlling Motor Direction), to visually show how IN1/IN2 pin combinations control motor behavior.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a visual truth table for DC motor direction control through the L298N. Four rows are illustrated as cartoon panels: Row 1 -- IN1=HIGH, IN2=LOW: a cartoon motor spinning clockwise with a green arrow and label "Forward!" Row 2 -- IN1=LOW, IN2=HIGH: the motor spinning counterclockwise with an orange arrow and label "Backward!" Row 3 -- IN1=LOW, IN2=LOW: the motor stopped with a red stop sign and label "Stop (coast)." Row 4 -- IN1=HIGH, IN2=HIGH: the motor locked with a brake icon and label "Brake (locked)." Each row shows the L298N pins highlighted in blue for HIGH and gray for LOW. A cheerful cartoon kid at the bottom holds a joystick, and arrows connect joystick positions to the matching motor states. Use green for output/forward, orange for backward, and red for stop.

---

## Lesson 40: IR Sensor and Remote Control

### Filename: `lesson-40-invisible-flashlight-morse-code.png`
**Place in lesson:** Before Step 2 (How IR Communication Works), to show the invisible light beam concept and signal encoding.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show the "invisible flashlight Morse code" analogy. On the left, a cartoon hand holds a TV remote control with a visible IR LED at the front. The remote sends an invisible beam toward the right, shown as a dotted purple/magenta line labeled "Infrared Light (invisible to your eyes!)." A cartoon eye icon with an X through it sits above the beam with the label "You can't see this." A cartoon camera icon below the beam shows the light as visible, labeled "But a camera can!" On the right, an IR receiver module (three-pin component) catches the beam, connected to an Arduino. Between the remote and receiver, the beam is annotated with a pattern of short and long pulses (like Morse code dashes and dots) labeled "Each button sends a different blink pattern." A cheerful cartoon kid holds a phone camera up to the remote, seeing the purple glow on the phone screen.

### Filename: `lesson-40-ir-button-code-decoding.png`
**Place in lesson:** Before Step 4 (Decoding Button Codes), to show the full chain from button press to decoded hex number.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a three-stage left-to-right decoding flow. Stage 1 (left): a cartoon hand presses button "1" on an IR remote, with a callout showing the button highlighted in yellow. Stage 2 (center): the IR signal pattern is shown as a waveform with blue highs and lows, labeled "Signal Pattern" with timing marks. Below the waveform, dotted lines translate the pattern into binary bits. Stage 3 (right): an Arduino connected to a computer monitor displaying a Serial Monitor window. The Serial Monitor shows decoded output: "Button: 1, Code: 0xFFA25D" in green text on a black background. Arrows connect each stage with labels: "Button Press" to "IR Blink Pattern" to "Decoded Hex Number." A cheerful cartoon kid character wears detective glasses and holds a magnifying glass, with a speech bubble saying "Code cracked!" Use blue for signal lines and green for the decoded output.

---

## Lesson 41: PIR Motion Sensor

### Filename: `lesson-41-pir-detection-zones.png`
**Place in lesson:** Before Step 2 (How PIR Sensors Work), to show the Fresnel lens detection zone concept using the spy movie laser grid analogy.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a top-down view of a PIR sensor (HC-SR501 module with its white dome clearly drawn) at the bottom center. From the dome, a fan-shaped detection area spreads outward and upward, divided into multiple triangular zones by thin blue laser-like lines, resembling the spy movie laser grid analogy. The zones alternate in light blue and light purple tints. The detection fan spans approximately 120 degrees and is labeled "Detection Range: up to 7 meters." The white Fresnel lens dome is labeled "Fresnel Lens -- splits view into zones." The three pins on the back of the module are labeled: VCC (red), OUT (blue), GND (black). A smiling cartoon robot security guard character stands next to the sensor wearing a tiny hat and holding a flashlight. The background is a simple room corridor.

### Filename: `lesson-41-warm-body-detection-burst.png`
**Place in lesson:** Before Step 3 (Wiring and First Test), to show what happens when a warm body crosses the detection zones.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show the PIR sensor at the bottom with its fan-shaped detection grid (from the spy movie laser grid analogy). A cheerful cartoon kid walks from left to right across the detection zones, with their warm body shown radiating wavy red/orange infrared heat lines. As the kid crosses from one zone to the next, a bright yellow starburst labeled "DETECTED!" appears at the sensor. The sensor's OUT pin shows a blue signal line going HIGH (drawn as a rising step on a tiny graph). Connected to the Arduino, a green LED lights up and a buzzer shows "BEEP!" in a speech bubble. Two small side annotations explain: "Still body = no trigger (infrared stays the same)" with a standing-still figure and a calm sensor, and "Moving body = TRIGGER (infrared changes between zones)" with the walking figure and the alert burst. Use red/orange for heat, blue for the signal output, and green for the LED response.

---

## Lesson 42: Smart Room Project

### Filename: `lesson-42-smart-room-birds-eye.png`
**Place in lesson:** Before the Smart Room System Features section, to give kids an exciting preview of the entire project.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a bird's-eye (top-down) view of a cartoon bedroom. Four sensor systems are active and labeled in different corners: (1) Top-left corner -- a DHT11 sensor connected to an LCD screen showing "22 C / 55%" with a green checkmark, labeled "Climate Monitor." (2) Top-right corner -- an LDR near a window with a small LED night light glowing, labeled "Auto Night Light." (3) Bottom-left -- an HC-SR04 ultrasonic sensor near the bedroom door with a buzzer, labeled "Door Alert (distance < 20 cm = BEEP!)." (4) Bottom-right -- a PIR sensor near a doorway with a servo motor gate that swings open, labeled "Motion-Activated Gate." Each sensor zone is highlighted with a colored glow: red/orange for temperature, yellow for light, blue for distance, and green for motion output. An Arduino Uno sits in the center of the room like a command hub, with colored wires radiating out to each sensor. A cheerful cartoon kid stands at the door, triggering the HC-SR04 and PIR simultaneously.

### Filename: `lesson-42-smart-room-pin-map.png`
**Place in lesson:** Before the wiring section (Step 2: System Wiring), to provide a complete reference for connecting all four sensor systems to one Arduino.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a large, clear Arduino Uno board in the center with all its pins visible. Four groups of colored wires fan out to four sensor modules arranged around the Arduino: (1) DHT11 (top-left) with red VCC wire, blue data wire to digital pin 2, and black GND wire. (2) LDR + 10k resistor voltage divider (top-right) with red power, a yellow wire to analog pin A0, and black GND. (3) HC-SR04 (bottom-left) with red VCC, blue Trig wire to pin 7, blue Echo wire to pin 8, and black GND. (4) PIR sensor (bottom-right) with red VCC, blue OUT wire to pin 4, and black GND. Outputs are also shown: servo (green wire to pin 9), buzzer (green wire to pin 10), LEDs (green wires to pins 11-13), LCD via I2C (SDA to A4, SCL to A5). Each sensor group is boxed with a matching color border and labeled. A cheerful cartoon robot assistant holds a checklist of all connections at the bottom corner.

### Filename: `lesson-42-smart-room-system-flowchart.png`
**Place in lesson:** Before Step 3 (Writing the Code -- System Integration), to show how all sensor readings flow into decisions and outputs.
**Prompt:**
Bright, colorful flat-design illustration for kids ages 6--12. Friendly cartoon style, no dark or scary elements. Show a top-to-bottom flowchart of the Smart Room system logic. At the top, four sensor input boxes in a row: "DHT11: Read Temp" (red/orange box), "LDR: Read Light" (yellow box), "HC-SR04: Read Distance" (blue box), "PIR: Read Motion" (purple box). Arrows flow down from each to a decision diamond: "Temp > 28 C?" leads to "Red LED ON" (red), "Light < 300?" leads to "Night Light ON" (yellow/green), "Distance < 20 cm?" leads to "Buzzer BEEP!" (blue), "Motion = YES?" leads to "Servo Gate OPEN" (green). All four paths merge at the bottom into an LCD display box showing "Display all readings on LCD." A loop arrow returns from the bottom back to the top labeled "Repeat every 2 seconds." Each decision path uses the matching color coding. A cheerful cartoon kid at the bottom gives a thumbs-up next to the completed flowchart.
