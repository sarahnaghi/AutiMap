from django.shortcuts import render,redirect
from centers.models import Center,Review,RequestTour,CenterEmployee
from django.http import HttpRequest,HttpResponse
from django.db.models import Avg
from django.utils.datastructures import MultiValueDictKeyError

def add_center_view(request:HttpRequest):
 if request.user.is_superuser:

    if request.method == "POST":
        center = Center(centerName=request.POST["centerName"],city=request.POST["city"] ,description=request.POST["description"],content=request.POST["content"], location=request.POST["location"], image=request.FILES["image"])
        center.save()

        return redirect("centers:centers_view")

    return render(request, 'centers/add_center.html', {"Center": Center})


def centers_view(request:HttpRequest):

    centers = Center.objects.all()

    return render(request, 'centers/centers.html', {'centers': centers, 'Center':Center ,"category_choices": Center.city_choices })

def center_detail_view(request:HttpRequest, center_id):


    center = Center.objects.get(id=center_id)
    reviews = Review.objects.filter(center=center)
    avg= Review.objects.filter(center=center).aggregate(Avg('rating'))

    employees = CenterEmployee.objects.filter(center=center)

    if request.method == 'POST':
        if request.POST.get('content',False):
            review = Review(center=center, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
            review.save()

        elif request.POST.get("selected_time", False):

            tours = RequestTour(center=center, user=request.user, date=request.POST["date"], times=request.POST["selected_time"])
            tours.save()
        
            return redirect("centers:success_view")



    return render(request, 'centers/center_detail.html', {'center': center, 'reviews': reviews ,'RequestTour':RequestTour,'Review':Review, 'avg':avg ,'employees':employees, 'Employee':CenterEmployee})


def success_view(request:HttpRequest):
    return render(request, 'centers/user_profile.html')


def center_employee_view(request:HttpRequest,center_id):
 center = Center.objects.get(id=center_id)
 
 if request.method == "POST":
         employee = CenterEmployee(center=center, employees_names=request.POST["employees_names"],employee_image=request.FILES["employee_image"])
         employee.save()
         return redirect("centers:center_detail_view",center_id=center.id)

 return render(request,'centers/center_employee.html',{'center': center})


def category_view(request:HttpRequest):
    
    if "Riyadh" in request.GET:
     centers = Center.objects.filter(city='Riyadh')

    elif "Jeddah" in request.GET:
     centers = Center.objects.filter(city='Jeddah')

    elif "Khobar" in request.GET:
     centers = Center.objects.filter(city='Khobar')

    else: 
     centers = Center.objects.filter(city='Mecca')

    return render(request, "centers/centers.html",{'centers':centers})

