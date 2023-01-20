from django.urls import path, include
from . import views 
from config import urls
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('grades/', views.list, name='list'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('grades/add', views.addgrade, name='addgrade'),
    path('status/add', views.statusadd, name='ST'),
    path('status/', views.statusredirect, name='add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)