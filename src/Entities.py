from typing import List
import datetime
import Utility
import Entities

# The entity which is stored in the csv file
class Exercise:

    def __init__(self, id: int, name: str, muscles_targeted: str, calories_10_min: float, fun_factor: int, is_compound: int, how_critical: int, exercise_type: str) -> None:
        self.id: int = id
        # Name of the exercise
        self.name: str = name
        # Core, ...
        self.exercise_type: str = exercise_type
        # bicep tricep legs -> Space sepearted muscle groups
        self.muscles_targeted: str = muscles_targeted
        # A single number
        self.calories_10_min: float = calories_10_min
        # User given 0 - 5
        self.fun_factor: int = fun_factor
        # Number, 0: false, 1: true
        self.is_compound: int = is_compound
        # Number 0 - 5
        self.how_critical: int = how_critical

# The entity which is stored in the csv file
class Workout:

    def __init__(self, id: int, date: str, exercise_list: str, workout_fun_factor: int, duration: float, calories_burnt: float, mood: int, activeness: int, rpe_list: str) -> None:
        self.id: int = id
        # str yyyyddmm
        self.date: str = date
        # bicep_curl tricep_extension
        self.exercise_list: str = exercise_list
        # The overall workout fun factor 0 - 10
        self.workout_fun_factor: int = workout_fun_factor
        # Overall duration of workout - float
        self.duration: float = duration
        # Number
        self.calories_burnt: float = calories_burnt
        # Mood 0, 1, 2 - Unhappy to Happy
        self.mood: int = mood
        # Activeness: 0, 1, 2 - Unactive to veryActive
        self.activeness: int = activeness
        # 0 10 7 1 2
        # Same order in which user did the exercises
        self.rpe_list: str = rpe_list

    @staticmethod
    def prompt_to_create_workout(now) -> Entities.Workout:
        id = Utility.get_a_unique_id(now)
        # Eg - bicep_curl tricep_extension leg_press
        exercise_list: str = input('Enter exercises of a list separated by space ')
        date: str = Utility.get_todays_date_in_str(now)
        workout_fun_factor: int = int(input('Enter workout fun factor \t\t int \t\t 0 to 5, with 0 being least fun'))
        duration: float = float(input('Enter your duration of workout \t\t float'))
        calories_burnt: float = input('Enter calories burnt today \t\t float')
        mood: int = int(input('Enter your mood today \t\t int \t\t 0 being unhappy'))
        activeness = int(input('Enter how active you feel \t\t int \t\t 0 being least active'))
        rpe_list: str = input('Enter rpe in int per exercise seperated by space')
        # Validation and cleanup of the data entered by the user
        # TODO
        # Lower case every execrise

        todays_workout = Entities.Workout(id, date, exercise_list, workout_fun_factor, duration, calories_burnt, mood, activeness, rpe_list)
        return todays_workout

# A class that has the metrics derived from todays workout
class Exercise_Derived:

    def __init__(self, id, name, exercise_importance, exercise_cost, exercise_recurrance_factor_per_cycle, exercise_rpe, exercise_overall_fun_factor, exercise_exhaustion_factor, missed_in_cycle_count) -> None:
        self.id: int = id
        self.name: str = name
        self.exercise_importance: int = exercise_importance
        self.exercise_cost: int = exercise_cost
        self.exercise_recurrance_factor_per_cycle: int = exercise_recurrance_factor_per_cycle
        self.exercise_rpe: int = exercise_rpe
        self.exercise_overall_fun_factor: int = exercise_overall_fun_factor
        self.exercise_exhaustion_factor: int = exercise_exhaustion_factor
        self.missed_in_cycle_count: int = missed_in_cycle_count

class Workout_Derived:

    def __init__(self, suggested_wo_completion_percentage, wo_imp, wo_cost, wo_muscles_targetted, wo_rpe, wo_overall_cals) -> None:
        self.suggested_wo_completion_percentage: float = suggested_wo_completion_percentage
        self.wo_imp: int = wo_imp
        self.wo_cost: int = wo_cost
        self.wo_muscles_targetted: str = wo_muscles_targetted
        self.wo_rpe: int = wo_rpe
        self.wo_overall_cals: float = wo_overall_cals

class User:

    def __init__(self, id, name, gender, fitness_level, focused_muscle_group, age, goal, weight) -> None:
        self.id: id = id
        self.name = name
        self.gender = gender
        self.fitness_level = fitness_level
        self.focused_muscle_group = focused_muscle_group
        self.age = age
        self.goal = goal
        self.weight = weight