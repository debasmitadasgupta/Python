#example1
def decorator_function(func):
    def add_message(name):
        return "welcome" + func(name)
    return add_message

@decorator_function
def friend(name):
    return name

print friend("Antara")

#example2
def decorator_function1(func):
    func.data=8
    return func

@decorator_function1
def myfunc(x,y):
    return x+y

print myfunc(2,4)
print myfunc.data