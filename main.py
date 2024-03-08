from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from data_cleaning import process_messages
from typing import List
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from model import summarizer

class Message(BaseModel):
    _id: int
    address: str
    body: str
    creator: str
    date: int
    date_sent: int
    error_code: int
    locked: int
    protocol: int
    read: int
    reply_path_present: int
    seen: int
    status: int
    sub_id: int
    thread_id: int
    type: int

app = FastAPI(title="NLP Backend", reload=False)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def root():
    return JSONResponse(content={"message": "Hello World!"}, status_code=200)

@app.post("/summarize_text")
async def summarize_text(text: str):
    try:
        result = await summarizer(text)
        return JSONResponse(content={"summary": result}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post('/send-data')
async def send_data(data: List[Message]):
    try:
        result = []
        for msg in data:
            result.append(msg.dict())

        result = await process_messages(result)
        return JSONResponse(content=result, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
