import datetime
from typing import List
from ServiceLayer import ServiceLayer
import Utility
import Entities

'''
Responsible for:
1. Display prompt to user
2. Accept the input
3. Push to ServiceLayer
4. Accept output from service and display to user
'''

class FrontEndService:

    def __init__(self, safety: True) -> None:
        self.service_layer: ServiceLayer = ServiceLayer()
        self.safety: bool = safety

    '''
    Ops to perform
    1. 
    '''
    def _prompt_user_and_get_todays_workout(self) -> Entities.Workout:
        now = datetime.now()

        id = Utility.get_a_unique_id()
        exercise_list: str = input('Enter exercises of a list separated by space ')
        date: str = Utility.get_todays_date_in_str()
        workout_fun_factor: int = int(input('Enter workout fun factor \t\t int \t\t 0 to 5, with 0 being least fun'))
        duration: float = float(input('Enter your duration of workout \t\t float'))
        calories_burnt: float = input('Enter calories burnt today \t\t float')
        mood: int = int(input('Enter your mood today \t\t int \t\t 0 being unhappy'))
        activeness = int(input('Enter how active you feel \t\t int \t\t 0 being least active'))
        
        todays_workout = Entities.Workout(id, date, exercise_list, workout_fun_factor, duration, calories_burnt, mood, activeness)
        print("\n")
        # Eg - bicep_curl tricep_extension leg_press
        return todays_workout
    
    def _main_procedure(self) -> str:
        # 1. Get todays workout
        todays_workout: Entities.Workout = self._prompt_user_and_get_todays_workout()
        if len(todays_workout.exercise_list.split(" ")) == 0:
            print("No exercises detected")
            raise Exception("No workouts were entered")
        else:
            print("Workouts captured")
            print('Todays workout was: ', todays_workout)
        
        # 2. Push the workouts to todays workout session and ensure safety in pushing
        # Push to date - manipulate data only when safety is off
        if not self.safety:
            self.service_layer.save_workouts(todays_workout)
            print("Saved the workouts")
        else:
            print("Not saving current workout in sheet")
        
        # 3. Predict the next workout
        next_workout: str = self.service_layer.predict_next_workout()
        return next_workout
    
    def main_procedure(self):
        exit = True
        while exit:
            next_workouts: List[str] = self._main_procedure()
            print("Next workout is", next_workouts)
            exit = input("Keep doing ops? Y/N").lower().strip() == 'y'

        return True