from typing import List
from ServiceLayerDao import DaoLayer
from ServiceLayerRecommender import RecommenderLayer
import Entities
'''
A class responsible for:
1. 
'''
class ServiceLayer:

    def __init__(self) -> None:
        self.dao_layer = DaoLayer()
        self.recommender_layer = RecommenderLayer()

    '''
    Save a workout given by the top user
    '''
    def save_workouts(self, todays_workout: Entities.Workout) -> bool:
        status_of_save: bool = self.dao_layer.save_workout(todays_workout)
        # A new workout was just in, need to run recomputations on exercise and workout calc file
        status_of_recomputation = self.do_recomputation()
        return status_of_save and status_of_recomputation

    def do_recomputation(self):
        # Do recomputations on exercise_calc
        self.recommender_layer.recompute_exercises_weights()
        # Do recomputations on workout_calc
        self.recommender_layer.recompute_workout_weights()
        return None

    '''
    Predict next workout
    '''
    def predict_next_workout(self):
        # Predict/Train from the model
        return self.recommender_layer.recommend_next_workout()