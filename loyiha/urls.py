from django.urls import path
from .views import loyihalar

urlpatterns = [
    path('' , loyihalar, name = 'loyihalar' )
]