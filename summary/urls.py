from django.urls import path
from .views import summarize, index

urlpatterns = [
    path('summarize/', summarize, name='summarize'),
    path('', index, name='index'),
]