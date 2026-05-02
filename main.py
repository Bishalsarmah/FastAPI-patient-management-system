from fastapi import FastAPI
import json

app = FastAPI()

def data_load():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
async def Hello():
    return {"message" : "Hello People"}

@app.get("/about")
async def about():
    return {"data" : "Creating my first FastAPI endpoints"}

@app.get("/view")
def view():
    data = data_load()
    return data