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
from FitFigures.views import hello_message
from FitFigures.views import signIn
from FitFigures.views import postsignIn
from FitFigures.views import signUp
from FitFigures.views import logout
from FitFigures.views import postsignUp
from FitFigures.views import reset
from FitFigures.views import postReset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_message),
    path('', signIn),
    path('postsignIn/', postsignIn),
    path('signUp/', signUp, name="signup"),
    path('logout/', logout, name="log"),
    path('postsignUp/', postsignUp),
    path('reset/', reset),
    path('postReset/', postReset),

]
