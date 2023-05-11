import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
from keras import models, layers, losses, regularizers

class RecommenderEngine:

    def __init__(self) -> None:
        self.model = None
        pass

    def handle_model_creation(self):
        '''
        Do model creation part
        Create the model, or load from the file
        ''' 
        pass

    def train(self, train, test):
        '''
        A wrapper for training if needed
        '''
        # Model Architecture
        # Creating the Sequential object
        model = models.Sequential()
        # Adding the Conv2D layer to the model with fileters = 8, kernel size = (3, 3), strides = (1,1), padding='same', activation='relu' and a L2 Regularization of 0.0001.
        model.add(layers.Conv2D(filters = 8, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu', input_shape = train.shape[1:], kernel_regularizer = regularizers.l2(0.0001)))
        # Adding the Conv2D layer to the model with filters = 16, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu' and a L2 Regularization of 0.0001.
        model.add(layers.Conv2D(filters = 16, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu', kernel_regularizer = regularizers.l2(0.0001)))
        # Adding the Max Pooling layer with a pool size of (2,2), strides = (2,2).
        model.add(layers.MaxPooling2D(pool_size = (2,2), strides = (2,2)))
        # Adding the Conv2D layer to the model with filters = 32, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu' and a L2 Regularization of 0.0001.
        model.add(layers.Conv2D(filters = 32, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu', kernel_regularizer = regularizers.l2(0.0001)))
        # Adding the Conv2D layer to the model with filters = 64, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu' and a L2 Regularization of 0.0001.
        model.add(layers.Conv2D(filters = 64, kernel_size = (3,3), strides = (1,1), padding='same', activation='relu', kernel_regularizer = regularizers.l2(0.0001)))
        # Adding the Max Pooling layer with a pool size of (2,2), strides = (2,2).
        model.add(layers.MaxPooling2D(pool_size = (2,2), strides = (2,2)))
        # Adding a flatten layer to the model.
        model.add(layers.Flatten())
        # Adding a dense layer to the model with units = 512, activation='relu' and L2 Regularization of 0.0001.
        model.add(layers.Dense(units = 512, activation='relu', kernel_regularizer = regularizers.l2(0.0001)))
        # Adding a dense layer to the model with units = 10, activation='linear' and L2 Regularization of 0.0001.
        model.add(layers.Dense(units = 50, activation='linear', kernel_regularizer = regularizers.l2(0.0001)))
        # Adding a softmax layer to the output layer.
        model.add(layers.Activation('softmax'))     
        # Compiling the Neural Network model with adam optimizer, loss = losses.categorical_crossentropy and metrics as 'accuracy'.
        model.compile(optimizer = 'adam', loss = losses.categorical_crossentropy, metrics = ['accuracy'])

        # Training the model with a validation split of 0.2 and storing the model in the history object.
        history = model.fit(x = train, y = train, epochs = 10, batch_size = 1, validation_split = 0.2)
        # Predict the probabilities for each class in the output layer
        predictions = model.predict(test)

        predicted_labels = np.argmax(predictions, axis=1)


        return predictions_labels

    def predict(self) -> str:
        '''
        A wrapper for predicting if needed
        '''
        pass