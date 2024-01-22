from django.urls import path
from apple import views
urlpatterns = [
    
    path('i/',views.iphone),
    path('m/',views.mac),
]
