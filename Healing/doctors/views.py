from django.shortcuts import render, redirect
from .models import Specialties, DoctorsData, is_doctor
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants


def doctors_registration(request):
    

    if is_doctor(request.user):
        messages.add_message(request, constants.WARNING, "Você já é registrado como médico na nossa plataforma.")
        return redirect('/doctors/myschedule/')
    
    
    if request.method == "GET":
        specialties = Specialties.objects.all()
        return render(request, 'doctors_registration.html', {'specialties': specialties})
    elif request.method == "POST":
        crm = request.POST.get('crm')
        name = request.POST.get('name')
        acode = request.POST.get('acode')
        street = request.POST.get('street')
        region = request.POST.get('region')
        number = request.POST.get('number')
        medical_registration = request.FILES.get('medical_registration')
        registration = request.FILES.get('registration')
        profile_picture = request.FILES.get('profile_picture')
        specialties = request.POST.get('specialties')
        description = request.POST.get('description')
        service_price = request.POST.get('service_price')
        
        doctors_data = DoctorsData(
            
            crm=crm,
            name=name,
            street=street,
            region=region,
            number=number,
            acode=acode,
            medical_registration=medical_registration,
            registration=registration,
            profile_picture=profile_picture,
            specialties_id=specialties,
            description=description,
            service_price=service_price,
            user=request.user,
        )
        
        doctors_data.save()
        
        messages.add_message(request,constants.SUCCESS, "Seu cadastro médico foi realizado com sucesso!")
        return redirect('/doctors/myschedule/')
