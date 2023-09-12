from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User



class Center(models.Model):
    city_choices =(('Riyadh','Riyadh'),('Jeddah','Jeddah'),('Khobar','Khobar'),('Mecca','Mecca'))

    centerName = models.CharField(max_length=200)
    description=models.TextField()
    content = models.TextField()
    city=models.CharField(max_length=128, choices= city_choices )
    image = models.ImageField(upload_to="images/")
    location = models.URLField(max_length=1024)


    def get_average(self):
        return Review.objects.filter(center=self).aggregate(Avg('rating'))["rating__avg"]


    def str(self):
        return self.centerName
    


class RequestTour(models.Model):
    time_choices =(('8:00','8:00 am'),('9:00','9:00 am'),('10:00','10:00 am'),('11:00','11:00 am'))

    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    times = models.CharField(max_length=128, choices= time_choices)


class CenterEmployee(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    employees_names = models.CharField(max_length=200)
    employee_image=models.ImageField(upload_to='images/')



class Review(models.Model):
    rating_choices = ((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars"), )
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices= rating_choices)
    content = models.TextField()



  