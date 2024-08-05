# django-fitness-app

## MVP
- User Authentication
- Profile management
- Workout Tracking
- Goal Setting

## User Stories:
1. Allow the new users to sign-up for a account to track the fitness activities
2. Allow users to login and out of the account so that user can access their data securely
3. Allow new users to add new workouts and details so that they can track their progress
4. Allow users to view the list of their past workouts and provide them ability to edit or delete their workouts
5. Allow users to set the fitness goals and see the progress towards their goal
6. Allow users to edit and delete their fitness goals

## ERD:

## User
id, name, email, phne, password, weight, height, gender, level, goal, 

## logs
id, date, total_sets, reps_forEach_Set, total_duration, total_distance, ForeignKey to User

## goals
id, target_weight, target_height, target_date, ForeignKey to User
 
