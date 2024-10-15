#%%
# Use def keyword to define a function
def greeting(name):
    print(f'Hi {name}, welcome to ACDA class!')

greeting('Heather')

#%%
# Use return keyword if the function has a return value.
#%%
def add( a, b):
    return a + b

print(add(23, 12))

print(add('hello', 'Bye'))

print(12, 'Bye')
#%%

def new_add( a: int, b: int):
    return a + b

print(new_add(12, 45))
print(new_add(12, 45.8))

#%%

# Declare the data type


# Casting the variables

# %%
a = 22
b = '35'

print(str(a) + b) ## casting  a to string
print( a + int(b)) ## casting and intiger

# %%
