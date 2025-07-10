# 🔐 Password Strength Tester

## Aim

A simple **Python command-line app** that tests the strength of user passwords using OWASP-style rules and a list of known weak passwords.

This project is designed to promote good cybersecurity practices by helping users choose strong, secure passwords.

## 📄 Requirements:

Python 3.6+
Text file with weak passwords (weak_passwords.txt)

## 📌 Features

✅ Enforces basic password policy:
- Minimum 12 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

✅ Checks if password is in a list of common/weak passwords

✅ Provides clear, user-friendly CLI feedback

✅ Simple and lightweight — runs in any terminal


## 💻 How It Works

1️⃣ User runs the script in a terminal.  
2️⃣ Enters a password when prompted.  
3️⃣ The program:
   - Checks the password against common weak passwords (loaded from `weak_passwords.txt`).
   - Verifies all security rules are satisfied.
4️⃣ The program outputs:
   - ✅ *"Your password is strong!"* if all tests pass.
   - ⚠️ *Detailed issues* if the password is weak.

## Program :
```
import re

# Load weak password list from file
def load_weak_passwords(filename="weak_passwords.txt"):
    with open(filename, 'r') as file:
        weak_passwords = {line.strip() for line in file}
    return weak_passwords

# Check rules
def check_rules(password):
    errors = []

    if len(password) < 12:
        errors.append("Too short: must be at least 12 characters.")

    if not re.search(r'[A-Z]', password):
        errors.append("Must include at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        errors.append("Must include at least one lowercase letter.")

    if not re.search(r'\d', password):
        errors.append("Must include at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Must include at least one special character.")

    return errors

# Main password strength tester
def test_password(password, weak_passwords):
    feedback = []

    # Check against weak password list (case-insensitive)
    if password.lower() in weak_passwords:
        feedback.append("This password is too common and easily guessable.")

    # Check rules
    rule_errors = check_rules(password)
    feedback.extend(rule_errors)

    if not feedback:
        return "✅ Your password is strong!"
    else:
        return "⚠️ Weak password:\n" + "\n".join(f"- {error}" for error in feedback)

# Main CLI
def main():
    print("=== Password Strength Tester ===")
    weak_passwords = load_weak_passwords()

    password = input("Enter your password: ")

    result = test_password(password, weak_passwords)
    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()

```

## Output :

![image](https://github.com/user-attachments/assets/cdd89911-0831-4176-8994-b350c054f351)


## 🗂️ Project Structure

```
password_tester/
├── tester.py
└── weak_passwords.txt

```


- `tester.py` – The main Python script.
- `weak_passwords.txt` – A list of known weak passwords.



## 🛠️ How to Use

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/password-strength-tester.git
cd password-strength-tester
```

2️⃣ (Optional) Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Linux / macOS
venv\Scripts\activate     # On Windows
```

3️⃣ Install Requirements

(No external libraries are strictly required, but you can use colorama for colored output.)
```
pip install colorama
```
4️⃣ Run the App

```
python tester.py

```


✨ Example Usage

=== Password Strength Tester ===
Enter your password: Welcome123!

Result:
⚠️ Weak password:
- Too short: must be at least 12 characters.

=== Password Strength Tester ===
Enter your password: Str0ng!Passw0rd2024

Result:
✅ Your password is strong!


## Result 
The strength of the password you entered has been evaluated successfully, ensuring it meets all defined security criteria and providing you with clear feedback to help you adopt safer, stronger passwords in line with recommended cybersecurity practices.
