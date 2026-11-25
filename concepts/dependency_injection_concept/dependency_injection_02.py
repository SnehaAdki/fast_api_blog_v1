from fastapi import FastAPI, Depends,status

development_db = ["DB for Developments"]
def get_db_session():
    return development_db

app = FastAPI()

@app.post("/items")
def add_item(item : str, db = Depends(get_db_session)):
    db.append(item)
    print("----- db ----")
    print(db)
    return {"message" : f"Added item {item}", "status_code": status.HTTP_201_CREATED} 

