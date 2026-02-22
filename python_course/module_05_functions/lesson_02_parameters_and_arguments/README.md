# Module 5, Lesson 2: Parameters and Arguments

## Your Mission Today
Learn how to send information INTO your functions to make them flexible!

## Learning Objectives
By the end of this lesson, you will be able to:
- Add **parameters** to your functions
- Pass **arguments** when calling functions
- Use **default values** for parameters

---

## Parameters: Making Functions Flexible

Without parameters, a function always does the exact same thing.
With parameters, you can customize what it does each time!

```python
# Without parameters -- always greets the same way
def greet():
    print("Hello!")

# With a parameter -- greets anyone by name!
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")    # Prints: Hello, Alex!
greet("Jordan")  # Prints: Hello, Jordan!
```

### Vocabulary
- **Parameter**: The variable name in the function definition (like `name`)
- **Argument**: The actual value you pass when calling the function (like `"Alex"`)

Think of parameters as empty boxes inside the function. When you call the
function, you fill those boxes with arguments!

---

## Activity

Open `parameters.py` to see examples,
then complete `exercise_params.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 3 -- Return Values!

---

## Navigation

| | |
|:---|---:|
| [← Module 5, Lesson 1: What Are Functions?](../lesson_01_what_are_functions/README.md) | [Module 5, Lesson 3: Return Values →](../lesson_03_return_values/README.md) |
