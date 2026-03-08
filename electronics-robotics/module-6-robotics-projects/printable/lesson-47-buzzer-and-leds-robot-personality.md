# Lesson 47: Buzzer and LEDs — Robot Personality -- Quick Reference

**Age:** 6--12 years | **Time:** 55--65 min | **XP:** 260

---

## Robot Personality States

![Robot Personality States](../images/lesson-47-robot-personality-states.png)

**LEDs show the robot's mood — like traffic lights:**

| State | LED Color | Meaning | Real-World |
|-------|-----------|---------|-----------|
| Forward | 🟢 GREEN | Go! Happy! | Traffic light GO |
| Backward | 🔴 RED | Backing up, careful | Traffic light STOP |
| Obstacle | 🟡 YELLOW | Wait, scanning | Traffic light CAUTION |
| Startup | 🌈 RAINBOW | Initializing, excited | System startup |

---

## Express Robot Personality with Code

```cpp
void goForward() {
  digitalWrite(LEDgreen, HIGH);
  digitalWrite(LEDred, LOW);
  digitalWrite(LEDyellow, LOW);
  forward(500);
}

void goBackward() {
  digitalWrite(LEDgreen, LOW);
  digitalWrite(LEDred, HIGH);
  digitalWrite(LEDyellow, LOW);
  backward(300);
}

void obstacleDetected() {
  digitalWrite(LEDyellow, HIGH);
  // Blink to show scanning
  for (int i = 0; i < 3; i++) {
    delay(200);
    digitalWrite(LEDyellow, LOW);
    delay(200);
    digitalWrite(LEDyellow, HIGH);
  }
}
```

---

## Add Robot Sounds with Buzzer

![Tone Melody Buzzer](../images/lesson-47-tone-melody-buzzer.png)

**The tone() function plays musical notes:**

```cpp
// Play a note: tone(pin, frequency, duration)
tone(buzzerPin, 262, 500);  // C4 for 0.5 sec
delay(500);
tone(buzzerPin, 294, 500);  // D4
delay(500);
tone(buzzerPin, 330, 500);  // E4
delay(500);
tone(buzzerPin, 392, 500);  // G4
```

**Common frequencies (Hz):**

| Note | Frequency |
|------|-----------|
| C4 | 262 Hz |
| D4 | 294 Hz |
| E4 | 330 Hz |
| G4 | 392 Hz |
| A4 | 440 Hz |

---

## LED + Buzzer Combinations

| Action | LED | Buzzer |
|--------|-----|--------|
| Startup | Rainbow pulse | Ascending beeps (262→392 Hz) |
| Start moving | Green steady | Single beep |
| Obstacle! | Yellow flash | Alert chirp (600 Hz) |
| Success | Green + Yellow pulse | Victory fanfare |

---

## Real-World Uses

- 🚗 **Cars** - Backup beepers, turn signal blinks
- 🚨 **Alarms** - Red flash + loud buzzer for attention
- 🎮 **Video games** - Feedback when hitting obstacles
- 🤖 **Robots** - Communicate mood and status to humans

---

## Quick Quiz

**Q1:** What color LED means "Go forward"?
**A:** GREEN — like a traffic light.

**Q2:** How do you play a musical note on the buzzer?
**A:** Use `tone(buzzerPin, frequency, duration)`

**Q3:** What frequency is the note A4?
**A:** 440 Hz.

---

## Challenge

**Personality upgrade:** Add startup beeps and LEDs that cycle through all colors during the first 2 seconds when the robot powers on!

---

*Print this with the personality states and tone frequency table for reference!*
