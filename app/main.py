from fastapi import FastAPI, Request
from tensorflow import keras
import uvicorn
import os
import pandas as pd

bird_dex = pd.read_csv("/code/app/dict_liste_oiseaux.csv")
app = FastAPI()
model = keras.models.load_model('/code/app/model.h5')


@app.get('/')
def home():
    return({"Bienvenue" : "bienvenue"})

@app.post('/predict')
async def get_prediction(request : Request):
    
    mat = await request.json()
    mat = eval(mat)
    predict = model.predict(mat['Image'])
    predict = predict.argmax() + 1

    return({"result" : bird_dex[bird_dex['number'] == predict]["name"].values[0]})

if __name__ == '__main__':
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
