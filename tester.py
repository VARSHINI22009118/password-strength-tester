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
