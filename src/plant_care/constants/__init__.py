from pathlib import Path
from box import ConfigBox

TARGET_SIZE = ConfigBox({
    'potato' : (256, 256),
    'tomato' : (224, 224)
})

CONFIG_FILE_PATH = Path("config/config.json")
PARAM_FILE_PATH = Path("config/param.json")

CLASSES = ConfigBox({
    'potato' : ['Early blight', 'Late blight', 'healthy'],
    'tomato' : ['Bacterial spot',
                'Early blight',
                'Late blight',
                'Leaf Mold',
                'Septoria leaf spot',
                'Spider mites Two-spotted spider mite',
                'Target Spot',
                'Tomato Yellow Leaf Curl Virus', 
                'Tomato mosaic virus',
                'healthy',
                ]
})