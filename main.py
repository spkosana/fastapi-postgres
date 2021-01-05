from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def home():
    return {"application":"Welcome :), Surya Prakash is Special"}
