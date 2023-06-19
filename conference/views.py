from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
conferences = [
    {
        "id": 1,
        "name": "GOA Festival",
        "date": "2023-08-01",
        "city": "Kigali",
        "attendees": 1000,
    },
    {
        "id": 2,
        "name": "Python Hackathon",
        "date": "2023-10-01",
        "city": "Abuja",
        "attendees": 340,
    },
    {
        "id": 3,
        "name": "Django Conference",
        "date": "2024-08-01",
        "city": "Goma",
        "attendees": 14000,
    },
    {
        "id": 4,
        "name": "Youth Connekt",
        "date": "2023-07-01",
        "city": "Addis Ababa",
        "attendees": 13000,
    },
    {
        "id": 5,
        "name": "Transform Africa Summit",
        "date": "2025-08-01",
        "city": "Kigali",
        "attendees": 765,
    }
]

def conference_details(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_details.html', {'conference': conference})

def home(request):
    return render(request, 'index.html', {'conferences': conferences})

def update_page(request, conference_id: int):
    conference = list(filter(lambda c: c['id'] == conference_id, conferences))[0]
    return render(request, 'conference_update.html', {'conference': conference})