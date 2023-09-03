from django.urls import path
from .views import (homeview,
                    loginview,
                    logoutuser,
                    welcomeview,
                    registerview)

app_name = "base"
urlpatterns = [
    path('home', homeview, name='home'),
    path('login/', loginview, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register/', registerview, name='register'),
    path('account/', welcomeview, name='account')

]
