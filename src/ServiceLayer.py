from typing import List
from ServiceLayerDao import DaoLayer
from ServiceLayerRecommender import RecommenderLayer
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
    def save_workouts(self, todays_workout: List[str]):
        status_of_save: bool = self.dao_layer.save_workout(todays_workout)
        return status_of_save

    '''
    Predict next workout
    '''
    def predict_next_workout(self):
        return self.recommender_layer.recommend_next_workout()