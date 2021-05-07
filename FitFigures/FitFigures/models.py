from django.db import models
from django.utils import timezone


class Users(models.Model):
    UID = models.CharField(max_length=1028)
    Username = models.CharField(max_length=32)

    def __str__(self):
        return self.Username

class Weights(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateField(blank=True)
    Weight = models.IntegerField(blank=True)

    def __str__(self):
        return self.UID[:5] + " Weights"

class UserDetails(models.Model):
    UID = models.CharField(max_length=1028)
    Name = models.CharField(max_length=32, blank=True)
    DOB = models.DateField(blank=True)
    Weight = models.IntegerField(blank=True)
    Feet = models.IntegerField(blank=True)
    Inches = models.IntegerField(blank=True)

    def __str__(self):
        return self.UID[:5] + " User Details"

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

    def __str__(self):
        return self.UID[:5] + " Selected Stats"

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

    def __str__(self):
        return self.UID[:5] + " Stats"

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

    def __str__(self):
        return self.UID[:5] + " Interests"


class WorkoutDetails(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateField()
    Exercise = models.CharField(max_length=67)
    Set = models.IntegerField(blank=True)
    Interval = models.IntegerField(blank=True)
    Reps = models.IntegerField(blank=True)
    Weight = models.IntegerField(blank=True)
    Distance = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    Time = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.UID[:5] + ": " + self.Exercise


class Workouts(models.Model):
    UID = models.CharField(max_length=1028)
    Date = models.DateField()
   # Workout = models.ForeignKey(WorkoutDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.UID[:5] + " Workout"

class ExercisesList(models.Model):
    Name = models.CharField(max_length=67)

