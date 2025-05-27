from django.urls import path
from . import views
from .views import SignupView, ChangePasswordView

urlpatterns = [
    path('user/', views.user_info), 
    path('<str:user_name>/profile/', views.user_profile), 
    path('<int:user_pk>/follow/', views.user_follow),
    path('signup/', SignupView.as_view(), name='signup'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
