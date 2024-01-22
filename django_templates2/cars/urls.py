from django.urls import path
from cars import views
urlpatterns = [
    path('b/',views.bugatti),
    path('l/',views.lambo),
]
