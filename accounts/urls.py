from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
    path('specialist_information/<user_id>/', views.specialist_information_view, name="specialist_information_view"),
    path('specialist_register/', views.specialist_register_view, name="specialist_register_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('user_profile/', views.user_profile_view, name="user_profile_view"),
    path('admin_profile/', views.admin_profile_view, name="admin_profile_view"),
    path('login_success/', views.login_success_view, name="login_success_view"),

    path('specialist_profile/', views.specialist_profile_view, name="specialist_profile_view"),

]


