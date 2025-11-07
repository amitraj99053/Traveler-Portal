from django.urls import path
from .views import RegisterView, CurrentUserView, MechanicProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', CurrentUserView.as_view(), name='me'),
    path('mechanic-profile/', MechanicProfileUpdateView.as_view(), name='mechanic-profile'),
]
