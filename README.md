# TailorSweat

# Exercise Naming convention
1. All small letters
2. Underscore seperated
3. Singluar - leg_press, tricep_extension

# Assumptions
1. Legs are not split in quads, calves, hamstrings, etc. - rather its just legs

# Instructions
1. Run the CodeRunner.ipynb
2. ProjectReport is in notes folder.

# Libraries
1. As given in requirements.txt

# Context
Hello, so this application is intended to predict the users next workout(give suggestion) based on his/her prefernces, profile setting, and various other parameters(Knowledge base rules) defined by us. The metric of this system what percent does the system correctly predicts the workout which the user does. 

The central idea is, get various metrics, aggregate various metrics, calculate intelligently based on user profile, past history, get a weighted sum per workout of each user. 
Eg - exercise importance += 
does_user_want_to_bulk * 0.37
+ does_focus_muscle_group == todays_trained_muscle * 0.55
+ age_bracket and user_in_young_adult_age_bracket * 0.55
...

This is per_workout_dervied data is derived from:
1. User_Profile
2. Exercise_Derived
3. Exercise
4. Workouts

This per workout metric data is passed to the neural network, and it gives a padded weightage of 50 possible exercise(we have 50 exercises in master list). This is filtered on a threshold, do a nonzero on the result, and get the names of the indexes. Those are your next workout suggestion.
Store this as prediction.
Exercise_Derived is again intelligently calculated based on weighted aggregation.(Eg - impact factor of exercise, exhaustion factor, etc.)

# Questions, suggestions?
1. Happy to hear - Raise an issues, connect with us.