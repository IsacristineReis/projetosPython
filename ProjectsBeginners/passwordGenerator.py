'''

- collect user preferences
    - length
    - should contain uppecase
    - should contain special
    - should contain digits

- get all available characters
- randomly pick characters up to the length
- ensure we have at leasst one of each character type
- ensure length is valid

'''

import random as rd
import string as st

def generate_password():

    length = int(input("Enter the desired password length: ").strip())

    if length < 4:
        print("The password length must be at leats 4 characters.")
        return

    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digitss? (yes/no): ").strip().lower()

    lower = st.ascii_lowercase #alfabeto
    uppercase = st.ascii_uppercase if include_uppercase == 'yes' else '' #Inline
    special = st.punctuation if include_special == 'yes' else '' #Inline
    digits = st.digits if include_digits == 'yes' else '' #Inline
    all_characters = lower + uppercase + special + digits

    required_characters = [] #mais flexível
    if include_uppercase == 'yes':
        required_characters.append(rd.choice(uppercase))
    if include_special == 'yes':
        required_characters.append(rd.choice(special))
    if include_digits == 'yes':
        required_characters.append(rd.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = rd.choice(all_characters)
        password.append(character)

    rd.shuffle(password)

    str_password = "".join(password)
    return str_password

password = generate_password()
print(f"The random password is {password}")