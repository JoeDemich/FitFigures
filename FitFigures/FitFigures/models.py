from django.db import models
from django.utils import timezone

class Users(models.Model):
    UID = models.CharField(max_length=1028)

    def __str__(self):
        return self.UID.name

class Weights(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateTimeField(default=timezone.now)
    Weight = models.IntegerField()

class UserDetails(models.Model):
    UID = models.CharField(max_length=1028)
    Name = models.CharField(max_length=32)
    DOB = models.DateField()
    Weight = models.IntegerField()
    Feet = models.IntegerField()
    Inches = models.IntegerField()

class SelectedStats(models.Model):
    UID = models.CharField(max_length=1028)
    Max_Bench_Press = models.BooleanField()
    Max_Deadlift = models.BooleanField()
    Max_Squat = models.BooleanField()
    Max_Overhead_Press = models.BooleanField()
    Max_Pushups = models.BooleanField()
    Max_Pullups = models.BooleanField()
    Max_Dips = models.BooleanField()
    Max_Squats = models.BooleanField()
    Total_Weight_Used = models.BooleanField()
    Total_Cardio_Distance = models.BooleanField()
    Total_Cardio_Time = models.BooleanField()
    Number_of_Workouts = models.BooleanField()
    Average_Workouts_Per_Week = models.BooleanField()
    Longest_Workout_Streak = models.BooleanField()
    Longest_Rest_Streak = models.BooleanField()
    Total_Weight_Change = models.BooleanField()

class Stats(models.Model):
    UID = models.CharField(max_length=1028)
    Max_Bench_Press = models.IntegerField()
    Max_Deadlift = models.IntegerField()
    Max_Squat = models.IntegerField()
    Max_Overhead_Press = models.IntegerField()
    Max_Pushups = models.IntegerField()
    Max_Pullups = models.IntegerField()
    Max_Dips = models.IntegerField()
    Max_Squats = models.IntegerField()
    Total_Weight_Used = models.IntegerField()
    Total_Cardio_Distance = models.DecimalField(decimal_places=4, max_digits=16)
    Total_Cardio_Time = models.TimeField()
    Number_of_Workouts = models.IntegerField()
    Average_Workouts_Per_Week = models.DecimalField(decimal_places=4, max_digits=5)
    Longest_Workout_Streak = models.IntegerField()
    Longest_Rest_Streak = models.IntegerField()
    Total_Weight_Change = models.DecimalField(decimal_places=2, max_digits=5)

class Interests(models.Model):
    UID = models.CharField(max_length=1028)
    General_Fitness = models.BooleanField()
    Weight_Loss = models.BooleanField()
    Strength_Training = models.BooleanField()
    Endurance = models.BooleanField()
    Calisthenics = models.BooleanField()
    Athletics = models.BooleanField()
    Bodybuilding = models.BooleanField()
    Martial_Arts = models.BooleanField()


class WorkoutDetails(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateTimeField(default=timezone.now)
    Exercise = models.CharField(max_length=67)
    Set = models.IntegerField()
    Interval = models.IntegerField()
    Reps = models.IntegerField()
    Weight = models.IntegerField()
    Distance = models.DecimalField(decimal_places=2, max_digits=5)
    Time = models.TimeField()

    def __str__(self):
        return self.Exercise


class Workouts(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateField()
    Workout = models.ForeignKey(WorkoutDetails, on_delete=models.CASCADE)

class ExercisesList(models.Model):
    Name = models.CharField(max_length=67)

