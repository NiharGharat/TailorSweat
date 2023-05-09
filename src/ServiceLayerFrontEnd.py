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
        self.service_layer = ServiceLayer()
        self.safety = safety


    '''
    Ops to perform
    1. 
    '''
    def propmt_user(self):
        todays_workout = []
        input_string = input('Enter exercises of a list separated by space ')
        print("\n")
        todays_workout = input_string.split()
        return todays_workout
    
    def main_procedure(self):
        # 1. Get todays workout
        todays_workout = self.propmt_user()
        if len(todays_workout) == 0:
            print("No exercises detected")
            raise Exception("No workouts were entered")
        else:
            print("Workouts captured")
            print('Todays workout was: ', todays_workout)
        
        # Push the workouts to todays workout session
        if self.safety:
            

        


