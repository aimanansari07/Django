from django.http import path
from marvel import views
urlpatterns = [
    path("ironman/",views.ironman),
    path("spiderman/",views.spiderman),
]
