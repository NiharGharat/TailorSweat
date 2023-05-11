import numpy as np
import tensorflow as tf 
from keras import models, layers, losses, regularizers
import pandas as pd
from sklearn.model_selection import train_test_split
from ast import literal_eval

# Loading the dataset
data = pd.read_csv('src/resources/data/new_workout_conc.csv')

d = pd.read_csv('src/resources/data/new_workout_onehot.csv')
numpy_array = data.values
numpy_array.shape
# loading the exercise reference data.
data_reference = pd.read_csv("src/resources/data/exercise_raw.csv", index_col=False)
# To keep a reference of the exercise names.
exercise_data = data_reference.iloc[:, 1].values

# Assuming you have a NumPy array named 'data' for features and 'target' for the target variable
X_train, X_test, y_train, y_test = train_test_split(data, d['excercise_list'].values, test_size=0.2, random_state=42)
#X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))

y_train = np.array([literal_eval(x) for x in y_train], dtype=float)

class RecommenderEngine:

    def __init__(self,) -> None:
        self.model = None
        pass

    def handle_model_creation(self,X_train):
        '''
        Do model creation part
        Create the model, or load from the file
        ''' 
        model = models.Sequential()
        model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.2))
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.2))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.2))
        model.add(layers.Dense(50, activation='sigmoid'))        
        return model

    def train(self, X_train, y_train,X_test):
  
        '''
        A wrapper for training if needed
        '''
        model = self.handle_model_creation(X_train)
        model.compile(loss=losses.mean_squared_error,optimizer='adam')
        history = model.fit(x = X_train, y = y_train, epochs = 10, batch_size = 1, validation_split = 0.2)
        # Predict the probabilities for each class in the output layer
        predictions = model.predict(X_test)
        return predictions

    def predict_routine(self, exercise_data, X_train,y_train, X_test) -> str:
        '''
        A wrapper for predicting if needed
    
        '''
        exercise_names, exercise_counts = np.unique(exercise_data, return_counts=True)
        exercise_dict = {name: count for name, count in zip(exercise_names, exercise_counts)}
        probabilities = self.train(X_train,y_train, X_test)
        #exercise_dict = {name: 0 for name in exercise_data}
        exercise_probabilities = probabilities.flatten()
    
        # Combining the probabilities and the exercise_names
        exercise_prob = dict(zip(exercise_dict, exercise_probabilities))
        # Sorting the the probabilities and returning the top 5
        #top_5 = sorted(exercise_prob, key = exercise_prob.get, reverse = True)[:5]
        top_5 = [exercise for exercise in sorted(exercise_prob, key=exercise_prob.get, reverse=True)
             if exercise_prob[exercise] == 1][:5]

        return top_5
recommeder = RecommenderEngine()
print(recommeder.predict_routine(exercise_data,X_train,y_train,X_test))
