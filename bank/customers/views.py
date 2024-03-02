from django.shortcuts import render
from .models import customersDetailsModel
from .forms import customerDetailForm
from django.http import HttpResponse
# Create your views here.

def details_view(r):
    form = customerDetailForm()
    if r.method == 'POST':
        form = customerDetailForm(r.POST)
        if form.is_valid():
            data_dict = form.cleaned_data
            form.save()
            print(data_dict)
            return HttpResponse("Form Submitted")

    return render(r,'customerdetails.html',{'form': form})



