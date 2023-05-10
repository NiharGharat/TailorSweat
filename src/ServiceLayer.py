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
    New workout came in, save it
    Also, do recomputation of the weights on the exercise and workout calc tables
    '''
    def save_workouts(self, todays_workout: Entities.Workout) -> bool:
        status_of_save: bool = self.dao_layer.save_workout(todays_workout)
        # A new workout was just in, need to run recomputations on exercise and workout calc file
        # todays_workout is not needed further as we have already 
        status_of_recomputation = self.do_recomputation()
        return status_of_save and status_of_recomputation

    '''
    The recomputations
    '''
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