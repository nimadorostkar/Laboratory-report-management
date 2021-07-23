from django.urls import path, re_path
from app import views


app_name='app'



urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
