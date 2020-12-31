from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add', DisplayView.as_view(), name='add'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]
