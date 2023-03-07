from django.urls import path
from .views import RequesteeListView

urlpatterns = [
    path('', RequesteeListView.as_view())
]