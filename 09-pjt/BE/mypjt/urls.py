"""
URL configuration for mypjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('threads/', include('threads.urls')),
    path('accounts/', include('accounts.urls')), # 웹페이지/커스텀 API
    path('api/accounts/', include('dj_rest_auth.urls')), # API 전용
    path('api/accounts/', include('dj_rest_auth.registration.urls')), # 외부 인증 패키지
    path('api/books/', include('books.urls')), #  Book 앱 API 경로
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
