from django.db import models
from django.contrib.auth.models import User
from accounts .models import SpecialistProfile



# Create your models here.


class AppointmentBooking(models.Model):

    date_choices = (('17-09-2023', '17-09-2023'), ('18-09-2023', '19-09-2023'), ('19-09-2023', '19-09-2023'), ('20-09-2023', '20-09-2023'), ('21-09-2023', '21-09-2023'),('22-09-2023', '22-09-2023') )
    times_choices =(('8:00 am','8:00 am'),('9:00 am','9:00 am'),('10:00 am','10:00 am'),('11:00 am','11:00 am'),('12:00 pm','12:00 pm'),('4:00 pm','4:00 pm'),('6:00 pm','6:00 pm'),('7:00 pm','7:00 pm'),('8:00 pm','8:00 pm'))

    specialist = models.ForeignKey(SpecialistProfile,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=128,choices=date_choices)
    times = models.CharField(max_length=128,choices=times_choices)
    Appointment_description = models.TextField()
    zoom_url=models.URLField(blank=True)
    zoom_password=models.CharField(max_length=128)











    

    
    


    

 
    


    