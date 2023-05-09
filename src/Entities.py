from typing import List
import datetime

class Exercise:

    def __init__(self, id: int, name: str, muscle_grp_hit: List[str], calories_10_min: float, fun_factor: int, is_compound: bool, how_critical: int) -> None:
        self.id: int = id
        self.name: str = name
        self.muscle_grp_hit: List[str] = muscle_grp_hit
        self.calories_10_min: float = calories_10_min
        self.fun_factor: int = fun_factor
        self.is_compound: bool = is_compound
        self.how_critical: int = how_critical

class Workout:

    def __init__(self, id: int, date: str, exercise_list: List[str], workout_fun_factor: int, duration: float, calories_burnt: float, mood: int, activeness: int) -> None:
        self.id: int = id
        self.date: str = date
        self.exercise_list: List[str] = exercise_list
        self.workout_fun_factor: int = workout_fun_factor
        self.duration: float = duration
        self.calories_burnt: float = calories_burnt
        self.mood: int = mood
        self.activeness: int = activeness

    @staticmethod
    def convert_workouts_to_entity(todays_workout: List[str], workout_fun_factor: int, duration: float, calories_burnt: float, mood: int, activeness: int) -> Workout:
        now = datetime.now()
        # 20230509002049
        now_id = int(now.strftime('%Y%m%d%H%M%S'))
        now_date = now.strftime('%Y%m%d')
        workout = Workout(now_id, now_date, todays_workout, workout_fun_factor, duration, calories_burnt, mood, activeness)
        return workout