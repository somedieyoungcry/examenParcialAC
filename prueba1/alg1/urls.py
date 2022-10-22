from django.urls import path
from . import views
urlpatterns = [
    path('alg1/', views.algKNN, name='inicio'),
]