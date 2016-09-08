from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Event
from .forms import EventForm
import json

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {"events":events})

def goals(request):
    events = Event.objects.all()
    events=[ob.events_json() for ob in events]
    return HttpResponse(json.dumps(events), content_type="application/json")

def add(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/')
    else:
        form = EventForm()
    return render(request, 'add.html', {"form":form})

def goal_edit(request, pk):
    goal = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance = goal)
        if form.is_valid():
            goal=form.save()
            return redirect('/', pk=goal.pk)
    else:
        form = EventForm(instance=goal)
    return render(request, 'add.html', {"form":form})

def goal_delete(request, pk):
    goal = get_object_or_404(Event, pk=pk)
    goal.delete()
    return redirect("/")
