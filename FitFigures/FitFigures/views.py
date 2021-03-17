# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_message(request):
    # This will return Hello User!
    # string as HttpResponse
    return HttpResponse("Hello User!")

###########################################################
###########################################################
###########################################################



config={
	"apiKey": "AIzaSyCN1Bh-NxLYGllp-w51nqTMSsml6WiSFpU",
	"authDomain": "fitfigures-ca304.firebaseapp.com",
	"databaseURL": "https://fitfigures-ca304-default-rtdb.firebaseio.com/",
	"projectId": "fitfigures-ca304",
	"storageBucket": "fitfigures-ca304.appspot.com",
	"messagingSenderId": "10486500769",
	"appId": "1:10486500769:web:f158fff9fd84f194548fe0"
}
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):
	return render(request,"Login.html")
def home(request):
	return render(request,"Home.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		# if there is no error then signin the user with given email and password
		user=authe.sign_in_with_email_and_password(email,pasw)
	except:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	return render(request,"Home.html",{"email":email})

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"Login.html")

def signUp(request):
	return render(request,"Registration.html")

def postsignUp(request):
	email = request.POST.get('email')
	passs = request.POST.get('pass')
	name = request.POST.get('name')
	try:
		# creating a user with the given email and password
		user=authe.create_user_with_email_and_password(email,passs)
		uid = user['localId']
		idtoken = request.session['uid']
		print(uid)
	except:
		return render(request, "Registration.html")
	return render(request,"Login.html")

def reset(request):
	return render(request, "Reset.html")

def postReset(request):
	email = request.POST.get('email')
	try:
		authe.send_password_reset_email(email)
		message = "A email to reset password is succesfully sent"
		return render(request, "Reset.html", {"msg":message})
	except:
		message = "Something went wrong, Please check the email you provided is registered or not"
		return render(request, "Reset.html", {"msg":message})
