
from django.urls import path          # 1) Import the 'path' helper to define URL patterns
from . import views                   # 2) Import your views.py from the same folder (the dot means "this app")

urlpatterns = [                       # 3) A Python list that will hold all URL rules for this app
    path('',                   # 4) The URL part after your site domain. Here it’s "/events/"
         views.event_list,            # 5) The function to run when someone visits "/events/" (defined in views.py)
         name='event_list'),          # 6) A short name for this URL so you can refer to it in templates: {% url 'event_list' %}
]