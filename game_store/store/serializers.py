from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        exclude = ['password']

    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validation_data):
        pass

    def update(self, instance, validated_data):
        pass