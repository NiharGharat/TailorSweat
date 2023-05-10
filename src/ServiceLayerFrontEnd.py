import datetime
from typing import List
from ServiceLayer import ServiceLayer
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
    def _prompt_user(self) -> List[str]:
        now = datetime.now()

        exercise_list: str = input('Enter exercises of a list separated by space ')
        now_date: str = now.strftime('%Y%m%d')
        fun_factor_workout: int = int(input('Enter workout fun factor \t\t int \t\t 0 to 5, with 0 being least fun'))
        duration: float = float(input('Enter your duration of workout \t\t float'))
        calories_burnt: float = input('Enter calories burnt today \t\t float')
        mood: int = int(input('Enter your mood today \t\t int \t\t 0 being unhappy'))
        activeness = int(input('Enter how active you feel \t\t int \t\t 0 being least active'))
        print("\n")
        # Eg - bicep_curl tricep_extension leg_press
        '''
        self.date: str = date
        # bicep_curl tricep_extension
        self.exercise_list: str = exercise_list
        self.workout_fun_factor: int = workout_fun_factor
        self.duration: float = duration
        self.calories_burnt: float = calories_burnt
        self.mood: int = mood
        self.activeness: int = activeness
        '''

        return exercise_list
    
    def _main_procedure(self) -> str:
        # 1. Get todays workout
        todays_workout: str = self._prompt_user()
        if len(todays_workout.strip(" ")) == 0:
            print("No exercises detected")
            raise Exception("No workouts were entered")
        else:
            print("Workouts captured")
            print('Todays workout was: ', todays_workout)
        
        # 2. Push the workouts to todays workout session
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