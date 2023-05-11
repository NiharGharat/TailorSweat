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

    def recompute_exercises_weights(self):
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
        exercise_table = self.dao_layer.read_table(Constants.TABLE_EXERCISE)
        workout_table = self.dao_layer.read_table(Constants.TABLE_WORKOUT)
        exercise_dervied = self.dao_layer.read_table(Constants.TABLE_EXERCISE_DERIVED)
        workout_dervied = self.dao_layer.read_table(Constants.TABLE_WORKOUT_DERIVED)
        user = self.dao_layer.read_table(Constants.TABLE_USER)
        exercise_metadata = self.dao_layer.read_table(Constants.TABLE_EXERCISE)

        # Knowledge base part for exercise table
        self.knowledge_base_exercise(exercise_table, workout_table, exercise_dervied, user, exercise_metadata)

        # Knowledge base part for workout table
        self.knowledge_base_workout()
        # Save the exercise and workouts to the file again on overwrite
        pass

    def knowledge_base_exercise(self, exercise_table, workout_table, exercise_dervied, user, exercise_metadata):
        # If exercise_derived table has NaN in these columns, replace them with 0
        # Columns - "exercise_importance	exercise_cost	exercise_recurrance_factor_per_cycle	exercise_rpe	exercise_overall_fun_factor	exercise_exhaustion_factor	missed_in_cycle_count"
        columns_to_replace_nan_to_zero = ["exercise_importance", "exercise_cost", "exercise_recurrance_factor_per_cycle", "exercise_rpe", "exercise_overall_fun_factor", "exercise_exhaustion_factor", "missed_in_cycle_count"]


        # Rule 1: If "bicep" in exercise[muscles_targeted] and user has "bicep" in user[focused_muscle_group]
        # then increase old_val + 0.37
        muscle_group = "bicep"
        weight = 0.37
        exercise_table.apply(lambda row: RecommenderLayer.update_weights_muscle_group_matching(user, exercise_dervied, row, Constants.USER_NAME, muscle_group, weight), axis = 1)
        
        # Rule 1:
        '''
        Make bigger muscles stronger first
        '''
        mapping = {"bicep":0.25, "chest": 0.55, "core": 0.20, "leg": 0.55, "back": 0.55, "shoulder": 0.45, "tricep": 0.25}
        for key, value in mapping.items():
            exercise_table.apply(lambda row: RecommenderLayer.update_weights_muscle_group_matching(user, exercise_dervied, row, Constants.USER_NAME, key, value), axis = 1)
        
        

        # Rule 2: If 



    def recompute_workout_weights(self):
        '''
        Same compared to workout
        '''
        pass

    def recommend_next_workout(self, exercise_dervied, workout_dervied) -> str:
        predicted_workout: str = ""
        # 1. Pull params from dao layers from exercise_derived_table, workout_derived, user table
        

        # 2. Wrangle params with necessary
        # Create the data as we want as train, test
        train, test = self.wrangle_data(exercise_dervied, workout_dervied, user, exercise_metadata)

        # 3. Create network if not created
        self.recommender_engine.handle_model_creation()

        # 4. Train if needed
        self.recommender_engine.train(train, test)

        # 4. Predict using the model
        predicted_workout = self.recommender_engine.predict(train)
        return predicted_workout
    
    #### KnowledgeBase
    @staticmethod
    def update_weights_muscle_group_matching(df_user, df_derived_ex, row, user_name, muscle_group, weightage):
        if muscle_group in df_user[df_user['name'] == user_name]['focused_muscle_group'].item().split():
            # Update all rows who have bicep in muscle_targeted
            if muscle_group in row['muscles_targeted'].split():
                id = row['id']
                old_val = df_derived_ex[df_derived_ex['id'] == id]['exercise_importance'].item()
                df_derived_ex.loc[df_derived_ex['id'] == id, 'exercise_importance'] = old_val + weightage