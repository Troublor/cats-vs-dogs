import tensorflow as tf
import numpy as np
from os import path
import os

# force to use CPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class Classifier:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)
        self.class_names = ['cat', 'dog']
        self.img_height = 180
        self.img_width = 180

    def predict(self, image_path: str) -> [str, float]:
        img = tf.keras.preprocessing.image.load_img(
            image_path, target_size=(self.img_height, self.img_width)
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        # print(
        #     "This image most likely belongs to {} with a {:.2f} percent confidence."
        #         .format(self.class_names[np.argmax(score)], 100 * np.max(score))
        # )
        return self.class_names[np.argmax(score)], np.max(score)


if __name__ == '__main__':
    classifier = Classifier(path.join('model', 'classifier.h5'))
    print(classifier.predict('/home/troublor/workspace/catsVSdogs/data/small_set/dog/24.jpg'))
