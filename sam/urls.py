from django.urls import path
from .views import SampleView

urlpatterns = [
    path('sam', SampleView),
]