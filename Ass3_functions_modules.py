def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
sample_number = 5

result = factorial(sample_number)
print(f"The factorial of {sample_number} is {result}")

import math

number = float(input("Enter a positive number: "))

if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"\nResults for the number {number}:")
    print(f"Square root: {square_root}")
    print(f"Natural logarithm: {natural_log}")
    print(f"Sine: {sine_value}")
else:
    print("Please enter a positive number greater than zero for valid log and square root.")
