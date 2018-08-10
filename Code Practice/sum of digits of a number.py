number= 1234

def sumOfDigits(num):
    sum=0
    while(num > 0):
        digit=num % 10
        sum +=digit
        num=num/10
    return sum



print (sumOfDigits(1234))