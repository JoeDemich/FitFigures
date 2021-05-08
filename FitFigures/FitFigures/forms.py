
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
