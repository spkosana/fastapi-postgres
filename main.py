from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def home():
    return {"application":"fastapi-postgres"}
