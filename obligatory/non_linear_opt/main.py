import sys

import numpy as np
import tensorflow as tf
from keras.layers import Dense
from tensorflow import keras
from keras import layers, Sequential


def main():
    if len(sys.argv) != 4:
        print("Invalid usage: main.py <method> <epochs> <learning_rate>")
        quit(1)

    inputs_data = np.array([[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]])
    outputs_data = np.array([0, 1, 1])

    model = Sequential()
    model.add(Dense(2, activation="sigmoid", input_dim=3))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()

    optimizer = keras.optimizers.SGD(learning_rate=sys.argv[3])

    if sys.argv[1] == "SGD":
        optimizer = keras.optimizers.SGD(learning_rate=int(sys.argv[3]))
    elif sys.argv[1] == "ADAM":
        optimizer = keras.optimizers.Adam(learning_rate=int(sys.argv[3]))

    model.compile(optimizer=optimizer, loss="mean_squared_error", metrics=[keras.metrics.BinaryAccuracy(
        name="binary_accuracy", dtype=None, threshold=0.5)])

    batch_size = 3
    history = model.fit(inputs_data, outputs_data, batch_size=batch_size, epochs=int(sys.argv[2]))
    for layer in model.layers: print(layer.get_weights())


if __name__ == "__main__":
    main()
