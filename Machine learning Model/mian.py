import tensorflow.keras
from PIL import Image,ImageOps
import numpy as np

np.set_printoptions(suppress=True)

model=tensorflow.keras.models.load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# image = Image.open('k10.jpg')
image = Image.open('p10.jpg')

size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

image_array = np.asarray(image)
image.show()
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

prediction = model.predict(data)
print(prediction)

labels=['Kiwi','PineApple']
i=np.argmax(prediction[0],axis=0)
print(f'It is a {labels[i]}')
