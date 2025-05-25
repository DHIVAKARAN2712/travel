from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_visit, name='submit_visit'),
    path('add/', views.add_place, name='add_place'),
    path('my-submissions/', views.my_submissions, name='my_submissions'),
    path('most-wanted/', views.most_wanted_places, name='most_wanted'),

]
