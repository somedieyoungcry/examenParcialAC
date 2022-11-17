from django.urls import path
from . import views
urlpatterns = [
    path('alg3/', views.algRegLog, name='inicio'),
]