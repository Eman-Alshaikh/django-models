from django.shortcuts import render
from django.views.generic import ListView,DeleteView 
from .models import Snack
# Create your views here.

class SnacksListView(ListView):
    template_name='snacks_list.html'
    model=Snack


 

class SnacksDetailView(DeleteView):
    template_name='snack_detail.html'
    model=Snack


    