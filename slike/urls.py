from django.urls import path
from .views import galerija

app_name = 'slike'

urlpatterns = [
    path('', galerija, name='slike'),


]