import random as rn
import string as st
numbers = "1234567890"
abc_upper = st.ascii_uppercase
abc_lower = st.ascii_lowercase
characters = st.punctuation
passwrd = []

def password():
    number: int = int(input("Enter the quantity of the your desired password: "))
    upper = input("Do you want upper letters? (y/n) ")
    if upper.upper() == "Y":
        for n in range(number):
            passwrd.append(rn.choice(rn.choice([numbers, abc_lower, abc_upper, characters])))

    elif upper.upper() == "N":
        for n in range(number):
            passwrd.append(rn.choice(rn.choice([numbers, abc_lower, characters])))
    else: 
        print("You must select y or n")
        return None
    return ''.join(passwrd)

print("Generated password:", password())
    

