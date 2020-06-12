from django.shortcuts import render
from .models import Photo

# Create your views here.
def photo(request):
    photos = Photo.objects
    return render(request, 'photo.html', {'photos':photos})