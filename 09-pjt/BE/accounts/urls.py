from django.urls import path
from . import views
from .views import SignupView

urlpatterns = [
    path('user/', views.user_info), 
    path('signup/', SignupView.as_view(), name='signup'),
]
