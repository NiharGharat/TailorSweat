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
        # Validation: Working
        columns_to_replace_nan_to_zero = ["exercise_importance", "exercise_cost", "exercise_recurrance_factor_per_cycle", "exercise_rpe", "exercise_overall_fun_factor", "exercise_exhaustion_factor", "missed_in_cycle_count"]
        for i in columns_to_replace_nan_to_zero:
            exercise_dervied[i].fillna(0, inplace=True)

        # Rule 1: Working
        '''
        Make bigger muscles stronger first
        '''
        mapping = {"bicep":0.25, "chest": 0.55, "core": 0.20, "leg": 0.55, "back": 0.55, "shoulder": 0.45, "tricep": 0.25}
        for key, value in mapping.items():
            exercise_table.apply(lambda row: RecommenderLayer.update_weights_muscle_group_matching(exercise_dervied, row, key, value), axis = 1)
        
        # Rule 2: Working
        '''
        If Age in bracket 18 - 30 -> Improve asthetic muscles -> bicep and tricep and shoulder
        '''
        age_lower = 18
        age_higher = 40
        age_user = int(user[user['name'] == Constants.USER_NAME]['age'].item())
        if age_lower <= age_user and age_user <= age_higher:
            weight_to_improve = 0.55
            mapping = {"bicep":0.25, "core": 0.25, "shoulder": 0.25, "tricep": 0.25}
            for key, value in mapping.items():
                exercise_table.apply(lambda row: RecommenderLayer.update_weights_muscle_group_matching(exercise_dervied, row, key, value), axis = 1)

        # Rule 3: Working
        '''
        Boost muscle group which the user is focusing
        '''
        muscle_group_which_user_is_focusing = user[user['name'] == Constants.USER_NAME]['focused_muscle_group'].item().split()
        for i in muscle_group_which_user_is_focusing:
            weight_to_improve = 0.55
            exercise_table.apply(lambda row: RecommenderLayer.update_weights_muscle_group_matching(exercise_dervied, row, i, weight_to_improve), axis = 1)

        # Rule 4:
        '''
        Boost the exercises which have more fun factor
        '''
        
        # Rule 5: Increase the cost of exercises which have high calories burnt

        # Rule 6: If goal is strength, increase the cost of exercises which are cardio by little
        if user[user['name'] == Constants.USER_NAME]['goal'].item() == "strength":
            type_of_musc_to_penalise = "cardio"
            weight_cost = -0.25
            exercise_table.apply(lambda row: RecommenderLayer.increase_cost_of_type(exercise_dervied, row, type_of_musc_to_penalise, weight_cost), axis = 1)
        # Rule 7: If goal is cardio, increase the cost of exercises which are strength by little

        # Rule 8: If exercise is compound, then boost its importance

        # Rule 9: If exercise is critical, boost its importance

        # Rule 10: If fun factor < 2, but critical is less than 3, then increase the cost



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
    def update_weights_muscle_group_matching(df_derived_ex, row, muscle_group, weightage):
        # Update all rows who have bicep in muscle_targeted
        if muscle_group in row['muscles_targeted'].split():
            id = row['id']
            old_val = df_derived_ex[df_derived_ex['id'] == id]['exercise_importance'].item()
            df_derived_ex.loc[df_derived_ex['id'] == id, 'exercise_importance'] = old_val + weightage

    @staticmethod
    def increase_cost_of_type(exercise_dervied, row, type_of_musc_to_penalise, weight_cost):
        if type_of_musc_to_penalise in row['muscles_targeted'].split():
            id = row['id']
            old_val = exercise_dervied[exercise_dervied['id'] == id]['exercise_cost'].item()
            df_derived_ex.loc[df_derived_ex['id'] == id, 'exercise_cost'] = old_val + weightage