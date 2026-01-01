from django.urls import path
from .views import blogpost, home

urlpatterns = [
    path('', home, name='home'),        # 👈 ADD THIS
    path('allpost/', blogpost, name='blog'),
]
