from django.urls import path
from rent.views import index

urlpatterns = [
    path('', index),
    path('areas/', index),
]