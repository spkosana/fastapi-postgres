from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
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
            <img src="https://raw.githubusercontent.com/mdn/learning-area/master/html/multimedia-and-embedding/images-in-html/dinosaur_small.jpg"  align=“center”>
            <ul>
                <li><a href="https://www.linkedin.com/in/spkosana/">Linked In</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
