import Constants
import Utility
import Entities
from RecommenderEngine import RecommenderEngine
from ServiceLayerDao import DaoLayer


class RecommenderLayer:

    def __init__(self) -> None:
        self.model = None
        self.dao_layer = DaoLayer()
        self.recommender_engine = RecommenderEngine()
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
        exercise_dervied = self.dao_layer.read_table(Constants.TABLE_EXERCISE_DERIVED)
        workout_dervied = self.dao_layer.read_table(Constants.TABLE_WORKOUT_DERIVED)
        user = self.dao_layer.read_table(Constants.TABLE_USER)
        exercise_metadata = self.dao_layer.read_talle(Constants.TABLE_EXERCISE)

        # 2. Wrangle params with necessary
        # Create the data as we want as train, test
        train, test = self.wrangle_data(exercise_dervied, workout_dervied, user, exercise_metadata)

        # 3. Create network if not created
        self.recommender_engine.handle_model_creation()

        # 4. Train if needed
        self.recommender_engine.train(train, test)

        # 4. Predict using the model
        predicted_workout = self.recommender_engine.predict()
        return predicted_workout