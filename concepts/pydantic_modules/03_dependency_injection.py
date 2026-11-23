from fastapi import FastAPI, Depends

blogs = {
    "1" : "FastaPI Prerequisite",
    "2" : "Building API's with FastAPI",
    "3" : "FastaPI Prerequisite"
}

users = {
    "8" : "Jamine",
    "9" : "Roman"
}

app = FastAPI(title = "Dependency Injection")
