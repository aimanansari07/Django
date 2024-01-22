from django.urls import path
from android import views
urlpatterns = [
    
    path('s/',views.samsung),
    path('g/',views.google),
]
