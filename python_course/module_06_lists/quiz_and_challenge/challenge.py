"""
==============================================
  MODULE 6 CHALLENGE: Student Grade Manager!
  Earn 30 XP and your LIST NINJA badge!
==============================================

YOUR MISSION:
  Build a student grade management system!

  Your program should have these functions:

  1. add_student(students, name, score)
     - Adds a student as [name, score] to the students list.

  2. get_average(students)
     - Returns the average score of all students.

  3. get_highest(students)
     - Returns the name and score of the student with the highest score.

  4. get_failing(students, passing_score=60)
     - Returns a list of names of students who scored below passing_score.

  5. print_report(students)
     - Prints a formatted report card for all students.
     - Include: name, score, letter grade, and pass/fail status.

  6. sort_by_score(students)
     - Returns a new list sorted by score (highest first).

  After defining the functions, create at least 8 students
  and demonstrate all the functions!

  EXAMPLE OUTPUT:
  =======================================
         STUDENT GRADE REPORT
  =======================================
  Name          Score   Grade   Status
  ---------------------------------------
  Alice           95       A   PASS
  Bob             82       B   PASS
  Charlie         55       F   FAIL
  ...
  ---------------------------------------
  Class Average: 78.5
  Highest Score: Alice (95)
  Failing Students: Charlie, ...
  =======================================
"""

print("=" * 50)
print("   STUDENT GRADE MANAGER")
print("=" * 50)
print()

# --------------------------------------------------
# FUNCTION 1: add_student
# --------------------------------------------------
# def add_student(students, name, score):
#     students.append([name, score])

# --------------------------------------------------
# FUNCTION 2: get_average
# --------------------------------------------------
# def get_average(students):
#     total = 0
#     for student in students:
#         total += student[1]  # student[1] is the score
#     return total / len(students)

# --------------------------------------------------
# FUNCTION 3: get_highest
# --------------------------------------------------
# def get_highest(students):
#     best = students[0]
#     for student in students:
#         if student[1] > best[1]:
#             best = student
#     return best

# --------------------------------------------------
# FUNCTION 4: get_failing
# --------------------------------------------------
# def get_failing(students, passing_score=60):
#     failing = []
#     for student in students:
#         if student[1] < passing_score:
#             failing.append(student[0])
#     return failing

# --------------------------------------------------
# FUNCTION 5: print_report
# --------------------------------------------------
# def print_report(students):
#     print(f"{'Name':15s} {'Score':6s} {'Grade':6s} {'Status':6s}")
#     print("-" * 40)
#     for student in students:
#         name = student[0]
#         score = student[1]
#         # Determine grade
#         if score >= 90: grade = "A"
#         elif score >= 80: grade = "B"
#         elif score >= 70: grade = "C"
#         elif score >= 60: grade = "D"
#         else: grade = "F"
#         # Determine status
#         status = "PASS" if score >= 60 else "FAIL"
#         print(f"{name:15s} {score:6d} {grade:>6s} {status:>6s}")

# --------------------------------------------------
# FUNCTION 6: sort_by_score
# --------------------------------------------------
# def sort_by_score(students):
#     # Create a copy and sort it
#     sorted_list = sorted(students, key=lambda s: s[1], reverse=True)
#     return sorted_list

# --------------------------------------------------
# DEMO: Create students and use all functions!
# --------------------------------------------------

# students = []
# add_student(students, "Alice", 95)
# add_student(students, "Bob", 82)
# add_student(students, "Charlie", 55)
# add_student(students, "Diana", 91)
# add_student(students, "Eve", 78)
# add_student(students, "Frank", 67)
# add_student(students, "Grace", 44)
# add_student(students, "Henry", 88)

# sorted_students = sort_by_score(students)
# print_report(sorted_students)
# print()
# print(f"Class Average: {get_average(students):.1f}")
# best = get_highest(students)
# print(f"Highest Score: {best[0]} ({best[1]})")
# failing = get_failing(students)
# print(f"Failing Students: {', '.join(failing) if failing else 'None!'}")

print()
print("=" * 50)
print("Module 6 Complete!")
print("Badge Earned: [#] LIST NINJA")
print("Next: Module 7 - Build a Game! (Capstone Project)")
print("=" * 50)
