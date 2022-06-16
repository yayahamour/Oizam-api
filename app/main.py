from fastapi import FastAPI, Request, File, UploadFile
from tensorflow import keras
import uvicorn
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


bird_dex = pd.read_csv("/code/app/dict_liste_oiseaux.csv")
app = FastAPI()
model = keras.models.load_model('/code/app/model.h5')


@app.get('/')
def home():
    return({"Bienvenue" : "bienvenue"})

@app.post('/predict/')
async def get_prediction(file: UploadFile(...)):
    # img = image.load_img(file, target_size=(299, 299))
    img_array = image.img_to_array(file.read())
    img_batch = np.expand_dims(img_array, axis=0)
    preprocessed_image = tf.keras.applications.xception.preprocess_input(img_batch)

    predict = model.predict(preprocessed_image)
    predict = predict.argmax() + 1

    return({"result" : bird_dex[bird_dex['number'] == predict]["name"].values[0]})

if __name__ == '__main__':
    uvicorn.run("__main__:app", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
