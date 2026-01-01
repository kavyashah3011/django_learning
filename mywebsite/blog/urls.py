from django.urls import path
from .views import blogpost

urlpatterns = [
    path('', blogpost, name='home'),        # 👈 ADD THIS
    path('allpost/', blogpost, name='blog'),
]
