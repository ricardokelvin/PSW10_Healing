from django.db import models
from django.contrib.auth.models import User


def is_doctor(user):
    return DoctorsData.objects.filter(user=user).exists()

class Specialties(models.Model):
    specialty = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.specialty

class DoctorsData(models.Model):
    crm = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    street = models.CharField(max_length=50)
    region = models.CharField(max_length=25)
    number = models.IntegerField()
    acode = models.CharField(max_length=11)
    registration = models.ImageField(upload_to='registration')
    medical_registration = models.ImageField(upload_to='medical_registration')
    profile_picture = models.ImageField(upload_to='profile_picture')
    description = models.TextField()
    service_price = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    specialty = models.ForeignKey(Specialties, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.username

class ScheduleOpenings(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    appointment_date = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.date)
