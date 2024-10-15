#Asks for your name
#%%

name = input("What is your name?")
print(name)

#Asks for your year of birth
birth_year = int(input("Enter your year of birth"))
print(birth_year)

#Greets you with “Hello”

def greeting(name):
    print(f'Hello {name}')
greeting({name})

#Calculates and tells you your age

from datetime import datetime
current_year = datetime.now().year

def calculate_age(birth_year):
    age = current_year - birth_year
    print(f"Your current age is: {age}")

calculate_age(birth_year)

#%%


#Says “Goodbye” at the end of program

# %%
