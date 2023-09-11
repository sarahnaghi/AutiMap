from django.contrib import admin
from .models import Center,Review,RequestTour,CenterEmployee

# Register your models here.


class CenterAdmin(admin.ModelAdmin):

    list_display = ("centerName", "description", "content", "city","image","location")


class ReviewAdmin(admin.ModelAdmin):

 list_display = ("rating","content","center")

class RequestTourAdmin(admin.ModelAdmin):
 list_display = ("times","date")



class CenterEmployeeAdmin(admin.ModelAdmin):
  list_display = ("employee_image","employees_names")


admin.site.register(Center, CenterAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(RequestTour, RequestTourAdmin)
admin.site.register(CenterEmployee, CenterEmployeeAdmin)




