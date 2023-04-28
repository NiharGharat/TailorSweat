Depth
	- Papers
	- What does a system like this must have?
	- Already present system already have/What functionality do they offer?
	- Cousumption of the app?
--------------------------------
TODO
- Check reddit pre mark workout plans
- Catalogue exercises
- movie reco
- reco sys
- blogs
- reco sys people what use often
- gpt mock skelton
- netflix reco algo
- kaggle 

--
----Questions
1. Goals
	- Are you trying to loose weight?
	- Bulk up - Gain weight
	- Prep for 5k
	- Creation of goals
		- Specific
		- Measurable
		- Attainable
		- Relevant
		- Timely
	- Strength Training - Increase your strength - One rep maxes
2. Keep it simple
	- Simple workout routines
3. You want a workout routine that has at least one exercise for your:
	- Quads (front of your legs).
	- Butt and hamstrings (back of your legs).
	- Chest, shoulders, and triceps: (“push” muscles).
	- Back, biceps, and grip (“pull” muscles).
	- Core (abdominals and lower back).
4. Increase compound exercises.
5. How much time you can spend for the workout.
6. Avoid a muscle group.

----Statements to think
1. I have fun in a exercise and I want to keep repeting that.(Intelligently sense)
2. An exercise which is really crucial, and it has to be done.(Intelligently sense)
3. 5 exercises total, each with 4 “work sets” is a good start.
4. Tailor workout based on users profile and history.

----Ideas
1. Get stronger with each movement each week, and you have yourself a recipe for a great physique.
2. Keep things interesting, avoid hitting plateau.
	#
	If you do bench presses on Monday, go with overhead presses on Wednesday and dips on Friday.
	Squats on Monday? Try lunges on Wednesday and front squats on Friday.
	Do deadlifts every Wednesday, but change up the sets and reps you pick!
	#
3. Analyse which exercise is most boring to the user, and maybe try to spin a variation.
4. Rep range suggestion template, no algo suggestion??
#
- If you’re looking to burn fat while building muscle, keep your number of repetitions per set in the 8-15 range per set.
- If you can do more than 15 reps without much of a challenge, consider increasing the weight or the difficulty of the movement. This is true for things like lunges, bodyweight squats, push-ups, pull-ups, etc.
- Reps in the 1-5 range build super dense muscle and strength (called myofibrillar hypertrophy).
- Reps in the 6-12 range build a somewhat equal amount of muscular strength and muscular size (this is called sarcoplasmic hypertrophy).
- Reps in the 12+ range build muscular endurance.
#

----Types of Variables
1. Categorical
	- Nomial(Name, label without order)
	- Ordinal(order reln, #good, #veryGood, etc.)
2. Numeric
	- Continuous
	- Dicrete

----Assumptions
1. Keep it simple
2. Extensibility
3. App might not suggest you the set range

----Keep in mind
1. Maybe - retrain after like 1 week, or getting 10 days worth of additional data.

----User params
1. Gender
2. Height
3. Age
4. Weight
5. User onboarding workout level

----Metrics for exercise
1. Duration of exercises				- 3min															- numeric(D)
2. Calories burnt of exercise			- #400kcal														- numeric(D)
3. Muscle groups targetted				- #bicep, #tricep, #quads, #hamstrings, #abs, etc				- catagorical(n)
4. isCompound							- #True, #False													- catagorical(o)
5. TagOfMovement						- #Push, #Pull, #FrontLeg, #Core, #Cardio, #BackLeg, #Endurance	- catagorical(n)
6. How essential is that exercise?		- #VeryVeryEssential, #VeryEssential, #Essential, #Okish, #Skippable - cat(o)
7. Are you bored of this exercise?		- #5, #4, #Somewhat, #Yes, #VeryMuchSo					- catagorical(o) 
8. Exercise intensity					- #5, #4, ...											- catagorical(o)
9. Rated Perceived Exertion(RPE)		- #5, #4, ...

----Metrics for workout
1. Duration of workout					- #10min, #30min, #60min, #120min, #150min						- num(D)
2. Calories burnt of workout			- 100kcal, 500kcal, 											- num(D)
3. Muscle groups targetted after wrokout- #bicep, etc.													- cat(n)
4. isCompound included					- #True, etc.													- cat(o)
5. Workout completion					- 
6. Cooldown

----Example of an effective workout
-> Targets front leg, back leg, chest, back, core, etc.
#
Barbell squats: 5 sets of 5 reps.
Barbell Deadlifts: 3 sets of 3 reps.
Push-ups (or dips): 3 sets of 15 reps.
Pull-ups (or Inverted Rows): 3 sets of 8 reps.
Planks: 3 sets, 1-minute hold each.
#

----Things to discuss in the presentation
1. Extensibility of idea
	- Extend to planner of sort - eg for studies
2. Better weight recommendation, progressive loading
3. Day suggestion

----References
[1] https://www.nerdfitness.com/blog/how-to-build-your-own-workout-routine/
[2] https://medium.com/nikeengineering/serving-athletes-with-personalized-workout-recommendations-285491eabc3d