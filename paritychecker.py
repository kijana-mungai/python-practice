# creating a function to check parity
# funciton subtracts the no by 2 until result is 0 else the no is odd
def parity(x):
    while x >= 2:
        x = x - 2
    if x == 0:
        return "Even"
    else:
        return "Odd"

print(parity(10))  