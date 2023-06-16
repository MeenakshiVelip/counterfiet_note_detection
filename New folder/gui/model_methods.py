from plistlib import load
import skimage
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2


def predict_image(file_name):
    img = cv2.imread(file_name) # read
    img = cv2.resize(img,(500,500)) # resize
    model = tf.keras.models.load_model("./saved_model/v1.0")
    pred = model.predict(np.array([img]))[0][0] # predict
    return "Real Note" if pred == 1.0 else "Fake Note"