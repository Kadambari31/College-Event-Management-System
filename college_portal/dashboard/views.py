from django.shortcuts import render
from students.models import Student
from faculty.models import Faculty
from events.models import Event
from django.http import HttpResponse

def admin_dashboard(request):
    students_count = Student.objects.count()
    faculty_count = Faculty.objects.count()
    events_count = Event.objects.count()

    return render(request, "dashboard/admin_dashboard.html", {
        "students_count": students_count,
        "faculty_count": faculty_count,
        "events_count": events_count,
    })

def index(request):
    return HttpResponse("Hello from Students app")