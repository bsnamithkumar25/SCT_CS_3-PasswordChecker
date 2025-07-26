import re

MIN_LENGTH = 8
SPECIAL_CHARACTERS = r"[!@#$%^&*()_+=\-{}\[\]:\";'<>?,./]"

def assess_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        remarks.append(f"Password is too short (minimum {MIN_LENGTH} characters).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Include at least one uppercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Include at least one digit (0-9).")

    if re.search(SPECIAL_CHARACTERS, password):
        score += 1
    else:
        remarks.append("Include at least one special character (e.g., @, #, $, etc.).")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }
    strength = strength_levels.get(score, "Unknown")

    return strength, remarks

def display_feedback(strength, remarks):
    print(f"\nPassword Strength: {strength}")
    if remarks:
        print("Suggestions to improve your password:")
        for remark in remarks:
            print(f"- {remark}")

def main():
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter your password: ").strip()
    
    strength, feedback = assess_password_strength(password)
    display_feedback(strength, feedback)

if __name__ == "__main__":
    main()
