from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def home():
    return {"application":"Welcome :), Surya Kosana is Special"}
