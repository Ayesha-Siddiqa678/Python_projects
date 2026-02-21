#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Percentage Calculator in Python

def calculate_percentage(part, whole):
    return (part / whole) * 100

part = float(input("Enter the part value: "))
whole = float(input("Enter the whole value: "))

percentage = calculate_percentage(part, whole)
print(f"The percentage is: {percentage:.2f}%")


# In[2]:


# Prime number checker between two numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

# Get input from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num)


# In[ ]:


#Fun program to pass time by guessing numbers.

import random

number = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100!")

while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! The number was", number)


# In[ ]:




