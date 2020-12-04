from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding this method to save password in encrypted form
        """
        return get_user_model().objects.create_user(**validated_data)


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)