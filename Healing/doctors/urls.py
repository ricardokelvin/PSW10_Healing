from django.urls import path
from . import views

urlpatterns = [
    path('doctors_registration/', views.doctors_registration, name="doctors_registration"),
    path('schedule_opener/', views.schedule_opener, name="schedule_opener"),
]
