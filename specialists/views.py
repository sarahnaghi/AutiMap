from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from . models import User,AppointmentBooking
from accounts .models import SpecialistProfile
from .zoom import create_meeting




def all_specialist_view(request:HttpRequest):
    specialists = SpecialistProfile.objects.all()

    return render(request, "specialists/all_specialist.html",{'specialists':specialists})


def detail_specialist_view(request:HttpRequest,specialist_id):
    specialist = SpecialistProfile.objects.get(user__id=specialist_id)
    
    return render(request, 'specialists/detail_specialist.html',{'specialist':specialist})


def appointment_booking_view (request:HttpRequest,specialist_id):
    specialist = SpecialistProfile.objects.get(user__id=specialist_id)
    
    if request.method == 'POST':
        if request.POST.get('select_times',False):
            new_appointment_booking = AppointmentBooking(user=request.user, specialist=specialist,date=request.POST['date'],times=request.POST['select_times'],Appointment_description=request.POST['Appointment_description'])
            new_appointment_booking.save()

            meeting_url = create_meeting("reservation with specilaist", "60", new_appointment_booking.date , "09:00:00")
            join_url = meeting_url["meeting_url"]
            password=meeting_url["password"]
            new_appointment_booking.zoom_password = password
            new_appointment_booking.zoom_url = join_url
            new_appointment_booking.save()

            return redirect('accounts:user_profile_view')
        
    return render(request, "specialists/appointment_booking.html", {"specialist": specialist, "AppointmentBooking":AppointmentBooking })
    
   


def appointment_success_view(request:HttpRequest):
    return render(request, 'specialists/appointment.html')





 










 

