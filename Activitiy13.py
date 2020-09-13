def calculate_sum(numlist):
    sum = 0
    for num in numlist:
        sum +=num
    return sum
numlist1=[1,2,3,4,5,6,6,7,7,8,98]
sum1=calculate_sum(numlist1)
print(str(sum1))
