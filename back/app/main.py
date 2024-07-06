from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_teddynote import logging
from langchain_openai import ChatOpenAI
# API KEY 정보로드
load_dotenv()
# FastAPI 앱 생성
app = FastAPI()
# 프로젝트 이름을 입력합니다.
logging.langsmith("apitester")
# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    model_name="gpt-4o",  # 모델명

)
class Question(BaseModel):
    question: str
    
# 엔드포인트 정의
@app.post("/ask")
async def ask_question(question: Question):
    answer = llm.invoke(question.question)
    return {"답변": answer}