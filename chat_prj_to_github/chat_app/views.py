from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def create_room(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
        except:
            new_room = Room.objects.create(room_name=room)
            new_room.save()
        return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')


def message_view(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Messages.objects.filter(room=get_room)

    context = {
        'messages': get_messages,
        'user': username,
        'room_name': room_name
    }
    return render(request, 'message.html', context)