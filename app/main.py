from fastapi import FastAPI
import sys, os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI(title="Sample of EdGPT", description="This is a sample of EdGPT", version="1.0")

@app.get("/", description="Hello World")
def read_root():
    return {"Hello": "GET"}

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)