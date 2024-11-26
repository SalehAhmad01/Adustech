from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
from .views import sign_up, confirm_email
app_name = 'users'

urlpatterns = [
    path('users/', views.sign_up, name= 'users-sign-up'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name= 'users-edit'),
    path('email-sent/', views.email_sent, name= 'email_sent'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),  name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),  name='users-logout'),
    path('confirm-email/<str:uidb64>/<str:token>/', confirm_email, name='confirm-email'),
]



