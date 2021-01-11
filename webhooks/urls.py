from django.urls import path
from . import views
#from webhooks.views import RegisterUser, ListUser
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('example/', views.example),
    #path('login/', views.Login, name='login'),
    #path('register/', views.Register, name='register'),
    #path('listado_usuario/', login_required(ListUser.as_view()),
    #     name='listar_usuarios'),
    #path('registrar_usuario/', login_required(RegisterUser()),
    #     name='registrar_usuario'),

    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),

]

