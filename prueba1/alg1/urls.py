from django.urls import path
from . import views
urlpatterns = [
    path('alg1/', views.algKNN_list, name='algKNN'),
]