from django.shortcuts import render
from django.http import HttpResponse
from .models import PlayerModel
from .forms import PlayerForm


# Create your views here.

def Player_details(r):
    form = PlayerForm()
    if r.method == 'POST':
        form = PlayerForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Submitted")

    return render(r, 'PlayerDetails.html', {'form': form})
