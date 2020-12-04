from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from account.serializers import UserSerializer, SignInSerializer


class SignupAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.create(user=user)
        data = {
            'token': token.key,
            'user': serializer.validated_data,
        }

        return Response(data=data, status=status.HTTP_201_CREATED)


class SigninAPIView(GenericAPIView):
    serializer_class = SignInSerializer
    queryset = get_user_model().objects.filter(is_active=True)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_qs = self.get_queryset().filter(username=serializer.validated_data['username'])

        if not user_qs.exists():
            raise AuthenticationFailed('User is not register.')
        user = user_qs.first()
        if not user.check_password(serializer.validated_data['password']):
            raise AuthenticationFailed('Invalid username or password')
        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
            'user': serializer.validated_data,
        }
        return Response(data=data, status=status.HTTP_200_OK)
