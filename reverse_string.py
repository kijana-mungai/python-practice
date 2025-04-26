def reverse(x):
    reversed_string = ""
    i = len(x) - 1 # comp starts counting from 0
    while i >= 0: # condition    to ensure that all letters are included
        reversed_string = reversed_string + x[i]
        i = i - 1
    return reversed_string
print(reverse("GoodMorning")) #test