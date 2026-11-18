# Write a Python program to implement a sequence of even numbers less than 20 using python generators.

# Do not create function with additional parameter. The tests are designed in a way that they will internally call the even_numbers() function.

def even_numbers():
    for number in range(20):
        if number % 2 == 0:
            yield number
