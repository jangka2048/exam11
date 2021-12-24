from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
    path('find_username/', views.find_username, name = 'find_username'),
]
