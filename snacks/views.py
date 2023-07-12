from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = "data"

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack
# Create your views here.