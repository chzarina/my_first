from django.shortcuts import render
from .models import Group
# Create your views here.

def groups(request):
    yangiliklar = Group.objects.all()
    return render(request, 'home.html', {'yangiliklar': yangiliklar})












