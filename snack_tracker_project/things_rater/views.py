from django.shortcuts import render
from django.views.generic import ListView
from .models import Thing


# Create your views here.
class ThingsListView(ListView):
    template_name="things_list.html"
    model=Thing
    



