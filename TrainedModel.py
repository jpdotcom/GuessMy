from PIL import Image
import os
import tensorflow as tf
import numpy as np
import ast
from PIL import ImageOps
import time
np.set_printoptions(suppress=True)
path = "training_1"
s=os.path.dirname(path)
loaded_model=tf.keras.models.load_model(s)


def predict(img):
    
    img=ast.literal_eval(img)
    img=list(img.values())
    img=np.array(Image.fromarray(np.array(img,dtype='uint8').reshape(200,200,4)).resize((28,28)).convert('L')).reshape(1,28,28,1)/255
    start=time.time()
    results = loaded_model.predict(img)
    
    return "The number is " + str(np.argmax(results))




