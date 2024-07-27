import random
import string

def mypassword(min_length=12, max_length=18):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special

    password_length = random.randint(min_length, max_length)

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_characters, k=password_length - 4)

    random.shuffle(password)

    return ''.join(password)

# now generate and print a random password
print(mypassword())
