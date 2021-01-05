from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def home():
    html_content = """
    <html>
        <head>
            <title>Surya</title>
        </head>
        <body>
            <h1>Surya Prakash is Special</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
