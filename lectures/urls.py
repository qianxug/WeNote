from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lectures-home'),
    path('lectures/', views.showAllLectures, name='lectures-showAllLectures'),
    path('lectures/<int:lecID>/', views.showOneLecture, name='lectures-showOneLecture')
]