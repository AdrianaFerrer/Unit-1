# Operators
# %%
x = 25
y = 3

# %%
# Arithmetic operators
# x + y
# x - y
# x * y
# x / y 
# x ** y 
# x % y
# x // y

print(x ** y)
print(x // y)
print(x % y)

# Example 3 - get all odd number from 10 to 100 and store in a list
# %%
odd_numbers = [i for i in range(10,101) if i % 2 !=0]
print(odd_numbers)

odd_numbers_2 = [i for i in range(10,101) if i % 2 !=0]
print(odd_numbers_2)

even_numbers = [i for i in range(10,101) if i % 2 ==0]
#%%
# Example 4 - multiple all numbers by 3 in a list

print([i for i in range(5,20,2)])

print([i * 3 for i in range (5,20,2)])

# %%
# Assignment Operator



# Comparison operators
# x == y
# x != y
# x > y
# x < y
# x >= y
# x <= y

# %%

# Logical operators
print(x > 1 and x < 10)
print(x > 1 or x < 10)
print(not(x < 5))


# %%

# Identity operators

print(x is y)
print(x is not y)
#%%
# Membership Operators
