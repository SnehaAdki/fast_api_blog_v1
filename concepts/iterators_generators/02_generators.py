# return some value



def return_values():
    yield 1
    yield 2
    yield "three"


value = return_values()
print(value.__next__())
print(value.__next__())
print(value.__next__())