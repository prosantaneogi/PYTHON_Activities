def fibonacci(numberofelm):
    if numberofelm <=1:
        return numberofelm
    else:
        return (fibonacci(numberofelm-1)+fibonacci(numberofelm-2))

numbers= int((input("Enter the numberof element")))

if numbers <= 0:
    print("Please enter a valid positive number")
else:
    for x in range(numbers):
        print(fibonacci(x))
