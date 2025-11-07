from rest_framework import serializers
from .models import ServiceRequest, Review, ChatMessage
from users.serializers import MechanicProfileSerializer

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ('user','mechanic','status','created_at')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user','created_at')

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    class Meta:
        model = ChatMessage
        fields = ('id','request','sender','sender_username','text','timestamp')
        read_only_fields = ('timestamp','sender_username')
