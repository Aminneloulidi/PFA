from django.urls import include, path
from . import views
urlpatterns = [
    path('hello/', views.say_hello)
]

urlpatterns = [
    path('api/mentorat/', include('mentorat.urls')),  # Inclure les URLs de l'application mentorat
    # Ajoutez ici les URLs des autres applications
]