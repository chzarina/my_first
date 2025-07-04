from django.shortcuts import render

from loyiha.models import Loyiha
from group.models import Group
from news.models import Yangilik
# Create your views here.

def loyihalar(request):
    loyiha_list = Loyiha.objects.all()
    group_list = Group.objects.all()
    news_list = Yangilik.objects.all()

    context = {
        'loyiha_list': loyiha_list,
        'group_list': group_list,
        'news_list': news_list
    }
    return render(request, 'home.html', context)
# Create your views here.









