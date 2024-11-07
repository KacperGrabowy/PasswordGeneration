# 8 character password
# 1 special character
# 1 uppercase 
# 1 lowercase
# 1 digit
import random
import string

# Making a special character variable
special_characters = "!£$%^&*()_+[]@:#~<>,.?"

# making a password list, will combine all characters and jumble at the end
password = []

# generating 1 random for each required character
random_uppercase = random.choices(string.ascii_uppercase)
password.append(random_uppercase)
random_lowercase = random.choices(string.ascii_lowercase)
password.append(random_lowercase)
random_digit = random.choices(string.digits)
password.append(random_digit)
random_special = random.choices(special_characters)
password.append(random_special)

# testing if 4 random characters are chosen as attempted above
print(password)

for i in range(4):
    i+1
    random_number = random.randint(1, 4)