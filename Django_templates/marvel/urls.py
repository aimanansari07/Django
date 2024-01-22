from django.urls import path
from marvel import views
urlpatterns = [
    path('i/',views.ironman),
    path('sp/',views.spiderman),
]
