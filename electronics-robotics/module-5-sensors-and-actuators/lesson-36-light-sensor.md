# Lesson 36: Light Sensor -- The Eye of Your Arduino (LDR)

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 275 XP

---

## Your Mission Today

Circuit Explorer, your Arduino just learned to feel temperature. But it is still in the dark -- literally! Today you are giving it the power of **sight** (well, sort of). You will connect a **Light Dependent Resistor (LDR)** that can tell the difference between bright sunlight and total darkness. By the end, you will build an automatic night light that turns on by itself when the room gets dark. How cool is that?

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what an LDR is and how it works
- Build a voltage divider circuit with an LDR
- Read light levels with Arduino's analog input
- Use the `map()` function to scale sensor values
- Build an automatic night light
- Use your Magic Measurement Wand to measure LDR resistance in different light conditions

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| LDR (Light Dependent Resistor / photoresistor) | 1 |
| 10k-ohm resistor | 1 |
| LEDs (any color) | 2 |
| 330-ohm resistors | 2 |
| Breadboard | 1 |
| Jumper wires | 8 |
| Multimeter (your Magic Measurement Wand!) | 1 |
| Something to block light (your hand, a box, a book) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Automatic Streetlight Mystery (5 min)

Start with a question:

> "Have you ever noticed how streetlights turn on automatically when it gets dark, and turn off when the sun comes up? Nobody is flipping a switch! How do they KNOW when it is dark?"

Let them guess. Then reveal:

> "They use a tiny component called a Light Dependent Resistor -- or LDR for short. It is basically a little eyeball for electronics. When light shines on it, its resistance goes DOWN. When it is dark, its resistance goes WAY UP. That is literally how streetlights, automatic porch lights, and even some nightlights work!"

Show them the LDR -- it looks like a small disk with a squiggly line pattern on top and two legs.

> "See that squiggly pattern? That is a special material that reacts to light. Photons (tiny particles of light) hit it and knock electrons loose, making electricity flow easier. More light = less resistance = more current!"

**Award: +10 XP for learning about LDRs!**

---

### Step 2: How an LDR Works (5 min)

**The Sunglasses Analogy:**

> "Imagine you are wearing magic sunglasses. In bright sunlight, the lenses become clear (low resistance -- light passes through easily). In the dark, the lenses become totally black (high resistance -- nothing gets through). An LDR does the same thing, but with electricity instead of your eyes!"

**Key vocabulary:**

- **LDR (Light Dependent Resistor):** A resistor whose resistance changes based on light. Also called a photoresistor or photocell.
- **Bright light:** Resistance drops to about 100--500 ohms
- **Total darkness:** Resistance climbs to 500,000 ohms or more (500k ohms!)
- **Voltage divider:** A pair of resistors that splits voltage into a smaller output voltage. We use this to convert the LDR's changing resistance into a changing voltage that Arduino can read.

```
  Light Level vs LDR Resistance:

  Bright sun ........ ~100-500 ohms     (very low)
  Room lights ....... ~1,000-5,000 ohms (medium)
  Dim room .......... ~10,000-50,000 ohms (high)
  Total darkness .... ~200,000-500,000+ ohms (very high!)
```

**Award: +10 XP for understanding the LDR!**

---

### Step 3: Wiring the LDR with a Voltage Divider (8 min)

The LDR does not give Arduino a direct signal like the DHT11. Instead, we put it in a **voltage divider** so Arduino can read a voltage that changes with the light level.

**Circuit diagram:**

```
  Arduino 5V ----+
                 |
               [LDR]  (resistance changes with light)
                 |
                 +-------> Arduino A0 (analog input)
                 |
             [10k-ohm]  (fixed resistor)
                 |
  Arduino GND ---+
```

**How it works:**

> "The LDR and the 10k-ohm resistor share the 5V between them. When it is bright, the LDR has low resistance, so it takes a small share of the voltage -- meaning the voltage at A0 is HIGH (close to 5V). When it is dark, the LDR has high resistance, so it hogs most of the voltage -- meaning the voltage at A0 drops LOW (close to 0V)."

**Quick summary:**
- Bright = high analog reading (close to 1023)
- Dark = low analog reading (close to 0)

**Award: +20 XP for wiring the voltage divider!**

---

### Step 4: Reading Light Levels (8 min)

**Basic Light Reading Code:**

```cpp
int ldrPin = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("Light Sensor Ready!");
}

void loop() {
  int lightValue = analogRead(ldrPin);

  Serial.print("Light Level: ");
  Serial.print(lightValue);

  if (lightValue > 800) {
    Serial.println("  -- Bright!");
  } else if (lightValue > 400) {
    Serial.println("  -- Normal room light");
  } else if (lightValue > 100) {
    Serial.println("  -- Dim");
  } else {
    Serial.println("  -- Dark!");
  }

  delay(500);
}
```

**Upload and experiment:**
1. Upload the sketch and open Serial Monitor
2. Watch the numbers in normal room light
3. Cover the LDR with your hand -- numbers drop!
4. Shine a flashlight (or phone light) on it -- numbers jump up!
5. Try covering it completely with a box -- how low does it go?

> "You just gave your Arduino eyes! It can now tell the difference between bright, normal, dim, and dark."

**Award: +20 XP for reading light levels!**

---

### Step 5: Build the Automatic Night Light (8 min)

Now add an LED that turns on when it gets dark:

```cpp
int ldrPin = A0;
int ledPin = 9;     // Use a PWM pin for smooth dimming
int threshold = 300; // Below this = dark enough to turn on LED

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lightValue = analogRead(ldrPin);

  // Map light value to LED brightness (inverted!)
  // Dark (low reading) = bright LED, Bright (high reading) = LED off
  int ledBrightness = map(lightValue, 0, 1023, 255, 0);

  // Only turn on LED when it is dim enough
  if (lightValue < threshold) {
    analogWrite(ledPin, ledBrightness);
  } else {
    analogWrite(ledPin, 0);
  }

  Serial.print("Light: ");
  Serial.print(lightValue);
  Serial.print("  LED: ");
  Serial.println(ledBrightness);

  delay(100);
}
```

**What `map()` does:**

> "The `map()` function is like a translator. The LDR gives us numbers from 0 to 1023, but `analogWrite()` needs numbers from 0 to 255. Plus, we want to FLIP the relationship -- dark room means BRIGHT LED. `map()` handles all of that in one line!"

**Test it:**
- Cover the LDR slowly with your hand -- watch the LED gradually brighten
- Remove your hand -- LED fades away
- Try it in a dim room vs a bright room

**Award: +30 XP for building the automatic night light!**

---

### Step 6: Wand Check -- Measure LDR Resistance Live! (8 min)

> "Here is where your Magic Measurement Wand gets really exciting. You are going to watch resistance change in REAL TIME as you change the light!"

**Wand Test -- LDR Resistance in Different Conditions:**

1. **Remove the LDR from the circuit** (very important -- never measure resistance in a powered circuit!)
2. Set your Wand to Resistance mode (ohms)
3. Touch one probe to each LDR leg

**Now test in different light conditions:**

```
| Condition | Expected Resistance | Your Wand Reads | Points |
|-----------|-------------------|----------------|--------|
| Bright light (flashlight on LDR) | 100-500 ohms | | +10 XP |
| Normal room light | 1k-10k ohms | | +10 XP |
| Covered with hand | 10k-100k ohms | | +10 XP |
| Totally dark (inside a box) | 100k-500k+ ohms | | +10 XP |
```

> "Watch the Wand's display as you slowly cover and uncover the LDR. See how the numbers climb when it gets darker? That is resistance increasing because fewer photons are hitting the sensor material. You are literally watching physics happen!"

**Bonus Wand trick:**

Try keeping one probe on the LDR while slowly moving a flashlight closer and farther away. The resistance changes smoothly -- not in sudden jumps!

**Award: +40 XP for measuring LDR resistance in 4 conditions!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** When bright light shines on an LDR, what happens to its resistance?
- A) Resistance goes UP (higher)
- B) Resistance goes DOWN (lower)
- C) Resistance stays the same

**(Correct: B -- +15 XP!)**

**Question 2:** Why do we need a 10k-ohm resistor paired with the LDR?
- A) To protect the LDR from breaking
- B) To form a voltage divider so Arduino can read a changing voltage
- C) To make the LED brighter

**(Correct: B -- +15 XP!)**

**Question 3:** What does the `map()` function do in our night light code?
- A) Shows a map of the room
- B) Rescales a number from one range to another range
- C) Maps the Arduino pins to the breadboard

**(Correct: B -- +15 XP!)**

**Question 4:** In total darkness, roughly what resistance would you expect from an LDR?
- A) About 100 ohms
- B) About 1,000 ohms
- C) About 200,000 ohms or more

**(Correct: C -- +15 XP!)**

---

## Lesson 36 Complete!

```
  =============================================

     LIGHT DETECTIVE BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire and read an LDR light sensor
     [check] Build a voltage divider
     [check] Use map() to rescale values
     [check] Build an automatic night light
     [check] Measured resistance changes with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- streetlight mystery | 10 |
| Understanding LDRs | 10 |
| Wiring the voltage divider | 20 |
| Reading light levels | 20 |
| Automatic night light | 30 |
| Wand Check (4 conditions) | 40 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **190** |

---

## Coming Up Next...

In **Lesson 37**, you will discover the **ultrasonic distance sensor** (HC-SR04) -- a component that measures distance using sound waves you cannot even hear! You will build a parking sensor that beeps faster as objects get closer, just like a real car. Your Wand will measure the trigger and echo pin voltages!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Analog reading stays at 0 or 1023 | Check voltage divider wiring -- LDR and 10k resistor must be in series between 5V and GND, with A0 connected to the middle |
| LED does not respond to light changes | Make sure LED is on a PWM pin (3, 5, 6, 9, 10, or 11) |
| Readings jump around wildly | Add a small delay (100ms) and average multiple readings |
| Wand reads "OL" on LDR in darkness | Switch to a higher resistance range -- LDR can be very high resistance in dark |
| Night light turns on/off randomly | Adjust the threshold value in code to match your room's light level |
| LDR seems to not react | Make sure the squiggly side faces the light source -- the back is less sensitive |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 35: Temperature Sensor -- Your Arduino's Thermometer (DHT11/DHT22)](lesson-35-temperature-sensor.md) | [Lesson 37: Ultrasonic Distance Sensor -- Your Arduino's Echolocation (HC-SR04) →](lesson-37-ultrasonic-distance-sensor.md) |
