from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cardshower, name='cardshower'),
    path('upload/', views.Upload.as_view(), name='upload_url'),
]
