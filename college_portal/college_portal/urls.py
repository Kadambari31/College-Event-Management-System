"""
URL configuration for college_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin       # 1) Admin site import
from django.urls import path, include  # 2) 'include' lets you plug in other URL files (like the app's urls)

urlpatterns = [
    path('admin/', admin.site.urls),          # 3) Route "/admin/" to Django’s admin
    path('events/', include('events.urls')),         # 4) At the site root (''), load patterns from events/urls.py
    path('students/', include('students.urls')),
    path('faculty/', include('faculty.urls')),
    path('dashboard/', include('dashboard.urls')), #admin dashboard
]


