import Constants
import Utility
import Entities
import ServiceLayer

class RecommenderLayer:

    def __init__(self) -> None:
        self.model = None
        self.service_layer = ServiceLayer()
        self.model = Utility.load_model(Constants.MODEL_PATH)

    def recompute_exercises_weights(self, todays_workout: Entities.Workout):
        # Here, we need to recompute the weights from the exercise data(in exercise_recomp)

        '''
        Algo-
        1. Read the exercises table
        2. Read the workouts table
        3. Read the exercise_derived table
        4. Read the workout_derived table
        5. Read the user table
        6. Compute the new weighs based on recommenderLayer knowledge base
        7. Push the new once to exercise_recalc, and workout_recalc
        '''
        pass

    def recompute_workout_weights(self):
        '''
        Same compared to workout
        '''
        pass

    def recommend_next_workout(self) -> str:
        predicted_workout: str = ""
        # 1. Pull params from dao layers from exercise_derived_table, workout_derived, user table

        # 2. Wrangle params with necessary 

        # 3. Create network if not created
        # Do model part
        # Create the model, or load from the file

        # 4. Predict using the model
        return predicted_workout