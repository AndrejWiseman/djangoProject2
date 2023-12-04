from django.shortcuts import render, get_object_or_404
from .models import Galerija

# Create your views here.
def galerija(request):

    slike = Galerija.objects.all()

    context = {
        'slike': slike
    }
    return render(request, 'slike.html', context)


def slikaDetail(request, id):

    slika = get_object_or_404(Galerija, id=id)

    context = {
        'slika': slika
    }
    return render(request, 'slika_detail.html', context)
