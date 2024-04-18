from django.shortcuts import render
from doctors.models import DoctorsData, Specialties

def home(request):
    if request.method == "GET":
        doctors_filter = request.GET.get('doctor_name')
        specialties_filter = request.GET.get('specialties')
        doctors = DoctorsData.objects.all()
        
        if doctors_filter:
            doctors = doctors.filter(name__icontains=doctors_filter)
        if specialties_filter:
            doctors = doctors.filter(specialties_id=specialties_filter)
        
        specialties = Specialties.objects.all()
        return render(request, 'home.html', {'doctors': doctors, 'specialties': specialties})
    
