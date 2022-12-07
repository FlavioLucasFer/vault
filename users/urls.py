from django.urls import path
from django.contrib.auth import views
urlpatterns = [
    
    path('sign-in/', views.LoginView.as_view(
        template_name='users/sign-in.html'
    ), name='sign-in'),

    path('sign-out/', views.LogoutView.as_view(), name='sign-out'),

]