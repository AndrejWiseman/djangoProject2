from django.shortcuts import render
from .models import Galerija

# Create your views here.
def galerija(request):

    context = {

    }
    return render(request, 'slike.html', context)
