
from django.contrib import admin
from .models import AppointmentBooking



class AppointmentBookingAdmin(admin.ModelAdmin):
    list_display = ("specialist", 'date','times' , 'Appointment_description')



admin.site.register(AppointmentBooking,AppointmentBookingAdmin,)

