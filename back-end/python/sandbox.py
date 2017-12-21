x = 50


def func():
    global x
    x = 1000


print(f'x is equal to {x}')
func()
print(f'x is equal to {x}')
