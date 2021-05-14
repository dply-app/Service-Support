from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Problem_link : File 

class bugreport_tools(BaseModel):
    User_email : str
    Explanation : str

class ask_tools(BaseModel):
    User_email : str
    question : str

class partnership_tools(BaseModel):
    Server_name : str
    Server_link : str
    Server_github : str
    Server_introduction : str
    Server_host_tag : str

@app.get("/")
def read_root():
    return {"Test" : "True"}

@app.get("/bugreport")
def bugreport(bugreport:bugreport):
    return {"email" : bugreport.User_email}

@app.get("/ask")
def ask(ask:ask):
    return {"email" : ask.User_email}

# TODO: make report

@app.get("/partnership")
def partnership(partnership:partnership):
    return {"email":partnership.User.email}

# uvicorn main:app --reload --host 0.0.0.0