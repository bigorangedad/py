


name ='tome'

a = 1

def func():
    global a
    a = 2
    print(f"a = {a}")


func()
print(a)
