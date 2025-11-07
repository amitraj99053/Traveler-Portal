from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceRequest, Review, ChatMessage
from .serializers import ServiceRequestSerializer, ReviewSerializer, ChatMessageSerializer
from users.models import MechanicProfile
from django.contrib.auth import get_user_model
from math import radians, cos, sin, asin, sqrt

User = get_user_model()

def haversine(lat1, lon1, lat2, lon2):
    # returns distance in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1,lon1,lat2,lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all().order_by('-created_at')
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def nearby_mechanics(self, request):
        lat = float(request.query_params.get('lat',0))
        lon = float(request.query_params.get('lon',0))
        radius_km = float(request.query_params.get('radius',10))
        profiles = MechanicProfile.objects.filter(available=True)
        results = []
        for p in profiles:
            if p.latitude is None or p.longitude is None:
                continue
            d = haversine(lat,lon,p.latitude,p.longitude)
            if d <= radius_km:
                results.append({
                    'mechanic_id': p.user.id,
                    'username': p.user.username,
                    'skills': p.skills,
                    'rating': p.rating,
                    'distance_km': round(d,2),
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                })
        return Response(results)

    @action(detail=True, methods=['post'])
    def assign_mechanic(self, request, pk=None):
        sr = self.get_object()
        if not request.user.is_mechanic:
            return Response({'detail':'Only mechanics can accept.'}, status=status.HTTP_403_FORBIDDEN)
        if sr.mechanic is not None:
            return Response({'detail':'Already assigned'}, status=400)
        sr.mechanic = request.user
        sr.status = 'ACCEPTED'
        sr.save()
        return Response({'detail':'Assigned'})

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        sr = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(ServiceRequest.STATUS_CHOICES):
            return Response({'detail':'Invalid status'}, status=400)
        sr.status = new_status
        sr.save()
        return Response(ServiceRequestSerializer(sr).data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all().order_by('timestamp')
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
