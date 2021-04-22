import tensorflow as tf
from tensorflow import keras

import tensorflow_datasets as tfds
import os
import json
import h5py
from PIL import Image

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train=x_train.reshape(60000, 28, 28, 1)/255

x_test=x_test.reshape(10000,28,28,1)/255



s=os.path.dirname(os.path.abspath('TrainingModel1_saved'))+"\TrainingModel1_saved"
print(s)
model=keras.models.Sequential([
    keras.layers.Conv2D(32,3,activation="relu",input_shape=[28,28,1]),
    keras.layers.MaxPooling2D(2),
    keras.layers.Dropout(0.25),
    keras.layers.Conv2D(64,3,activation="relu",padding='same'),
    keras.layers.MaxPooling2D(2),
    keras.layers.Dropout(0.25),
    keras.layers.Conv2D(128,3,activation="relu",padding='same'),
    keras.layers.MaxPooling2D(2),
    keras.layers.Dropout(0.4),
    keras.layers.Flatten(),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10,activation="softmax"),
])
model.compile(
    optimizer='adam',
 
    loss=keras.losses.SparseCategoricalCrossentropy(),
    
    metrics=['accuracy'],
)

model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=100,
    validation_data=(x_test, y_test),
)


model.save(s)





