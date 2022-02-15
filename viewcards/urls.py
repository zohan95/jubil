from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainmenu, name='mainmenu'),
    path('upload/', views.Upload.as_view(), name='upload_url'),
    path('viewid/<str:course>/<str:category>', views.ViewById.as_view(), name='view_id_url'),
    path('show_theory/<int:pk>', views.ShowTheory.as_view(), name='show_theory_url')
]
