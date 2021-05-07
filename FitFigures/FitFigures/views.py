from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, modelformset_factory, formset_factory
import pyrebase
from .models import WorkoutDetails
from .forms import *
from .models import *
import random
from datetime import date
import datetime
from datetime import date
import time
import json
import matplotlib.pyplot as plt

config = {
    "apiKey": "AIzaSyCN1Bh-NxLYGllp-w51nqTMSsml6WiSFpU",
    "authDomain": "fitfigures-ca304.firebaseapp.com",
    "databaseURL": "https://fitfigures-ca304-default-rtdb.firebaseio.com/",
    "projectId": "fitfigures-ca304",
    "storageBucket": "fitfigures-ca304.appspot.com",
    "messagingSenderId": "10486500769",
    "appId": "1:10486500769:web:f158fff9fd84f194548fe0"
}
# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
currentUID = -1
currentCreds = {'email': 'e',
                'pass': 'p'}

Quotes = [
        "\"Strength does not come from the physical capacity. It comes from an indomitable will.\" – Mahatma Gandhi",\
        "\"Energy & persistence conquer all things.\" – Benjamin Franklin",
        "\"No matter how slow you go, you’re still lapping everybody on the couch.\"   —​Elite Daily",
        "\"It always seems impossible until it’s done.\" —​Nelson Mandela",
        "\"If it doesn’t challenge you it doesn’t change you!\" – Fred Devito",
        "\"We are what we repeatedly do. Excellence then is not an act but a habit.\" —Aristotle",
        "\"The difference between try and triumph is a little umph.\" – Marvin Phillips",
        "\"Motivation is what gets you started. Habit is what keeps you going.\" – Jim Ryin",
        "\"No pain, no gain.\" – Benjamin Franklin",
        "\"Don’t count the days, make the days count.\" —Muhammad Ali",
        "\"A year from now you may wish you had started today.\" – Karen Lamb",
        "\"A healthy body owns a healthy mind.\" – Amit Kalantri"
    ]


def signIn(request):
    return render(request, "Login.html")


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!! Please Check your Data"
        return render(request, "Login.html", {"message": message})


    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    global currentUID
    currentUID = user['localId']
    print("Should be UID: " + currentUID + "\n")

    rand = random.randint(0, len(Quotes) - 1)
    context = {'quote': Quotes[rand],
               "email": email}
    return render(request, "Home.html", context)


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")

# Experiencing a strange error. For some reason
# an unknown exception is being thrown upon
# account registration, so I have to render
# AccountDetails.html in the wrong location
# for the website to function as intended.

def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')

    rand = random.randint(0, len(Quotes) - 1)
    context = {'quote': Quotes[rand],
               "email": email}

    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        user = authe.sign_in_with_email_and_password(email, passs)
        uid = user['localId']

        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "Home.html", context) # should be Registration.html

    return render(request, "Home.html", context)

def reset(request):
    return render(request, "Reset.html")


def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message = "A email to reset password is succesfully sent"
        return render(request, "Reset.html", {"msg": message})
    except:
        message = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg": message})


def Home(request):
    rand = random.randint(0, len(Quotes)-1)
    context = {'quote': Quotes[rand]}
    return render(request, "Home.html", context)


def Profile(request):
    return render(request, "Profile.html")

def Input(request):
    return render(request, "Input.html")

def Figures(request):
    return render(request, "Figures.html")

def Logs(request):
    return render(request, "Logs.html")

def Stats(request):
    return render(request, "Stats.html")

def Cardio(request):
    return render(request, 'Cardio.html')

def Strength(request):
    return render(request, 'Strength.html')

def ChangeWeight(request):
    return render(request, 'ChangeWeight.html')

def EntryComplete(request):
    return render(request, 'EntryComplete.html')

def enterStrengthWorkout(request):
    StrengthFormSet = formset_factory(StrengthForm, extra = 10)
    formset = StrengthFormSet()

    if request.method == 'POST':
        formset = StrengthFormSet(request.POST)
        print(authe.current_user['localId'])
        for form in formset:
            # Add UID from firebase to form
            #form.UID = str(currentUID)
            form.instance.UID = authe.current_user['localId']
            print("UID in strength form: " + str(form.instance.UID) + "\n")
            print(form.errors)
            if form.is_valid():
                if form.instance.Date != None and form.instance.Exercise != None and form.instance.Set != None and form.instance.Reps != None and form.instance.Weight != None:
                    print("FORM IS VALID\n")
                    form.save()
                    return render(request, 'EntryComplete.html')
            else:
                print("Form is not valid\n")
    else:
        print("Not post?\n")
    context = {'formset': formset}
    return render(request, 'Strength.html', context)

def enterCardioWorkout(request):
    CardioFormSet = formset_factory(CardioForm, extra = 10)
    formset = CardioFormSet()

    if request.method == 'POST':
        formset = CardioFormSet(request.POST)
        for form in formset:
            form.instance.UID = authe.current_user['localId']
            print("UID in cardio form: " + str(form.instance.UID) + "\n")
            print(form.errors)
            if form.is_valid():
                if form.instance.Date != None and form.instance.Exercise != None and form.instance.Interval != None and form.instance.Distance != None and form.instance.Time != None:
                    print(form.instance.Time)
                    print("\n")
                    form.save()
                    print("Form is valid\n")
                    return render(request, 'EntryComplete.html')
    else:
        print("Not post?\n")
    context = {'formset': formset}
    return render(request, 'Cardio.html', context)

def enterWeight(request):
    form = WeightForm()
    if request.method == 'POST':
        form = WeightForm(request.POST or None)
        form.instance.UID = authe.current_user['localId']
        if form.is_valid():
                if form.instance.Date != None and form.instance.Weight != None:
                    form.save()
                    return render(request, 'EntryComplete.html')
    context = {'form': form}
    return render(request, 'ChangeWeight.html', context)


def WeightLogs(request):
    return render(request, "WeightLogs.html")

def WorkoutLogs(request):
    return render(request, "WorkoutLogs.html")

def Workouts(request):
    return render(request, "Workouts.html")

def viewWeights(request):
    userUID = authe.current_user['localId']
    userWeights = Weights.objects.filter(UID=userUID).order_by('-Date')
    context = {'userWeights': userWeights}
    return render(request, "WeightLogs.html", context)

def viewDates(request):
    userUID = authe.current_user['localId']
    userWorkouts = WorkoutDetails.objects.filter(UID=userUID).values('Date').order_by('Date')
    dates = []
    for workout in userWorkouts:
        if str(workout['Date']) not in dates:
            dates.append(str(workout['Date']))
    dates.reverse()
    context = {'dates': dates}
    return render(request, "WorkoutLogs.html", context)

def viewWorkouts(request, workout_date):
    userUID = authe.current_user['localId']
    print("Date: " + workout_date)
    userWorkouts = WorkoutDetails.objects.filter(UID=userUID,Date=workout_date).order_by('Exercise', 'Set', 'Interval')#.order_by('Set').order_by('Interval')
    all_details = []
   # print(userWorkouts)

    print("These should show up")
    print(userWorkouts)
    for workout in userWorkouts:
        #print(workout.Exercise)
        if workout.Time != None:
            workout.Time = str(workout.Time)
        print()

        """ 
        all_details.append({
            'Maybe': "Maybe",
            'Exercise': str(workout.Exercise),
            'Set': str(workout.Set),
            'Reps': str(workout.Reps),
            'Weight': str(workout.Weight),
            'Interval': str(workout.Interval),
            'Time': str(workout.Time),
            'Distance': str(workout.Distance)
        })
        all_details.append(workout)
        """
    #print(all_details)
    return render(request, "Workouts.html", {
       'date': str(workout_date),
       'userWorkouts': userWorkouts
    })

def viewStats(request):
    userUID = authe.current_user['localId']
    print("On stats page")

    # Total Weight Change & Current Weight
    userWeights = Weights.objects.filter(UID=userUID).order_by('-Date')
    weights = []
    for weight in userWeights:
        weights.append(weight)
    weightChange = (weights[0].Weight - weights[-1].Weight)
    if weightChange > 0:
        weightChange = "+" + str(weightChange)
    currentWeight = weights[0].Weight


    # Number of Workouts
    userWorkouts = WorkoutDetails.objects.filter(UID=userUID).values('Date').order_by('Date')
    dates = []
    streakDates = []
    for workout in userWorkouts:
        if str(workout['Date']) not in dates:
            dates.append(str(workout['Date']))
            print("THIS ORDER: " + str(workout['Date']))
            streakDates.append(workout['Date'])
    numberofworkouts = len(dates)

    # Workout and Rest Streaks
    count = 0
    currentConsecutive = datetime.timedelta(1)
    longestConsecutive = datetime.timedelta(0)
    currentMissed = datetime.timedelta(0)
    longestMissed = datetime.timedelta(0)
    for Date in streakDates:
        print("Count: " + str(count))
        if count != 0:
            if Date - prevDate == datetime.timedelta(1):
                currentConsecutive = currentConsecutive + datetime.timedelta(1)
                if currentConsecutive > longestConsecutive:
                    longestConsecutive = currentConsecutive
                    print(longestConsecutive)
            else:
                currentMissed = (Date - prevDate)

                if currentMissed > longestMissed and currentMissed != -1:
                    longestMissed = currentMissed
                    longestMissed = longestMissed - datetime.timedelta(days=1)
                    print("Rest Test: " + str(longestMissed.days))
        if count == len(dates):
            today = date.today()
            if (today - Date) > longestMissed:
                longestMissed = today - Date

                print(longestMissed)
        prevDate = Date
        count = count + 1

    # Total Cardio Time and Distance
    cardioWorkouts = WorkoutDetails.objects.filter(UID=userUID).values('Time', 'Distance')
    totalDistance = 0.0
    totalTime = datetime.timedelta(0)
    print(cardioWorkouts)
    for workout in cardioWorkouts:
        if workout['Time'] != None:
            print(workout['Time'])
            time = str(workout['Time'])
            hour = int(time[:2])
            min = int(time[3:5])
            sec = int(time[6:8])
            totalTime = totalTime + datetime.timedelta(seconds=sec, minutes=min, hours=hour)
        if workout['Distance'] != None:
            totalDistance = totalDistance + float(workout['Distance'])

    # Total Weight Used
    strengthWorkouts = WorkoutDetails.objects.filter(UID=userUID).values('Reps', 'Weight')
    totalWeight = 0
    for workout in strengthWorkouts:
        if workout['Weight'] != None:
            totalWeight = totalWeight + (workout['Weight'] * workout['Reps'])

    context = {'weightChange': weightChange,
               'currentWeight': currentWeight,
               'numberofworkouts': numberofworkouts,
               'longestConsecutive': longestConsecutive.days,
               'longestMissed': longestMissed.days,
               'totalDistance': totalDistance,
               'totalWeight': totalWeight,
               'totalTime': totalTime}
    return render(request, "Stats.html", context)