from fastapi import FastAPI, Path, HTTPException
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

@app.get("/patients/{patient_id}")
def view_patient(patient_id : str = Path(..., description = "ID present in the DB", example = 'P001')):
    data = data_load()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found")
