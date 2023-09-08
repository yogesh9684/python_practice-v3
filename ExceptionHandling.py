def exceptionhandling():
    try:
        a = 10
        b = 20
        c = 'Test'
        d = (a+b)/c
        print(d)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except TypeError:
        print("Can't Add String to Integer")
exceptionhandling()