from rest_framework import routers
from django.urls import path, include
from .views import ServiceRequestViewSet, ReviewViewSet, ChatMessageViewSet

router = routers.DefaultRouter()
router.register('requests', ServiceRequestViewSet, basename='requests')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('messages', ChatMessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
