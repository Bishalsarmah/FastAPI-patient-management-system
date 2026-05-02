from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/sort")
def sort_patients(sort_by : str = Query(..., description ="Sort on the basis of height, weight or BMI"),
                  order : str = Query('asc', description = "Sort by ascending or descending")):
    valid_col = ['height','weight','bmi']
    if sort_by not in valid_col:
    # Use f-string to show the columns, and fix status_code
        raise HTTPException(status_code=400, detail=f"Invalid column. Select from {valid_col}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'")
    sort_order = True if order == 'desc' else False
    data = data_load()
    data_sorted = sorted(data.values(), key = lambda x : x.get(sort_by, 0), reverse=sort_order)
    return data_sorted