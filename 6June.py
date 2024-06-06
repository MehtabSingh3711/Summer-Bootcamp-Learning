# Print function
print("Hello world!")

# Input function
name = input("What is your name? ")
print("Hello, " + name + "!")

# Variables
x = 5
y = 3
print(x + y)

# Loops
# For loop
items = [1, 9, 0, 4, 1]
for item in items:
    print(item)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# If-Else statement
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

# Lambda function
square = lambda x: x ** 2
print(square(5))

# Using lambda() Function with map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

# Transform all elements of a list to upper case using lambda and map() function
strings = ["hello", "world", "python", "is", "fun"]
upper_strings = list(map(lambda x: x.upper(), strings))
print(upper_strings)

# Difference Between Lambda functions and def defined function
def cube(y):
    return y * y * y

lambda_cube = lambda y: y * y * y
print("Using function defined with def keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))