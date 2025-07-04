
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('loyiha.urls')),
    path('' , include('group.urls')),
    path('' , include('news.urls'))
    
] 

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

