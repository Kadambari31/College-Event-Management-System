from django.shortcuts import render           # 1) 'render' will return an HTML template as the response
from .models import Event                     # 2) Use your Event model to fetch data
from django.http import HttpResponse

def event_list(request):                      # 3) The function Django will call for "/events/"
    events = Event.objects.all().order_by('date')  # 4) Query all events ordered by date
    return render(request,                    # 5) Return an HTML page
                  'events/event_list.html',   # 6) Path to the template file
                  {'events': events})         # 7) Data sent to the template (a context dictionary)

def index(request):
    return HttpResponse("Hello from Students app")