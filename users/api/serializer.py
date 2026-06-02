from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password  # <-- Importamos el encriptador nativo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Tomamos la contraseña de Locust/Insomnia y la convertimos en un hash seguro
        validated_data['password'] = make_password(validated_data['password'])
        
        # Guardamos al usuario tal como te funcionaba antes, pero ya con la contraseña encriptada
        return User.objects.create(**validated_data)
