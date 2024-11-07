# 8 character password
# 1 special character
# 1 uppercase 
# 1 lowercase
# 1 digit
import random
import string

# Making a special character variable
special_characters = "!£$%^&*()_+[]@:#~<>,.?"

# generating 1 random for each required character
random_lowercase = random.choices(string.ascii_uppercase)
random_uppercase = random.choices(string.ascii_lowercase)
random_digit = random.choices(string.digits)
random_special = random.choices(special_characters)

# making a password list, will combine all characters and jumble at the end
password = []
