from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Hello():
    return {"message" : "Hello People"}

@app.get("/about")
async def about():
    return {"data" : "Creating my first FastAPI endpoints"}