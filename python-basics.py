# # print("Hello World")

# # Variables
# # a = 3
# # a = 32
# # a = 1
# # print(a + a + a)

# # data types

# # a = 3.63844
# # b = 23
# # c = True
# # d = "happy day"
# # d1 = '123@£$%ahdjdf'
# # print(type (a))
# # print(type (b))
# # print(type (c))
# # print(type (d))
# # print(type (d1))

# # type conversion
# # print(int(a))
# # print(float(b))

# # Concatination
# # print ("my " + "name " + "is " + "ade ")
# # print(str(300) + " dollars" )


# name = input(" Please enter your name: ")
# age = input("please enter your age: ")
# print(type(age))
# newAge = int(age) + 5
# print("your name is " + name + "and you age is " + str(newAge))

# word = "Helicopter"
# print(word[0])
# print(word[4])
# print(word[9])
# print(word[0:4])
# print(word[-1])
# print(word[-2:7]) 10 - 99

# Assignment
# number = input("please enter two digit number: ")
# a = number[0]
# b = number[1]
# print()
#  number = input("enter height and mass")
# mass = number[0]
# height = number[1]
# weight = height/mass
# print("your weight is " +weight)
# BMI

# height = float(input("enter height in meters: "))
# weight = float(input("enter your weight in kilogram: "))
# bmi = weight/(height**2)
# print(round(bmi, 2))

# number = int(input("enter any number: "))
# if (number % 2) == 0:
#  print("You have entered and even number")
# else:
#  print("you have enterd an odd number")


# height = float(input("enter height in meters: "))
# weight = float(input("enter your weight in kilogram: "))
# bmi = weight/(height**2)
# print(round(bmi, 2))
# if bmi == 18.5:
#  print("underweight")

# import random
# dice_value = random.randint(1, 6)
# print(dice_value)

# import random
# coin_toss = random.choice(0,1)
# print(coin_toss)

# fruits = ["apple", "peach", "orange"]
# for fruit in fruits: 
#     print(fruit)
#     print(f"{fruit} pie")
#     print(fruits)
# for i in range(0, 100):
#   print(i++)

#   for n in range(0, 100):
#     n =
# def my_function():
#     print("Hello")
#     print("Nice to meet you")
# my_function()


# Basics
print ("hello")
print ('hello')
# print (hello)

print(4 + 5)
print(8 * 3)
print(4 / 3)
print(4.0 / 3)
print(3 + 5 * 9)

first = "hello"
second = "world"
first + " " + second
type(first)
print (first)

name = input("what is your name?")
type(name)
age = input("What is your age?")
type(age)

import math

# Convert 32 degrees to radians
degrees = 32
radians = degrees * (math.pi / 180)
print(f"{degrees} degrees is equal to {radians:.2f} radians.")

# Ask user for radius, then calculate surface area and volume of a sphere
radius = float(input("Enter the radius of the sphere: "))
surface_area = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3
print(f"Surface area of the sphere: {surface_area:.2f} units²")
print(f"Volume of the sphere: {volume:.2f} units³")

# Get the current time and format it nicely
import datetime
now = datetime.datetime.now()
time_of_day = now.strftime("%I:%M %p")
print(f"The current time is {time_of_day}.")

# Split a sentence into its words
sentence = "The quick brown fox jumps over the lazy dog."
words = sentence.split()
print(f"The sentence '{sentence}' contains {len(words)} words.")

# Join a list of words into a sentence (two ways)
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

# Method 1: Using join() with a space separator
sentence1 = ' '.join(words)
print(f"Sentence 1: {sentence1}")

# Method 2: Using a loop to concatenate the words
sentence2 = ""
for word in words:
    sentence2 += word + " "
sentence2 = sentence2.strip()
print(f"Sentence 2: {sentence2}")

# Functions
def get_age():
    age = input("Please enter your age: ")
    return int(age)

def get_name():
    name = input("Please enter your name: ")
    return name

def main():
    name = get_name()
    age = get_age()
    print(f"Hello, {name}! I know that you are {age} years old.")

if __name__ == "__main__":
    main()



def calculate(operation, num1, num2):
    """Performs the specified arithmetic operation on two integers."""
    operation = operation.lower()  # Convert operation to lowercase for case-insensitivity
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

# Example usage (optional)
if __name__ == "__main__":
    op = input("Enter operation (add, subtract, multiply, divide): ")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    result = calculate(op, n1, n2)
    print(f"The result of {op}ing {n1} and {n2} is: {result}")

    # loops
    i = 7
while(i <= 19):
    print(i)
    i += 1  # Increment i by 1
# while loops
    i = 12
while(i <= 20):
    if i % 2 == 0:  # Check if the number is even
        print(i)
    i += 1  # Increment i by 1v


# Reverse Even numbers
    def evens(start, end):
    # """Prints all even numbers between start and end."""
     for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

def reverse_evens(start, end):
    """Prints all even numbers between start and end in reverse order."""
    for i in range(end, start - 1, -1):
        if i % 2 == 0:
            print(i)

# Example usage
print("Even numbers between 12 and 20:")
evens(12, 20)

print("\nEven numbers between 12 and 20 in reverse:")
reverse_evens(12, 20)

# range prints all the numbers in the range 1 to 11
for i in range(1,11):
    print (i) 

# j prints the numbers 1, 2, 3
for j in [1, 2 3]:
    print (j)