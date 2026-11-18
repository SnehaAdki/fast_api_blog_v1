class Pydantic:
    def is_valid(self, text):
        if "admin" in text:
            return False
        return True

class Starlette: 
    def is_valid(self,text):
        return True

# mixins for multiple inhertiance 
# mro is method resolution order
class FastAPI(Pydantic,Starlette):
    pass

fs = FastAPI()
print(FastAPI.__mro__)
print(fs.is_valid("admin tried to sign in"))