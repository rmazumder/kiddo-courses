# Lesson 37: Ultrasonic Distance Sensor -- Your Arduino's Echolocation (HC-SR04)

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

Circuit Explorer, your Arduino can now feel temperature and see light. Today you are giving it a completely different superpower -- **echolocation**, just like a bat! Using a sensor called the HC-SR04, your Arduino will send out invisible sound waves, listen for the echo, and calculate exactly how far away an object is. By the end of this lesson, you will build a real parking sensor that beeps faster as something gets closer!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how ultrasonic distance sensing works (send a ping, listen for the echo)
- Wire the HC-SR04 sensor to Arduino
- Write a sketch that measures distance in centimeters
- Build a parking sensor with a buzzer that beeps faster as objects approach
- Use your Magic Measurement Wand to measure trigger and echo pin voltages

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| HC-SR04 ultrasonic sensor | 1 |
| Active buzzer | 1 |
| LEDs (green, yellow, red) | 1 each |
| 330-ohm resistors | 3 |
| Breadboard | 1 |
| Jumper wires | 10 |
| Multimeter (your Magic Measurement Wand!) | 1 |
| A ruler or tape measure (for testing accuracy) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Bat Superpower (5 min)

> "Did you know that bats fly in complete darkness without bumping into things? They are not using night vision -- they use SOUND. A bat screams (at a pitch too high for humans to hear), and then listens for the echo bouncing off walls, bugs, and trees. From the echo's delay, the bat's brain calculates exactly how far away everything is. This is called echolocation."

Show them the HC-SR04:

> "This sensor does EXACTLY the same thing! See those two silver cylinders on the front? One is a tiny SPEAKER that sends out ultrasonic sound (too high-pitched for your ears). The other is a MICROPHONE that listens for the echo. Arduino does the math to figure out the distance. It is a robot bat eye!"

**Fun fact:**
> "The HC-SR04 sends sound at about 40,000 Hz (40 kHz). Humans can only hear up to about 20,000 Hz. So this sensor is screaming constantly and you cannot hear a thing!"

**Award: +10 XP for learning about echolocation!**

---

### Step 2: How It Works -- The Science (8 min)

**The Swimming Pool Analogy:**

> "Imagine you are standing at one end of a swimming pool and you clap your hands. The sound bounces off the far wall and comes back as an echo. If the pool is short, the echo comes back FAST. If the pool is long, the echo takes LONGER. If you know how fast sound travels, you can calculate the distance from the time!"

**The process in 4 steps:**

1. Arduino sends a tiny electrical pulse to the TRIGGER pin (like pressing a "shout" button)
2. The sensor blasts out 8 ultrasonic pulses (the "shout")
3. The pulses bounce off the nearest object and come back
4. The sensor sends a pulse back through the ECHO pin -- the length of this pulse tells Arduino how long the sound took to travel there and back

**The math:**

```
Speed of sound = 0.034 cm per microsecond (at room temperature)

Round-trip time = microseconds the echo took
Distance = (round-trip time x 0.034) / 2

We divide by 2 because the sound travels TO the object and BACK.
```

**HC-SR04 specs:**
- Range: 2 cm to 400 cm (about 1 inch to 13 feet)
- Accuracy: roughly +/- 3 mm
- Needs 5V power

**Award: +10 XP for understanding the science!**

---

### Step 3: Wiring the HC-SR04 (5 min)

**HC-SR04 Pinout:**

```
  HC-SR04 (front view -- two "eyes")

  +------+------+------+------+
  | VCC  | Trig | Echo | GND  |
  +------+------+------+------+
    |       |      |      |
    5V    Pin 9  Pin 10   GND
```

**Wiring:**

```
  HC-SR04       Arduino
  ---------     --------
  VCC    -----> 5V
  Trig   -----> Pin 9
  Echo   -----> Pin 10
  GND    -----> GND
```

> "Just 4 wires! This sensor is easy to connect. VCC and GND for power, Trig to send the shout, Echo to hear the reply."

**Award: +15 XP for wiring the sensor!**

---

### Step 4: Your First Distance Reading (10 min)

**The Code:**

```cpp
int trigPin = 9;
int echoPin = 10;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  Serial.println("Ultrasonic Sensor Ready!");
}

void loop() {
  // Send the trigger pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Listen for the echo
  long duration = pulseIn(echoPin, HIGH);

  // Calculate distance
  int distance = duration * 0.034 / 2;

  // Print the result
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(100);
}
```

**What each part does:**

- `digitalWrite(trigPin, HIGH)` for 10 microseconds -- sends the "shout" signal
- `pulseIn(echoPin, HIGH)` -- measures how many microseconds the echo pin stays HIGH (this is the round-trip time)
- `duration * 0.034 / 2` -- converts time to distance in centimeters

**Test it:**
1. Upload and open Serial Monitor
2. Hold your hand in front of the sensor -- move it closer and farther
3. Use a ruler to check: put an object exactly 10 cm away. Does Arduino agree?
4. Try 20 cm, 50 cm, and 100 cm

> "If it is off by a centimeter or two, that is normal! The sensor is accurate to about 3 millimeters, which is pretty good for a $2 component."

**Award: +20 XP for your first distance reading!**

---

### Step 5: Build the Parking Sensor (10 min)

Now let us make it useful -- a parking sensor with LEDs and a buzzer!

```cpp
int trigPin = 9;
int echoPin = 10;
int buzzerPin = 8;
int greenLED = 5;
int yellowLED = 6;
int redLED = 7;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  Serial.begin(9600);
}

int getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void loop() {
  int dist = getDistance();

  // Turn off all LEDs first
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, LOW);

  if (dist > 50) {
    // Far away -- all clear, green
    digitalWrite(greenLED, HIGH);
    noTone(buzzerPin);

  } else if (dist > 20) {
    // Getting closer -- caution, yellow
    digitalWrite(yellowLED, HIGH);
    tone(buzzerPin, 1000, 100);
    delay(300);

  } else if (dist > 5) {
    // Very close -- warning, red!
    digitalWrite(redLED, HIGH);
    tone(buzzerPin, 2000, 100);
    delay(100);

  } else {
    // Way too close -- STOP! Rapid beeping
    digitalWrite(redLED, HIGH);
    tone(buzzerPin, 3000, 50);
    delay(50);
  }

  Serial.print("Distance: ");
  Serial.print(dist);
  Serial.println(" cm");
}
```

**Try it out:**
- Walk toward the sensor slowly
- Green light when far, yellow getting closer, red when close, rapid beeping when too close!
- Move your hand toward it like it is a car backing into a parking spot

> "You just built the same kind of system that real cars use to help drivers park! Except those cost hundreds of dollars and yours cost about $3 in parts."

**Award: +40 XP for building the parking sensor!**

---

### Step 6: Wand Check -- Measure Trigger and Echo Voltages (5 min)

> "Time for your Wand to investigate what is really happening on those pins!"

**Wand Test 1 -- Trigger Pin:**

1. Set your Wand to DC Volts
2. Touch black probe to GND, red probe to the Trigger pin (pin 9)
3. While the sketch is running, the trigger pin sends very short HIGH pulses. Your Wand might show 0V or a tiny voltage (the pulses are only 10 microseconds long -- too fast for the Wand to catch!)

**Wand Test 2 -- Echo Pin:**

1. Keep Wand on DC Volts
2. Touch red probe to the Echo pin (pin 10)
3. Place your hand close to the sensor (10 cm) -- the Echo pin stays HIGH longer, so you might see a slightly higher average voltage
4. Move your hand far away -- shorter HIGH time, lower average reading

```
| Measurement | Hand Close (10cm) | Hand Far (50cm+) |
|-------------|------------------|-----------------|
| Echo pin average voltage | ~0.5-2V | ~0.1-0.5V |
| Your reading |  |  |
```

> "The Wand is averaging those super-fast pulses. When an object is close, the echo stays HIGH longer, so the average is higher. You are seeing the distance encoded as voltage!"

**Award: +30 XP for investigating pin voltages with your Wand!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** The HC-SR04 measures distance using:
- A) Laser beams
- B) Ultrasonic sound waves (too high-pitched to hear)
- C) Magnets

**(Correct: B -- +15 XP!)**

**Question 2:** Why do we divide the duration by 2 in the distance formula?
- A) Because the sensor has 2 cylinders
- B) Because the sound travels to the object AND back, so we only want one-way distance
- C) Because Arduino counts twice as fast

**(Correct: B -- +15 XP!)**

**Question 3:** What is the approximate range of the HC-SR04?
- A) 0 to 10 cm
- B) 2 to 400 cm
- C) 1 to 10 meters

**(Correct: B -- +15 XP!)**

**Question 4:** In our parking sensor, what happens when the distance is less than 5 cm?
- A) The green LED turns on
- B) Nothing happens
- C) The red LED flashes and the buzzer beeps rapidly

**(Correct: C -- +15 XP!)**

---

## Lesson 37 Complete!

```
  =============================================

     ECHO MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire and read an HC-SR04 ultrasonic sensor
     [check] Calculate distance from echo time
     [check] Built a parking sensor with LEDs and buzzer
     [check] Measured trigger/echo voltages with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- bat echolocation | 10 |
| Understanding the science | 10 |
| Wiring the sensor | 15 |
| First distance reading | 20 |
| Parking sensor build | 40 |
| Wand Check (trigger + echo) | 30 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **185** |

---

## Coming Up Next...

In **Lesson 38**, you will learn to control **servo motors** -- small motors that move to a precise angle. You will combine the ultrasonic sensor with a servo to build a scanning radar system that sweeps back and forth, measuring distances like a real sonar! Your Wand will measure the servo signal voltage!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Distance reads 0 cm all the time | Check Trig and Echo wiring -- make sure they are not swapped |
| Distance reads random huge numbers | Object might be too close (under 2 cm) or at a steep angle |
| Buzzer stays on constantly | Check your if-else logic -- are the distance thresholds correct? |
| Serial Monitor shows no output | Make sure baud rate is 9600 in Serial Monitor |
| Readings jump around | Ultrasonic waves can bounce oddly off soft or angled surfaces -- try a flat, hard surface |
| Sensor does not detect small objects | The object must be at least a few cm wide -- thin wires will not reflect sound well |
