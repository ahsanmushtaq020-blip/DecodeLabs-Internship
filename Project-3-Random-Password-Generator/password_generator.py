import random
import string


print("===== RANDOM PASSWORD GENERATOR =====")

try:
    password_length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a valid number.")
else:
    if password_length < 4:
        print("Password length should be at least 4.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password_characters = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]

        for _ in range(password_length - 4):
            password_characters.append(random.choice(characters))

        random.shuffle(password_characters)
        password = "".join(password_characters)
        print(f"Generated Password: {password}")
