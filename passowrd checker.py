import re

def check_password_strength(password):
    # Criteria
    length = len(password) >= 8
    uppercase = re.search(r'[A-Z]', password)
    lowercase = re.search(r'[a-z]', password)
    digit = re.search(r'\d', password)
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = sum([bool(length), bool(uppercase), bool(lowercase), bool(digit), bool(special)])

    # Result
    if score == 5:
        return "✅ Strong password!"
    elif 3 <= score < 5:
        return "⚠️  Moderate password. Consider improving it."
    else:
        return "❌ Weak password. Please follow these suggestions:\n" + get_improvements(length, uppercase, lowercase, digit, special)

def get_improvements(length, upper, lower, digit, special):
    suggestions = ""
    if not length:
        suggestions += "- Use at least 8 characters\n"
    if not upper:
        suggestions += "- Add uppercase letters (A–Z)\n"
    if not lower:
        suggestions += "- Add lowercase letters (a–z)\n"
    if not digit:
        suggestions += "- Include numbers (0–9)\n"
    if not special:
        suggestions += "- Use special characters (!@#$%^&* etc.)\n"
    return suggestions

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
