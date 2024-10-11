# List
# %%
cars = ['Honda', 'Ford', 'Tesla', 'BMW', 'GMC']

# %%
# Use the len() method to return the length of a list
print(f'Number of cars: {len(cars)}')

# %%
# Operations over list
values = [5, 4, -4, 8.9, -2.5, 12, 7.8]
print(len(values))
print(max(values))
print(min(values))
print(sum(values))

# %%
# Refer to a list element by referring to the index number (0-based)
print(f'First car is {cars[0]}')
print(f'First car is {cars[3]}')

print(f'First car is {cars[len(cars)-1]}') # to print the last item if I don't know it
print(f'First car is {cars[-1]}')  # to print last car
print(f'First car is {cars[-2]}')
# %%
# List Comprehension
terms = 'Advanced Concepts in Data Analytics'

# %%
# Example 1 - get all letters in a string and store them in a list
#find any letter in the string and append the letters in a list
all_letters = []
for letter in terms:
    all_letters.append(letter)  
print(all_letters)

# %%

# A more Pythonic way to achieve this task is as follow.
all_letter = [letter for letter in terms]
print(all_letters)

# %%


# Example 2 - get all non-vowel letters in a string and store in a list
vowels = 'aeiou'
non_vowel_letters = [letter for letter in terms if letter not in vowels]
print(non_vowel_letters)

#%%
# Module operators



# Example 3 - get all odd number from 10 to 100 and store in a list



# Example 4 - multiple all numbers by 3 in a list



