# Lesson 35: Temperature Sensor (DHT11) -- Quick Reference

**Age:** 6--12 years | **Time:** 50--60 min | **XP:** 240

---

## What is DHT11?

**DHT11 = A digital doctor's thermometer that sends signals**

- Measures **temperature** and **humidity**
- Has 3 pins: VCC, DATA, GND
- Sends data in a special digital pattern
- Arduino reads the pattern and gets the values

---

## How It Works

![DHT11 Module Pinout](../images/lesson-35-dht11-module-pinout.png)

**The DHT11:**
- Reads temperature and humidity
- Encodes as a digital signal
- Sends signal via ONE pin (data pin)
- Simple: only needs 3 connections!

---

## The Flow

![Thermometer to Arduino Flow](../images/lesson-35-thermometer-to-arduino-flow.png)

```
DHT11 sensor reads temperature
        ↓
Encodes as digital signal
        ↓
Sends via DATA pin
        ↓
Arduino receives and decodes
        ↓
Arduino displays on LCD or takes action
```

---

## Quick Wiring

| DHT11 Pin | Arduino Pin |
|-----------|------------|
| VCC | 5V |
| DATA | Digital 2 |
| GND | GND |

---

## Reading the Sensor

```cpp
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  Serial.print("Temp: ");
  Serial.println(temperature);
  delay(2000);
}
```

---

## Temperature Alert System

![Temperature Alert System](../images/lesson-35-temperature-alert-system.png)

**LEDs show temperature zones:**
- 🟢 **Green LED:** Cool (< 20°C)
- 🟡 **Yellow LED:** Comfortable (20-28°C)
- 🔴 **Red LED:** Hot! (> 28°C) -- buzzer alerts

---

## Real-World Uses

- 🌡️ **Smart thermostats** -- adjust heating/cooling
- 🏠 **Home monitoring** -- track room conditions
- 🌾 **Greenhouse** -- maintain plant environment
- 🏥 **Medical devices** -- monitor patient temperature
- 🎛️ **Weather stations** -- local weather data

---

## Quick Quiz

**Q1:** What does DHT11 measure?
**A:** Temperature and humidity.

**Q2:** How many pins does DHT11 have?
**A:** 3 pins: VCC, DATA, GND.

**Q3:** Why is this better than an analog temperature sensor?
**A:** Digital signal is cleaner and doesn't need calibration.

---

## Challenge

**Make a temperature logger:** Record temperatures every minute for one hour and print the highest and lowest values!

---

*Print this with the DHT11 pinout diagram for reference!*
