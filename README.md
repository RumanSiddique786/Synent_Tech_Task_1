# 🔐 Password Generator

A command-line tool to generate strong and secure passwords using Python.

Developed as part of the **Synent Technologies Python Development Internship**.

---

## ✨ Features

- 🔢 Choose password length *(4 to 128 characters)*
- 🔡 Select character types:
  - Uppercase letters `(A-Z)`
  - Lowercase letters `(a-z)`
  - Numbers `(0-9)`
  - Special characters `(!@#$%^&*)`
- 🔁 Generate multiple passwords at once
- 💪 Password strength checker:
  - Weak
  - Medium
  - Strong
  - Very Strong
- ✅ Ensures at least one character from each selected type

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python password_generator.py
```

No external libraries are required.

Uses only Python's built-in:

- `random`
- `string`

modules.

---

## 🖥️ Sample Output

```text
SECURE PASSWORD GENERATOR
Synent Technologies - Python Internship

Enter password length (default 12): 12

Select character types to include:
Uppercase letters (A-Z)? (y/n): y
Lowercase letters (a-z)? (y/n): y
Numbers (0-9)? (y/n): y
Special characters? (y/n): y

How many passwords? (default 1): 2

Generated Password(s):

[1] aB3$xZ9!mK2@
Strength: Very Strong

[2] Qw8#nL5^vR1!
Strength: Very Strong
```

---

## 💡 Strength Scoring System

| Score | Rating |
|------|---------|
| 0 - 3 | 🔴 Weak |
| 4 | 🟡 Medium |
| 5 | 🟢 Strong |
| 6 - 7 | 🔵 Very Strong |

### Points are awarded for:

- Length >= 8
- Length >= 12
- Length >= 16
- Contains uppercase letters
- Contains lowercase letters
- Contains digits
- Contains special characters

---

## 📁 Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed

---

## 👤 Author

**Ruman Tanveer**  
Synent Technologies — Python Development Internship

---

## 📌 Tags

`#python` `#password-generator` `#internship` `#security` `#programming`
