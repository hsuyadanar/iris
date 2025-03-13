from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Load the trained model
model = joblib.load('model/iris.pkl')

# Create Instance for API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data model for prediction
class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define a prediction endpoint
@app.post("/predict/")
def predict_species(iris: IrisSpecies):

    # Convert iris to NumPy array
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
     
    # Predict species
    prediction = model.predict(data)
    predicted_species = prediction[0]
    
    return {"species": predicted_species}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier!"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8888)


# uvicorn main:app --reload
