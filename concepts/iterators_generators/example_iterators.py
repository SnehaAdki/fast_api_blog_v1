class InfiniteNaturalNumbers():
    def __init__(self) -> None: 
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num +=1
        return num

values = iter(InfiniteNaturalNumbers())
print(next(values))
print(next(values))
print(next(values))