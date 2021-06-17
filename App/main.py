# -*- coding: utf-8 -*-
import uvicorn
from md_write import *
from email_write import *
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

class bugreport_tools(BaseModel):
    User_email : str
    Problem_Code : str
    Explanation : str

class ask_tools(BaseModel):
    User_email : str
    question : str

class report_tools(BaseModel):
    User_email : str
    Report_contents : str
    Explanation : str

class partnership_tools(BaseModel):
    Server_name : str
    Server_link : str
    Server_github : str
    Server_introduction : str
    Server_host_tag : str


# =========================================테스트 API 코드 START===================================

# 메인 API 코드
@app.get("/")
def read_root():
    return {"Test" : "True"}

# =========================================테스트 API 코드 END=====================================

# =========================================버그제보 API 코드 START=================================

#버그 제보
@app.post("/bugreport")
def bugreport(bugreport_tools:bugreport_tools):
    main.bugreport(email=bugreport_tools.User_email,contents=bugreport_tools.Problem_Code,explanation=bugreport_tools.Explanation)
    emailwrite.emailwrite(title=bugreport_tools.User_email,into="에러 확인 요청",data=bugreport_tools.User_email+"`s bugreport.md")
    return {"email" : bugreport_tools.User_email, "Explanation" : bugreport_tools.Explanation}

# =========================================버그제보 API 코드 END===================================

# =========================================질문 API 코드 START=====================================

#질문 제보
@app.post("/ask")
def ask(ask_tools:ask_tools):
    main.ask_md(email=ask_tools.User_email,question=ask_tools.question)
    emailwrite.emailwrite(title=ask_tools.User_email,into="질문 신청 요청",data=ask_tools.User_email+"`s ask.md")
    return {"email" : ask_tools.User_email, "question":ask_tools.question}

# =========================================질문 API 코드 END========================================

# =========================================신고 API 코드 END========================================

@app.post("/report")
def report(report_tools:report_tools):
    main.report(email=report_tools.User_email,contents=report_tools.Report_contents,explanation=report_tools.Explanation)
    emailwrite.emailwrite(title=report_tools.User_email,into="신고 확인 요청",data=report_tools.User_email+"`s report.md")
    return {"email" : report_tools.User_email, "Report_contents" : report_tools.Report_contents, "Explanation" : report_tools.Explanation}

# =========================================신고 API 코드 END========================================

# =========================================파트너쉽 API 코드 START===================================

#파트너쉽 안내 
@app.post("/partnership")
def partnership(partnership_tools:partnership_tools):
    main.partnership_md(title=partnership_tools.Server_name,link=partnership_tools.Server_link,tag=partnership_tools.Server_host_tag, github=partnership_tools.Server_github,into=partnership_tools.Server_introduction)
    emailwrite.emailwrite(title=partnership_tools.Server_name,into="파트너쉽 신청 요청",data=partnership_tools.Server_name+".md")
    return {"Server_name" : partnership_tools.Server_name, "Server_link" : partnership_tools.Server_link, "Server_github" : partnership_tools.Server_github, "Server_introduction" : partnership_tools.Server_introduction, "Server_host_tag" : partnership_tools.Server_host_tag}

# =========================================파트너쉽 API 코드 END======================================

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)