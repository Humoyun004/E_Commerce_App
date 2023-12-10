from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Goods

# Create your views here.


class Home(ListView):
    model = Goods
    paginate_by = 4
    template_name = 'products/index.html'
    context_object_name = 'goods'
    # login_url = '/login'

class Message(DetailView):
    model = Goods
    template_name = 'products/message.html'
    context_object_name = 'goods'


