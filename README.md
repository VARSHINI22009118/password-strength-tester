# 🔐 Password Strength Tester

A simple **Python command-line app** that tests the strength of user passwords using OWASP-style rules and a list of known weak passwords.

This project is designed to promote good cybersecurity practices by helping users choose strong, secure passwords.

---

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

---

## 💻 How It Works

1️⃣ User runs the script in a terminal.  
2️⃣ Enters a password when prompted.  
3️⃣ The program:
   - Checks the password against common weak passwords (loaded from `weak_passwords.txt`).
   - Verifies all security rules are satisfied.
4️⃣ The program outputs:
   - ✅ *"Your password is strong!"* if all tests pass.
   - ⚠️ *Detailed issues* if the password is weak.

---

## 🗂️ Project Structure

```
password_tester/
├── tester.py
└── weak_passwords.txt

```


- `tester.py` – The main Python script.
- `weak_passwords.txt` – A list of known weak passwords.

---

## 🛠️ How to Use

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-tester.git
cd password-strength-tester

2️⃣ (Optional) Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Linux / macOS
venv\Scripts\activate     # On Windows
3️⃣ Install Requirements
(No external libraries are strictly required, but you can use colorama for colored output.)

bash
Copy
Edit
pip install colorama
4️⃣ Run the App
bash
Copy
Edit
python tester.py
✨ Example Usage
yaml
Copy
Edit
=== Password Strength Tester ===
Enter your password: Welcome123!

Result:
⚠️ Weak password:
- Too short: must be at least 12 characters.
vbnet
Copy
Edit
=== Password Strength Tester ===
Enter your password: Str0ng!Passw0rd2024

Result:
✅ Your password is strong!
📄 Requirements
Python 3.6+

Text file with weak passwords (weak_passwords.txt)