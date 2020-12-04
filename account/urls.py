from django.urls import path
from .views import SignupAPIView, SigninAPIView

app_name = 'account'

urlpatterns = [
    path('signup', SignupAPIView.as_view(), name='signup'),
    path('signin', SigninAPIView.as_view(), name='signin'),
]