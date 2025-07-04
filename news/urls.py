from django.urls import path
from .views import lesprojet

urlpatterns = [
    path('' , lesprojet, name = 'lesprojet' )
]