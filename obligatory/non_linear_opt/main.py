import numpy as np
import tensorflow as tf
from keras.layers import Dense
from tensorflow import keras
from keras import layers, Sequential


def main():
    inputs_data = np.array([[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]])
    outputs_data = np.array([0, 1, 1])

    model = Sequential()
    model.add(Dense(2, activation="sigmoid", input_dim=3))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()
    model.compile(optimizer='adam',loss="mean_squared_error",metrics=[keras.metrics.BinaryAccuracy(
    name="binary_accuracy", dtype=None, threshold=0.5)])

    # Train the model for 1 epoch from Numpy data
    batch_size = 3
    print("Fit on NumPy data")
    history = model.fit(inputs_data, outputs_data, batch_size=batch_size, epochs= 2000)
    for layer in model.layers: print(layer.get_weights())


if __name__ == "__main__":
    main()
