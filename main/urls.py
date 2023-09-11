from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  
    path('', views.home_view, name="home_view"),
    path('how_to_start/', views.how_to_start_view, name="how_to_start_view"),
    path('having_doubts/', views.having_doubts_view, name="having_doubts_view"),
    path('family_journeys/', views.family_journeys_view, name="family_journeys"),
    

]