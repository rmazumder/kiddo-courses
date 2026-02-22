# Scratch Blocks Explained with Python

Every Scratch block below has a matching Python instruction right next to it.
Read each one carefully - you will start seeing patterns!

---

## 1. Starting the Program

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  when [green flag] clicked |  -->  if __name__ == "__main__":
+---------------------------+           main()

The green flag starts everything. In Python, this special line
does the same job - it runs your code when you press "Run".
```

---

## 2. Saying Something

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  say  [Hello!]            |  -->  print("Hello!")
+---------------------------+
|  for  [2]  secs           |  -->  time.sleep(2)
+---------------------------+

Scratch pops up a speech bubble. Python prints to the screen.
Both show your message to the world!
```

---

## 3. Moving a Sprite

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  move  [10]  steps        |  -->  x = x + 10
+---------------------------+           (or: x += 10)

In Scratch the sprite slides forward. In Python you change
a number variable to represent the new position.
```

---

## 4. Repeating Something

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  repeat  [10]             |  -->  for i in range(10):
|  +---------------------+  |          # your code here
|  |  (blocks go here)   |  |
|  +---------------------+  |
+---------------------------+

The C-shaped repeat block wraps around code to run it 10 times.
Python's for loop does exactly the same thing!
```

---

## 5. Checking a Condition

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  if  <touching color?>    |  -->  if touching_color:
|  +---------------------+  |          # run this code
|  |  (blocks go here)   |  |
|  +---------------------+  |
+---------------------------+

The diamond shape in Scratch is a True/False question.
Python's if statement works the same way.
```

---

## 6. Setting a Variable

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  set  [score]  to  [0]    |  -->  score = 0
+---------------------------+

Scratch orange blocks store values. Python uses the = sign
to store values in variables. Same idea!
```

---

## 7. Waiting (Pausing)

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  wait  [1]  secs          |  -->  import time
+---------------------------+       time.sleep(1)

Scratch pauses your script. Python's time.sleep() does the
same - it freezes the program for that many seconds.
```

---

## 8. Looping Forever

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  forever                  |  -->  while True:
|  +---------------------+  |          # your code here
|  |  (blocks go here)   |  |
|  +---------------------+  |
+---------------------------+

The forever block never stops. "while True:" in Python also
runs forever until you stop the program. Used for game loops!
```

---

## 9. Broadcasting a Message (Calling a Function)

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  broadcast  [jump!]       |  -->  jump()
+---------------------------+

+---------------------------+
|  when I receive  [jump!]  |  -->  def jump():
|  +---------------------+  |          # jumping code here
|  |  (blocks go here)   |  |
|  +---------------------+  |
+---------------------------+

Broadcast sends a message to other scripts. In Python, you
define a function with "def" and call it by name. Same idea!
```

---

## 10. Using a Variable

```
[SCRATCH BLOCK]                    [PYTHON CODE]
+---------------------------+
|  [my variable]  (orange)  |  -->  my_variable = 10
+---------------------------+       print(my_variable)
                                    my_variable = my_variable + 5

Scratch shows variables as orange rounded blocks. Python uses
names with an = sign. You can read and change them anytime!
```

---

## Quick Reference Card

Cut out (or copy) this table and keep it next to your screen!

```
Scratch Block              Python Code
--------------------------+--------------------------
when green flag clicked   | if __name__ == "__main__":
say "Hello!"              | print("Hello!")
wait 1 secs               | time.sleep(1)
move 10 steps             | x += 10
set score to 0            | score = 0
change score by 1         | score += 1
repeat 10                 | for i in range(10):
forever                   | while True:
if <condition>            | if condition:
if <condition> else       | if condition: ... else: ...
broadcast message         | my_function()
define my block           | def my_function():
```

You are already a programmer - you just learned the Python spelling!
