from django.shortcuts import render
from .models import Galerija

# Create your views here.
def galerija(request):

    slike = Galerija.objects.all()

    context = {
        'slike': slike
    }
    return render(request, 'slike.html', context)
