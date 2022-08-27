from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='lectures-home'),
    path('lectures/', views.showAllLectures, name='lectures-showAllLectures'),
    path('lectures/<int:lecID>/', views.showOneLecture, name='lectures-showOneLecture'),
    path('upload/', views.upload, name="lectures-upload")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)