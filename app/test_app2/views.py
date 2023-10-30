from django.shortcuts import render
from django.http import HttpResponse


from .models import Event, Registration


def user_list(request):
    users = Registration.objects.all()
    return render(request, 'test_app2/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = Registration.objects.get(id=user_id)
    return render(request, 'test_app2/ user_detail.html', {'user': user})


def event_registration(request):
    if request.method == 'POSt':
        attendee_name = request.POST['attendee_name']
        attendee_email = request.POST['attendee_email']
        event_id = request.POST['event_id']
        event = Event.objects.get(id=event_id)
        registration = Registration.objets.create(event=event, attendee_name=attendee_name, attendee_email=attendee_email)
        return HttpResponse('Регстрация успешно завершена ')
    else:
        events = Event.objects.filter(registration_open=True)
        return render(request, 'test_app2', {events: events})