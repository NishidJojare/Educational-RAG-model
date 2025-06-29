from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import search
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from datetime import datetime



retrieval_chain = None



@asynccontextmanager
async def lifespan(app: FastAPI):
    global retrieval_chain
    print("⏳ Initializing retrieval chain once...")
    retrieval_chain = search.get_retrieval_chain()
    print("✅ Retrieval chain ready.")
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



class Query(BaseModel):
    message: str



@app.post("/")
async def ask_query(query: Query):
    try:
        global retrieval_chain
        print("Received question:", query.message)
        answer = search.ask_question(query.message,retrieval_chain)

        # adding conversation history/logs
        with open("history.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
            log_file.write(f"# Question : {query.message}\n")
            log_file.write(f"# Answer : {answer}\n")
            log_file.write("-" * 50 + "\n\n")

        return {"answer": answer}
    
    except Exception as e: 
        print(f"Oops, Something went wrong : {e}")


# # start cmd : fastapi dev main.py
