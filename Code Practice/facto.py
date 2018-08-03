
def facto(number):
    if number <= 1:
        return number
    else:
        return number * facto(number-1)

print facto(5)