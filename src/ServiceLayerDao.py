from Entities import Workout
import pandas as pd
import csv
import Constants

class DaoLayer:

    def __init__(self) -> None:
        pass

    def save_workout(self, todays_workout: Workout):
        # Save workouts to csv file
        self._append_workout_to_csv(todays_workout, Constants.DAILY_WORKOUT_DATA_PATH)
        return True
    
    def _append_workout_to_csv(self, workout: Workout, filename: str):
        # Open the CSV file in append mode
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)

            # Write the workout data as a row in the CSV file
            writer.writerow([
                workout.id,
                workout.date.isoformat(),
                ','.join(workout.exercise_list),
                workout.workout_fun_factor,
                workout.duration,
                workout.calories_burnt,
                workout.mood,
                workout.activeness
            ])

        return True