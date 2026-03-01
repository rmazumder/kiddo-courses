# Lesson 3: Moving Averages

**Module:** 3 -- Market Trends
**Difficulty:** Star-3 Intermediate-Advanced
**Session Time:** 40--50 minutes
**Age:** 10--14 years
**XP Available:** 180 XP

---

## Your Mission Today

Welcome back, Trend Spotter! You have one final tool to learn in this module, and it is a BIG one: the **moving average**. This tool takes all the messy, zigzaggy price data and smooths it into a clean, easy-to-read line. It is like putting on noise-cancelling headphones for your charts -- all the static goes away, and you can hear the real signal!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a moving average is and why it is useful
- Calculate a simple moving average (SMA) by hand
- Plot a moving average on a chart
- Use moving averages to confirm trends

---

## What You Need

| Item | Qty |
|------|-----|
| Graph paper | 2 sheets |
| Pencil and eraser | 1 |
| Ruler | 1 |
| Calculator | 1 |
| Colored pencils (green, red, orange) | 3 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Noise Problem (5 min)

Say:
> "Look at this price data for a week:"

```
  Mon: $43,000    Tue: $45,000    Wed: $42,000
  Thu: $46,000    Fri: $44,000    Sat: $47,000    Sun: $43,500
```

> "Is the price going up or down? It is hard to tell, right? It keeps jumping around! This jumping around is called **noise**. It makes it hard to see the real trend."

> "What if I told you there is a way to SMOOTH OUT all that noise so you can see the real direction? That is what a moving average does!"

**The classroom grade analogy:**

> "Think about your grades in school. If you got 90, 70, 85, 95, 60 on five tests, those individual scores jump around a lot. But your AVERAGE is (90+70+85+95+60)/5 = 80. The average smooths out the ups and downs and gives you a clearer picture of how you are doing overall. A moving average does the same thing with prices!"

**Award: +10 XP for understanding the noise problem!**

---

### Step 2: What Is a Moving Average? (10 min)

Say:
> "A **moving average** is the average price over a certain number of days. But here is the cool part: it MOVES! Every day, you drop the oldest day and add the newest day. The average slides forward through time."

**Example: 3-Day Moving Average**

```
  Price Data:
  Day 1: $40,000
  Day 2: $42,000
  Day 3: $41,000
  Day 4: $43,000
  Day 5: $44,000
  Day 6: $42,000
  Day 7: $45,000

  3-Day Moving Average:
  Day 3: ($40,000 + $42,000 + $41,000) / 3 = $41,000
  Day 4: ($42,000 + $41,000 + $43,000) / 3 = $42,000
  Day 5: ($41,000 + $43,000 + $44,000) / 3 = $42,667
  Day 6: ($43,000 + $44,000 + $42,000) / 3 = $43,000
  Day 7: ($44,000 + $42,000 + $45,000) / 3 = $43,667
```

> "See how the moving average line is SMOOTHER than the actual price? It does not jump around as much. That is the whole point -- it filters out the noise!"

**Key vocabulary:**

| Word | Kid-Friendly Definition |
|------|------------------------|
| **Moving Average (MA)** | The average price over a set number of days, recalculated each day |
| **SMA** | Simple Moving Average -- the basic type where each day counts equally |
| **Period** | How many days you average together (e.g., 7-day, 20-day, 50-day) |
| **Smooth** | Less jumpy -- easier to see the real direction |

**Common periods traders use:**

| Period | What It Shows |
|--------|--------------|
| **7-day MA** | Short-term trend (about 1 week) |
| **20-day MA** | Medium-term trend (about 1 month) |
| **50-day MA** | Longer-term trend (about 2 months) |
| **200-day MA** | Very long-term trend (about 10 months) |

> "A shorter period (like 7 days) reacts faster but is still a bit jumpy. A longer period (like 50 days) is very smooth but reacts slowly to changes. Traders often use MULTIPLE moving averages together!"

**Award: +25 XP for understanding moving averages!**

---

### Step 3: Activity -- Calculate and Plot a Moving Average (15 min)

Say:
> "Time to do some math and create your own moving average! We will use a 3-day moving average to keep the math simple."

**The data (10 days):**

| Day | Price | 3-Day MA (You Calculate!) |
|-----|-------|--------------------------|
| Day 1 | $42,000 | -- |
| Day 2 | $43,000 | -- |
| Day 3 | $41,000 | ? |
| Day 4 | $44,000 | ? |
| Day 5 | $43,000 | ? |
| Day 6 | $46,000 | ? |
| Day 7 | $45,000 | ? |
| Day 8 | $47,000 | ? |
| Day 9 | $46,000 | ? |
| Day 10 | $48,000 | ? |

**Instructions:**

1. **Calculate each 3-Day MA:**
   - Day 3: ($42,000 + $43,000 + $41,000) / 3 = $42,000
   - Day 4: ($43,000 + $41,000 + $44,000) / 3 = $42,667
   - Day 5: ($41,000 + $44,000 + $43,000) / 3 = $42,667
   - Day 6: ($44,000 + $43,000 + $46,000) / 3 = $44,333
   - Day 7: ($43,000 + $46,000 + $45,000) / 3 = $44,667
   - Day 8: ($46,000 + $45,000 + $47,000) / 3 = $46,000
   - Day 9: ($45,000 + $47,000 + $46,000) / 3 = $46,000
   - Day 10: ($47,000 + $46,000 + $48,000) / 3 = $47,000

2. **Draw the chart:**
   - Y-axis: $40,000 to $50,000
   - X-axis: Day 1 to Day 10
   - Plot the actual prices in BLUE and connect them
   - Plot the moving average in ORANGE and connect them

3. **Compare the two lines:**
   - Which line is smoother? (The orange MA line)
   - Which line reacts faster to price changes? (The blue price line)
   - Both lines are going UP overall -- what does that tell you? (The trend is bullish!)

**Award: +45 XP for calculating and plotting your moving average!**

---

### Step 4: Using Moving Averages to Spot Trends (8 min)

Say:
> "Here is how traders use moving averages in real life."

**Rule 1: Price vs. Moving Average**

```
  Price ABOVE the MA = BULLISH (uptrend)

  Price ($)
    |     Price line
    |    /\  /\  /
    |   /  \/  \/
    |  /
    | /  Moving Average line (smoother)
    |/ ___---___---___---___
    +-------------------------> Time

  Price BELOW the MA = BEARISH (downtrend)

  Price ($)
    |\ ---___---___---___
    | \  Moving Average line
    |  \
    |   \  /\  /\
    |    \/  \/  \
    |              Price line
    +-------------------------> Time
```

> "If the price is above the moving average, the trend is UP. If the price is below the moving average, the trend is DOWN. Simple!"

**Rule 2: The Golden Cross and Death Cross**

> "When traders use TWO moving averages (like a 50-day and a 200-day), they watch for something dramatic:"

| Signal | What Happens | What It Means |
|--------|-------------|---------------|
| **Golden Cross** | Short MA crosses ABOVE long MA | Bullish signal -- the trend might be turning UP |
| **Death Cross** | Short MA crosses BELOW long MA | Bearish signal -- the trend might be turning DOWN |

```
  Golden Cross:

  Price ($)
    |        Short MA crosses ABOVE Long MA
    |           /
    |     ___--X--___     <- Long MA (200-day)
    |  __/     |     \__
    | /   ___--+         <- Short MA (50-day) crosses up
    |/ __/
    +-------------------------> Time
         "Golden Cross = Bullish!"
```

> "These crossovers are not magic -- they do not predict the future perfectly. But they are useful SIGNALS that help you understand what is happening."

**Award: +25 XP for learning trend signals with MAs!**

---

### Step 5: Putting It All Together (5 min)

Say:
> "Let's review all the trend tools you now have in your toolkit!"

```
  Your Trend Analysis Toolkit:

  Tool 1: Bull/Bear Markets
  "Is the overall market UP (bull) or DOWN (bear)?"

  Tool 2: Trend Lines
  "Can I draw a line connecting the lows (uptrend) or highs (downtrend)?"

  Tool 3: Moving Averages
  "Is the price above or below the moving average?"

  When ALL THREE agree, the signal is STRONG!

  Example: "Bull market" + "uptrend line holding" + "price above MA"
  = STRONG UPTREND!
```

> "When all your tools agree, you can be more confident about the trend. When they disagree, that is a warning to be cautious and wait for more clarity."

**Award: +15 XP for understanding how to combine all three tools!**

---

### Step 6: Quick Quiz (5 min)

**Question 1:** "What does a moving average do to price data?"
(It smooths out the noise and shows the overall direction more clearly)
**+10 XP for a correct answer!**

**Question 2:** "The price is consistently above the 50-day moving average. Is this bullish or bearish?"
(Bullish -- when the price is above the moving average, the trend is UP)
**+10 XP for a correct answer!**

**Question 3:** "What is a Golden Cross?"
(When a shorter moving average crosses above a longer moving average -- it is a bullish signal)
**+10 XP for a correct answer!**

**Bonus question:**
> "You are looking at a chart where the price is in a bull market, the uptrend line is holding, AND the price is above the 50-day moving average. How confident would you be that the trend is up?"
(Very confident! When all three tools agree, the signal is strong. But you should still be aware that trends can change at any time)
**+30 XP bonus!**

---

## Lesson 3 Complete!

```
  =============================================

     AVERAGE ACE BADGE UNLOCKED!

     Skills unlocked:
     [check] Know what a moving average is
     [check] Calculated a moving average by hand
     [check] Can plot a moving average on a chart
     [check] Understand Golden Cross and Death Cross

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| The noise problem | 10 |
| Understanding moving averages | 25 |
| Calculate and plot MA activity | 45 |
| Trend signals with MAs | 25 |
| Putting it all together | 15 |
| Quiz (3 questions) | 30 |
| Bonus question | 30 |
| **TOTAL POSSIBLE** | **180** |

---

## Coming Up Next...

In **Module 4**, you will learn the MOST important topic of the entire course: **smart investing**! You will discover how to manage RISK (so you never lose more than you can afford), learn about **dollar cost averaging** (a strategy so simple it is almost unfair), and figure out when to buy and when to sell. This is where everything comes together!

---

## Navigation

| | |
|:---|---:|
| [Lesson 2: Trend Lines](lesson_02_trend_lines.md) | [Module 4: Smart Investing](../module_04_smart_investing/README.md) |
