from fastapi import FastAPI, Depends , HTTPException, status

blogs = {
    "1" : "Fastapi Prerequistie",
    "2" : "Building API's with FastAPI",
    "3" : "Background Tasks | Celery X FastaPI"
}

users = {
    "8" : "Jamie" , 
    "9" : "Roman"
}

app = FastAPI(
    title="Dependency Injection"
)

# def get_model_or_404(model : dict , id: str):
#     obj = model.get(id)
#     if not obj:
#         raise HTTPException(detail=f"Model with {id} doesnt not exist",status_code=status.HTTP_404_NOT_FOUND)
#     return obj 

class GetObjectOR404 : 
    def __init__(self,model) -> None:
        self.model = model

    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"model with {id} doesnt not exist",status_code=status.HTTP_404_NOT_FOUND)
        return obj 


blog_dependecy = GetObjectOR404(blogs)
@app.get("/blog/{id}")
def get_blog(blog_name : str = Depends(blog_dependecy)):
    return blog_name


user_dependecy = GetObjectOR404(users)
@app.get("/user/{id}")
def get_blog(user_name : str = Depends(user_dependecy)):
    return user_name