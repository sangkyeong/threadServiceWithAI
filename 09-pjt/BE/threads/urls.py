from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.thread_list),
    path('<int:book_pk>/create/', views.thread_create),
    path('<int:thread_pk>/update/', views.thread_update),
    path('<int:thread_pk>/detail/', views.thread_detail),
    path('<int:thread_pk>/delete/', views.thread_delete),
    path('<int:thread_pk>/comment/create/', views.create_comment),
    path('comment/<int:comment_pk>/delete/', views.delete_comment),
]
