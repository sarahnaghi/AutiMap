

from django.urls import path
from . import views

app_name = "specialists"

urlpatterns = [
    path('appointment_success/', views.appointment_success_view,name='appointment_success_view'),
    path('all_specialist/', views.all_specialist_view,name='all_specialist_view'),
    path('detail_specialist/<specialist_id>/',views.detail_specialist_view,name='detail_specialist_view'),  
    path('appointment_booking/<specialist_id>/',views.appointment_booking_view,name='appointment_booking_view')

]