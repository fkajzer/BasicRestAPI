from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializers import LoginSerializer

# from core.api import permissions as core_permissions


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class LoginView(ObtainAuthToken):
    """
    (POST) Log in users.
    Expects email and password and returns token and uuid.
    """
    serializer_class = LoginSerializer
    # permission_classes = (core_permissions.IsSuperuser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'name': user.name,
            'uuid': user.uuid
        }, status=status.HTTP_200_OK)
