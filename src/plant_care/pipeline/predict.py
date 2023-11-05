import os
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

from plant_care.constants import *



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self, name: str):
        # load model
        model = load_model(os.path.join("artifacts","prepare_callbacks",name,"checkpoint_dir","model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=TARGET_SIZE[f"{name}"])
        test_image = image.img_to_array(test_image)

        test_image = test_image / 255.0

        test_image = np.expand_dims(test_image, axis = 0)
        pred = model.predict(test_image)
        result = np.argmax(pred, axis=1)

        if(result >= len(CLASSES[f"{name}"])) :
            return f"Either the image is not of a {name} plant or it's a new disease"

        print(imagename)
        print(pred)
        print("arr :",CLASSES[f"{name}"])
        print("index :", result[0])

        # print()
        # print(test_image)
        # print()
        return CLASSES[f"{name}"][result[0]]
    
