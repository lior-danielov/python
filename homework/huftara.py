import random

password = []
letters = ['a', 'b', 'c']

password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
print(f"before\n(password)")  # placeholder or interpolation

random.shuffle(password)
print(f"\n\nAfter\n{password}")
