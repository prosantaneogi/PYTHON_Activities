# Activity 8
# Given a list of numbers, return True if first and last number of a list is same.
# Bonus points if you can make the user enter their own list.

numbers = (list(input("Enter the list of numbers as per the format [1,2,..] :")))
def comparetwonumbers(numbers):
    fnumber = numbers[0]
    lnumber = numbers[-1]
    print(numbers)
    if (fnumber == lnumber):
        print('First and Last Number is same')
    else:
        print('First and Last number is not same')


comparetwonumbers(numbers)
