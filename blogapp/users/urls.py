from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [
    path('users/', views.sign_up, name= 'users-sign-up'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name= 'users-edit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),  name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),  name='users-logout'),


]
