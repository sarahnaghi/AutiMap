
from django.urls import path
from . import views

app_name = "centers"

urlpatterns = [
    path("category/", views.category_view, name="category_view"),
    path('centers/', views.centers_view, name="centers_view"),
    path('center_detail/<center_id>/', views.center_detail_view, name="center_detail_view"),
    path('add_center/', views.add_center_view, name="add_center_view"),  
    path('add_center/', views.add_center_view, name="add_center_view"),
    path('center_employee/<center_id>/', views.center_employee_view, name="center_employee_view"), 
    path('add_center/', views.add_center_view, name="add_center_view"),
    path('success/', views.success_view, name='success_view'),

]