from rest_framework import serializers
from .models import CustomUser, MechanicProfile
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','email','is_mechanic','phone')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ('username','email','password','is_mechanic','phone')
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password'],
            is_mechanic = validated_data.get('is_mechanic', False),
            phone = validated_data.get('phone','')
        )
        if user.is_mechanic:
            MechanicProfile.objects.create(user=user)
        return user

class MechanicProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = MechanicProfile
        fields = '__all__'
