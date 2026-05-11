import random
import string
 
 
def generate_password(length=12, use_upper=True, use_lower=True,
                      use_digits=True, use_special=True):
    character_pool = ""
    guaranteed = []
 
    if use_upper:
        character_pool += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        character_pool += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        character_pool += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_special:
        character_pool += string.punctuation
        guaranteed.append(random.choice(string.punctuation))
 
    if not character_pool:
        print("Error: Select at least one character type.")
        return None
 
    remaining = [random.choice(character_pool) for _ in range(length - len(guaranteed))]
    password_list = guaranteed + remaining
    random.shuffle(password_list)
    return "".join(password_list)
 
 
def check_strength(password):
    score = 0
    if len(password) >= 8:   score += 1
    if len(password) >= 12:  score += 1
    if len(password) >= 16:  score += 1
    if any(c.isupper() for c in password):             score += 1
    if any(c.islower() for c in password):             score += 1
    if any(c.isdigit() for c in password):             score += 1
    if any(c in string.punctuation for c in password): score += 1
 
    if score <= 3:   return "Weak"
    elif score <= 4: return "Medium"
    elif score <= 5: return "Strong"
    else:            return "Very Strong"
 
 
def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("   Please enter y or n.")
 
 
def get_positive_int(prompt, default=12):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            value = int(raw)
            if value < 4:
                print("   Minimum length is 4.")
            elif value > 128:
                print("   Maximum length is 128.")
            else:
                return value
        except ValueError:
            print("   Please enter a valid number.")
 
 
def main():
    print("=" * 50)
    print("      SECURE PASSWORD GENERATOR")
    print("  Synent Technologies - Python Internship")
    print("=" * 50)
 
    while True:
        print()
        length = get_positive_int("Enter password length (default 12): ", default=12)
 
        print("\nSelect character types to include:")
        use_upper   = get_yes_no("  Uppercase letters (A-Z)?")
        use_lower   = get_yes_no("  Lowercase letters (a-z)?")
        use_digits  = get_yes_no("  Numbers (0-9)?")
        use_special = get_yes_no("  Special characters (!@#$...)?")
 
        how_many = input("\nHow many passwords? (default 1): ").strip()
        count = int(how_many) if how_many.isdigit() and int(how_many) > 0 else 1
 
        print("\n" + "-" * 50)
        print("  Generated Password(s):")
        print("-" * 50)
 
        for i in range(1, count + 1):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_special)
            if pwd:
                strength = check_strength(pwd)
                print("  [" + str(i) + "] " + pwd)
                print("      Strength: " + strength)
 
        print("-" * 50)
 
        again = get_yes_no("\nGenerate more passwords?")
        if not again:
            print("\nThank you! Stay secure.\n")
            break
 
 
if __name__ == "__main__":
    main()