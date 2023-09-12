from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('add/digital/', views.add_game_apps_view, name="add_game_apps_view"),
    path('all/digital/', views.all_games_view, name="all_games_view"),
    path('add/toys/', views.add_toy_view, name="add_toy_view"),
    path('all/toys/', views.all_toys_view, name="all_toys_view"),

 path('update/<game_id>/', views.digital_game_update_view, name="digital_game_update_view"),
    path('delete/<game_id>/', views.digital_game_delete_view, name="digital_game_delete_view"),
    path('update/toy/<toy_id>/', views.toy_update_view, name="toy_update_view"),
    path('delete/toy/<toy_id>/', views.toy_delete_view, name="toy_delete_view"),

]