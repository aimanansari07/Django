from django.urls import path
from bikes import views
urlpatterns = [
    path('h/',views.hayabusa),
    path('n/',views.ninja),
]
