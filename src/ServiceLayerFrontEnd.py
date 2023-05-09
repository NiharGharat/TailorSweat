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
        input_string: str = input('Enter exercises of a list separated by space ')
        print("\n")
        return input_string.split()
    
    def _main_procedure(self) -> List[str]:
        # 1. Get todays workout
        todays_workout: List[str] = self._prompt_user()
        if len(todays_workout) == 0:
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
        next_workout: List[str] = self.service_layer.predict_next_workout()
        return next_workout
    
    def main_procedure(self):
        exit = True
        while exit:
            next_workouts: List[str] = self._main_procedure()
            print("Next workout is", next_workouts)
            exit = input("Keep doing ops? Y/N").lower().strip() == 'y'

        return True