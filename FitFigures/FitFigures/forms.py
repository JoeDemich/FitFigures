
from django import forms
from django.forms import ModelForm, DateInput
from .models import *


#class getUserDetails(forms.Form):
 #   weight = forms.CharField(label = 'user_weight', max_length = 3)
  #  feet = forms.IntegerField(label = 'user_feet', max_value = 7, min_value = 3)
   # inches = forms.IntegerField(label = 'user_inches', max_value = 11, min_value = 0)

class CreateUserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('UID', 'Username')

class StrengthForm(ModelForm):
    class Meta:
        model = WorkoutDetails
        fields = ('Date', 'Exercise', 'Set', 'Reps', 'Weight')

        #widget = {'Date': forms.SelectDateWidget,
         #         'Set': forms.Select}
        def __init__(self):
            self.fields['Date'].widget.attrs.update({'type': 'date'})

class CardioForm(ModelForm):
    class Meta:
        model = WorkoutDetails
        fields = ('Date', 'Exercise', 'Interval', 'Time', 'Distance')

        #widget = {'Date': forms.SelectDateWidget,
         #         'Set': forms.Select}
        def __init__(self):
            self.fields['Date'].widget.attrs.update({'type': 'date'})

class WeightForm(ModelForm):
    class Meta:
        model = Weights
        fields = ('Date', 'Weight')

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ('Name', 'DOB', 'Weight', 'Feet', 'Inches')

class InterestsForm(ModelForm):
    class Meta:
        model = Interests
        fields = ('General_Fitness', 'Weight_Loss', 'Strength_Training', 'Endurance',
                  'Calisthenics', 'Athletics', 'Bodybuilding', 'Martial_Arts')

class SelectedStatsForm(ModelForm):
    class Meta:
        model = SelectedStats
        fields = ('Max_Bench_Press', 'Max_Deadlift', 'Max_Squat', 'Max_Overhead_Press',
                  'Max_Pushups', 'Max_Pullups', 'Max_Dips', 'Max_Squats', 'Total_Weight_Used',
                  'Total_Cardio_Distance', 'Total_Cardio_Time', 'Number_of_Workouts',
                  'Average_Workouts_Per_Week', 'Longest_Workout_Streak', 'Longest_Rest_Streak',
                  'Total_Weight_Change')
   # date = forms.DateField()
    #exercise = forms.CharField(max_length=67)
    #set_interval = forms.IntegerField()
    #reps = forms.IntegerField()
    #weight = forms.CharField(label='user_weight', max_length=3)