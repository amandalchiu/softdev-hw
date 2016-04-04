def h(x):
    return lambda y: x + y

b = h(1)
#print b(3)
#print h(1)(3)

#Task
def repeat(str):
    return lambda n: str * n

print repeat('cool')(3)


def r1(n):
    return repeat('hello')(n)
def r2(n):
    return repeat('goodbye')(n)

print r1(2)
print r2(2)
