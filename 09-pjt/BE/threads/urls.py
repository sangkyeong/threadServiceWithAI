from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.thread_list),
    path('<int:book_pk>/create', views.thread_create),
]
