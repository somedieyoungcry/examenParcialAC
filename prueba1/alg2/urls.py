from django.urls import path
from . import views
urlpatterns = [
    path('alg2/', views.algBayIng, name='inicio'),
]