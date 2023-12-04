from django.urls import path
from .views import galerija, slikaDetail

app_name = 'slike'

urlpatterns = [
    path('', galerija, name='galerija'),

    path('<int:id>/', slikaDetail, name='slika-detail'),


]