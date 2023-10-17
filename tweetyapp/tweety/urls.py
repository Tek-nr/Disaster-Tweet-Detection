from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

#http://127.0.0.1:8000/

urlpatterns = [
    path("", views.home, name="home"),
    #path("home", views.home),
    path("tyardim/", views.tyardim, name="tyardim"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("kul-bilgiler/", views.user_bilgiler, name="bilgiler"), 
    path("veriSil/<str:pk>/", views.veriSil, name="veriSil"), 
    #path("password/", views.change_pwd, name="password"), 
    #path("password", auth_views.PasswordChangeView.as_view(template_name='registration/change_password.hmtl')), 
]