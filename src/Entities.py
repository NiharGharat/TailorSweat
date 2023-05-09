class Exercise:

    def __init__(self, id, name, muscle_grp_hit, calories_10_min, fun_factor, is_compound, how_critical) -> None:
        self.id = id
        self.name = name
        self.muscle_grp_hit = muscle_grp_hit
        self.calories_10_min = calories_10_min
        self.fun_factor = fun_factor
        self.is_compound = is_compound
        self.how_critical = how_critical

class Workout:

    def __init__(self, id, date, exercise_list, workout_fun_factor, duration, calories_burnt, mood, activeness) -> None:
        self.id = id
        self.date = date
        self.exercise_list = exercise_list
        self.workout_fun_factor = workout_fun_factor
        self.duration = duration
        self.calories_burnt = calories_burnt
        self.mood = mood
        self.activeness = activeness