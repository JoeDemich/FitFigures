"""FitFigures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
    path('Home', views.Home, name='home'),
    path('Profile', views.Profile, name='profile'),
    path('Input', views.Input, name='input'),
    path('Figures', views.Figures, name='figures'),
    path('Logs', views.Logs, name='logs'),
    path('Logs/Weight', views.WeightLogs),
    path('Logs/Workouts', views.WorkoutLogs, name='workoutlog'),
    path('viewWeights', views.viewWeights, name='weightlog'),
    path('viewDates', views.viewDates, name='workoutlog'),
    path('Workouts', views.Workouts, name='workouts'),
    path('Workouts/<str:workout_date>', views.viewWorkouts, name='workouts'),
    path('viewWorkouts', views.viewWorkouts, name='workouts'),
    path('Stats', views.Stats, name='stats'),
    path('viewStats', views.viewStats, name='stats'),
    path('Input/Cardio', views.Cardio, name='cardio'),
    path('Input/Strength', views.Strength, name='strength'),
    path('Input/ChangeWeight', views.ChangeWeight, name='weight'),
    path('Input/EntryComplete', views.EntryComplete, name='complete'),
    path('Input/EnterStrength', views.enterStrengthWorkout, name='strength'),
    path('enterStrengthWorkout/', views.enterStrengthWorkout),
    path('enterCardioWorkout/', views.enterCardioWorkout),
    path('enterWeight/', views.enterWeight),
    path('Input/EnterCardio', views.enterCardioWorkout, name='cardio'),
    path('Input/EnterWeight', views.enterWeight, name='weight'),
    path('ChooseExercises', views.ChooseExercise, name='chooseexercise'),
    path('viewExercises', views.viewExercises, name='chooseexercise'),
    path('Graph', views.Graph, name='graph'),
    path('Graph/<str:name>/', views.exerciseGraph, name='graph'),
    path('WeightGraph', views.WeightGraph, name='weightgraph'),
    path('viewWeightGraph', views.viewWeightGraph, name='weightgraph'),
]