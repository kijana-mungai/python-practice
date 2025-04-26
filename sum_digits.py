def sum_of_digits(x):
    total = 0
    while x > 0:
        total = total + (x % 10)  # Add the last digit to the total
        x = x // 10  # Remove the last digit from the number
    return total
print(sum_of_digits(12)) #test