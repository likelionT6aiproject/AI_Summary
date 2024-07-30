from django.urls import path
from .views import SummarizeView, IndexView

urlpatterns = [
    path('summarize/', SummarizeView.as_view(), name='summarize'),
    path('', IndexView.as_view(), name='index'),
]