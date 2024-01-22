from django.urls import path
from dc import views
urlpatterns = [
    path('s/',views.superman),
    path('b/',views.batman),
]
