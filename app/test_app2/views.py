from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, RegistrationForm



def user_list(request):
    users = RegistrationForm.objects.all()
    return render(request, 'test_app2/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = RegistrationForm.objects.get(id=user_id)
    return render(request, 'test_app2/ user_detail.html', {'user': user})


def event_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            attendee_name = form.cleaned_data['attendee_name']
            attendee_email = form.cleaned_data['attendee_email']
            event = form.cleaned_data['event']
            registration = RegistrationForm.objects.create(event=event, attendee_name=attendee_name, attendee_email=attendee_email)
            return HttpResponse('Регистрация успешно завершена!')
    else:
        form = RegistrationForm()
        events = Item.objects.filter(registration_open=True)
        return render(request, 'test_app2/event_registration.html', {'form': form, 'events': events})