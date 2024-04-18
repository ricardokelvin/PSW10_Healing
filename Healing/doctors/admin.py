from django.contrib import admin
from .models import Specialties, DoctorsData, ScheduleOpenings

admin.site.register(Specialties)
admin.site.register(DoctorsData)
admin.site.register(ScheduleOpenings)