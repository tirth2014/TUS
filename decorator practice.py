def fun1(func):
    def fun2():
        print("before execution")

        func()
        print('aftr execution')
    return fun2

@fun1
def anotherFun():
    print('inner function')


# anotherFun = fun1(anotherFun)
anotherFun()
