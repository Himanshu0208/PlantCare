from http import client
from venv import logger
from flask import Flask, request, jsonify, render_template
import os
import openai
import cloudinary
import cloudinary.uploader
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from plant_care.utils.main_utils import decodeImage
from plant_care.pipeline.predict import PredictionPipeline
from plant_care.constants import *

load_dotenv()
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

openai.api_key = os.getenv("OPENAI_API_KEY")
def openai_api(plant_name: str, disease: str, lang: str) -> str:  
    completion1 = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"My {plant_name} plant has {disease}; 3 precautions and 3 solutions, in {lang}"}
      ]
    )

    return completion1.choices[0].message.content

def save_input_image(name: str, result: str) :
    """load binary data

    Args:
        name (str): name of the plant
        result(str): name of the disease

    Returns:
        Any: object stored in the file
    """

    saved = cloudinary.uploader.upload(
        'inputImage.jpg',
        folder="plantCare/",
        width=TARGET_SIZE[f"{name}"][0],
        height=TARGET_SIZE[f"{name}"][0]
    )
    logger.info("Image Saved to Cloudinary")
    logger.info(saved)
    client = MongoClient(os.getenv("MONGO_URI"))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        db = client.PlantCare
        collection = db[f'{name}']
        res = collection.insert_one({
            "disease" : f"{result}",
            "image_url" : saved['secure_url']
        })
        logger.info("Image url Saved MongoDB")
        logger.info(res)
    except Exception as e:
        logger.error(e)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    if(request.json['plant_name'] == 'none') :
        return jsonify("Error: Plant Type Not Selected")
    image = request.json['image']
    name = request.json['plant_name']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict(name)
    print(name, result)
    ans = 0
    try:
        ans = openai_api(plant_name=name, disease=result, lang=request.json['lang'])
        print("gpt Complete")
        save_input_image(name=name, result=result)
    except Exception as e:
        logger.error(e)
    ans = ans.replace("\n", "<br>")
    return jsonify(ans)

if __name__ == "__main__":
    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        secure=True,
    )
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE

