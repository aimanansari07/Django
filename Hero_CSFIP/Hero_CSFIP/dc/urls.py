from django.http import path
from dc import views
urlpatterns = [
    path('batman/',views.batman),
    path('superman/',views.superman),
]
