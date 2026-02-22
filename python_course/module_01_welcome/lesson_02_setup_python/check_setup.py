"""
==============================================
  MODULE 1 - LESSON 2: Check Your Setup
==============================================

Run this file to make sure Python is installed
correctly on your computer!

How to run:
  - In IDLE: Open this file, then press F5 (or Run > Run Module)
  - In Terminal: Type   python check_setup.py   (or python3 on Mac)
"""

import sys

print("=" * 50)
print("  PYTHON SETUP CHECK")
print("=" * 50)
print()

# Check Python version
version = sys.version
print(f"Python version: {version}")
print()

# Check if version is 3.x
major_version = sys.version_info.major
minor_version = sys.version_info.minor

if major_version >= 3 and minor_version >= 6:
    print("RESULT: Everything looks great!")
    print(f"You are running Python {major_version}.{minor_version}.")
    print("You are ready to start coding!")
    print()
    print("Try typing this in the Python shell:")
    print('  >>> print("I am a Python programmer!")')
elif major_version >= 3:
    print("RESULT: You have Python 3, which is good!")
    print("But your version is a bit old.")
    print("Consider updating at python.org for the best experience.")
else:
    print("WARNING: You are running Python 2!")
    print("This course needs Python 3.")
    print("Please download Python 3 from python.org")

print()
print("=" * 50)
