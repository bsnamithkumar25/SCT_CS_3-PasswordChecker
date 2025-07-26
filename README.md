# Password Strength Checker – Python CLI Tool

**SkillCraft Cybersecurity Internship – Task 3**  
**Author:** B S Namith Kumar  
**Domain:** Cybersecurity

---

## Project Overview

This is a Python-based password strength assessment tool developed as part of Task 3 of my internship at SkillCraft Technology. It evaluates password strength based on industry-standard criteria and provides constructive suggestions for stronger password creation.

---

## Features

- Evaluates password strength using five core criteria:
  - Minimum length of 8 characters
  - At least one lowercase letter
  - At least one uppercase letter
  - At least one digit (0–9)
  - At least one special character (e.g., @, #, $, %)
- Strength scoring from **Extremely Weak** to **Very Strong**
- Tailored improvement suggestions
- CLI-based interface built using `argparse`
- Modular and reusable Python code

---

## Learning Outcomes

- Used regular expressions for input validation
- Applied cybersecurity principles to practical scripting
- Improved modular coding practices
- Understood real-world password policy implementations
- Followed best practices for password complexity enforcement

---

## Sample Run

### Example – Strong Password

```bash
$ python main.py
Enter your password: Welcome@123
Password Strength: Very Strong
Suggestions to improve your password:
(None – all criteria met)
Example – Weak Password
bash
Copy
Edit
$ python main.py
Enter your password: hello
Password Strength: Very Weak
Suggestions to improve your password:
- Include at least one uppercase letter.
- Include at least one digit (0–9).
- Include at least one special character (e.g., @, #, $, etc.).
- Password is too short (minimum 8 characters).
Notes
No external libraries required (uses built-in re and argparse)

Password input is visible (optional to use getpass for hidden input)

Strength levels:

5: Very Strong

4: Strong

3: Moderate

2: Weak

1: Very Weak

0: Extremely Weak

Supports English character set

Easily integrable into GUI apps or other Python projects

How to Run
Install Python 3

Save the script as main.py

Run using:

bash
Copy
Edit
python main.py
```
