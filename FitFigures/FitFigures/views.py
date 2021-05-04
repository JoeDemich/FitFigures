from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, modelformset_factory, formset_factory
import pyrebase
from .models import WorkoutDetails
from .forms import *

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
    return render(request, "Home.html", {"email": email})


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
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']

        # ADD UID TO USER MODEL FORM

        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "AccountDetails.html") # should be Registration.html
    return render(request, "AccountDetails.html")


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
    return render(request, "Home.html")


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


#def getAccountDetails(request):
  #  if request.method == 'POST':
   #     form = getUserDetails(request.POST)
    #    if form.is_valid():
     #       return HttpResponseRedirect('/Home/')

def getAccountDetails(request):
	user_feet = request.POST.get('user_feet')
	user_inches = request.POST.get('user_inches')
	weight = request.POST.get('weight')
	name = request.POST.get('name')
	# add fitness interests and choose notable stats
	try:
		# Add info to profile
		uid = user['localId']
	except:
		return render(request, "AccountDetails.html")
	return render(request, "Home.html")




def AccountDetails(request):
    return redirect('/AccountDetails/')

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
    for form in formset:
        # Add UID from firebase to form
        userID = request.session['uid']
        form.UID = userID
        if form.is_valid():
            form.save()

    context = {'formset': formset}
    return render(request, 'Strength.html', context)

def enterCardioWorkout(request):
    CardioFormSet = formset_factory(CardioForm, extra = 10)
    formset = CardioFormSet()
    for form in formset:
        # Add UID from firebase to form
        userID = request.session['uid']
        form.UID = userID
        if form.is_valid():
            form.save()

    context = {'formset': formset}
    return render(request, 'Cardio.html', context)

# Needs to also update the weight in the UserDetails table
def enterWeight(request):
    form = WeightForm(request.POST or None)
    # Add UID from firebase to form
    userID = request.session['uid']
    form.UID = userID
    print(userID + "\n")
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'ChangeWeight.html', context)

# Add UID to each form
def getUserInfo(request):
    UserDetForm = UserDetailsForm(request.POST or None)
    UserIntForm = InterestsForm(request.POST or None)
    UserSelStatsForm = SelectedStatsForm(request.POST or None)

    # Set UIDs
    userID = request.session['uid']
    UserDetForm.UID = userID
    UserIntForm.UID = userID
    UserSelStatsForm.UID = userID

    # Set UserDetForm
    UserDetForm.Name = request.POST.get("user_name")
    UserDetForm.DOB = request.POST.get("birthday")
    UserDetForm.Weight = request.POST.get("user_weight")
    UserDetForm.Feet = request.POST.get("user_feet")
    UserDetForm.Inches = request.POST.get("user_inches")

    # Set UserIntForm
    UserIntForm.General_Fitness = request.POST.get("general_fitness")
    UserIntForm.Weight_Loss = request.POST.get("weight_loss")
    UserIntForm.Strength_Training = request.POST.get("strength_training")
    UserIntForm.Endurance = request.POST.get("endurance")
    UserIntForm.Calisthenics = request.POST.get("calisthenics")
    UserIntForm.Athletics = request.POST.get("athletics")
    UserIntForm.Bodybuilding = request.POST.get("bodybuilding")
    UserIntForm.Martial_Arts = request.POST.get("martial_arts")

    # Set UserSelStatsForm
    UserSelStatsForm.Max_Bench_Press = request.POST.get("max_bench_press")
    UserSelStatsForm.Max_Deadlift = request.POST.get("max_deadlift")
    UserSelStatsForm.Max_Squat = request.POST.get("max_squat")
    UserSelStatsForm.Max_Overhead_Press = request.POST.get("max_overhead_press")
    UserSelStatsForm.Max_Pushups = request.POST.get("max_push-ups")
    UserSelStatsForm.Max_Pullups = request.POST.get("max_pull-ups")
    UserSelStatsForm.Max_Dips = request.POST.get("max_dips")
    UserSelStatsForm.Max_Squats = request.POST.get("max_squats")
    UserSelStatsForm.Total_Weight_Used = request.POST.get("total_weight_used")
    UserSelStatsForm.Total_Cardio_Distance = request.POST.get("total_cardio_distance")
    UserSelStatsForm.Total_Cardio_Time = request.POST.get("total_cardio_time")
    UserSelStatsForm.Number_of_Workouts = request.POST.get("number_of_workouts")
    UserSelStatsForm.Average_Workouts_Per_Week = request.POST.get("average_workouts_per_week")
    UserSelStatsForm.Longest_Workout_Streak = request.POST.get("longest_workout_streak")
    UserSelStatsForm.Longest_Rest_Streak = request.POST.get("longest_rest_streak")
    UserSelStatsForm.Total_Weight_Change = request.POST.get("total_weight_change")

















    if UserDetForm.is_valid() and UserIntForm.is_valid() and UserSelStatsForm.is_valid():
        UserDetForm.save()
        UserIntForm.save()
        UserSelStatsForm.save()

    context = {
        'UserDetForm': UserDetForm,
        'UserIntForm': UserIntForm,
        'UserSelStatsForm': UserSelStatsForm
    }

    return render(request, 'Home.html', context)



#def autocomplete(request):
 #   if 'term' in request.GET:
  #      qs = ExerciseName.objects.filter(title_istartswith=request.GET.get('term'))
   #     titles = list()
    #    for exercise in qs:
      #      titles.
     #   return JsonResponse(titles, safe=False)
    #return

