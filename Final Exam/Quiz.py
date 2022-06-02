def f1(i):
    return i ** 2

def f2(j):
    return (f1(j + 1))
print(f2(3))