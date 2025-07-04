from django.shortcuts import render



from .models import Yangilik
# Create your views here.

def lesprojet(request):
    yangiliklar = Yangilik.objects.all()
    return render(request, 'home.html', {'yangiliklar': yangiliklar})
# Create your views here.