import tensorflow.lite as tflite
from io import BytesIO
from urllib import request
import numpy as np

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_image(img):
    img = np.array(img, dtype='float32')
    img = np.array([img])
    img = img /255.0
    return img



interpreter = tflite.Interpreter(model_path='bees-wasps.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']

output_index = interpreter.get_output_details()[0]['index']


X = download_image('https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg')
X = prepare_image(X, (150, 150))
X = preprocess_image(X)
interpreter.set_tensor(input_index, X)

interpreter.invoke()
interpreter.get_tensor(output_index)

