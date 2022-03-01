from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='mainPage'),
    path('search/', views.search_images, name='searchPage'), 
    path('location/<location>/', views.view_by_location, name='locationPage'), 
    path('category/<category>/', views.view_by_category, name='categoryPage'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
