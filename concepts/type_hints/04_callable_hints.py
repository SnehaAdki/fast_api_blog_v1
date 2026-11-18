
def smart_divide(func : Callable[[int,int],float]):
    def inner(a,b):
        if b == 0 :
            print("Division by zero!.... ")
            return None
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)


divide(9,0)