import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers


def main():
    inputs_data = np.array([[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]])
    outputs_data = np.array([0, 1, 1])
    print("ASDA")
    inputs = keras.Input(shape=3)
    x = layers.Dense(2, activation="relu")(inputs)
    outputs = layers.Dense(1, activation="sigmoid")(x)
    model = keras.Model(inputs, outputs)
    model.summary()



if __name__ == "__main__":
    main()
