🔐 Password Generator
A command-line tool to generate strong, secure passwords built with Python.

Developed as part of the Synent Technologies Python Development Internship


✨ Features

🔢 Choose password length (4 to 128 characters)
🔡 Select character types:

Uppercase letters (A-Z)
Lowercase letters (a-z)
Numbers (0-9)
Special characters (!@#$...)


🔁 Generate multiple passwords at once
💪 Password strength checker (Weak / Medium / Strong / Very Strong)
✅ Guarantees at least one character from each selected type


🚀 How to Run
Make sure Python is installed, then run:
bashpython password_generator.py

No external libraries required — uses only Python's built-in random and string modules.


🖥️ Sample Output
==================================================
       SECURE PASSWORD GENERATOR
   Synent Technologies - Python Internship
==================================================

Enter password length (default 12): 12

Select character types to include:
  Uppercase letters (A-Z)? (y/n): y
  Lowercase letters (a-z)? (y/n): y
  Numbers (0-9)?       (y/n): y
  Special characters?  (y/n): y

How many passwords? (default 1): 2

--------------------------------------------------
  Generated Password(s):
--------------------------------------------------
  [1] aB3$xZ9!mK2@
      Strength: Very Strong
  [2] Qw8#nL5^vR1!
      Strength: Very Strong
--------------------------------------------------

💡 Strength Scoring System
ScoreRating0 - 3🔴 Weak4🟡 Medium5🟢 Strong6 - 7🔵 Very Strong
Points are awarded for:

Length >= 8
Length >= 12
Length >= 16
Contains uppercase letters
Contains lowercase letters
Contains digits
Contains special characters


📁 Project Structure
password-generator/
├── password_generator.py
└── README.md

🛠️ Requirements

Python 3.x
No external libraries needed


👤 Author
Ruman Tanveer
Synent Technologies — Python Development Internship

#internship #python #programming #technology