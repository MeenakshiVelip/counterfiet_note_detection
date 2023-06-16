from tensorflow.keras.models import Model
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

class FinalInference:
    def __init__(self, model_path=None):
        if not model_path:
            self.model_path = "./saved_model/v1.0"
        else:
            self.model_path = model_path
        
        self.model = tf.keras.models.load_model(self.model_path)

    def predict_counterfiet_note(self, file_path):
        img = cv2.imread(file_path)
        img = cv2.resize(img,(500,500))
        pred = self.model.predict(np.array([img]))[0][0]
        return "Real Note" if pred == 1 else "Fake Note"
