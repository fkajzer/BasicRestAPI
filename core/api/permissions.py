from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

# from allauth.account.models import EmailAddress


class IsSuperuser(permissions.BasePermission):
    message = "This account is not a superuser."

    def has_permission(self, request, view):
        if "email" in request.data:
            user = User.objects.get(email=request.data["email"])
            return user.is_superuser
        return False


# class HasVerifiedEmailAddress(permissions.BasePermission):
#     message = "Your email hasn't been verified yet."
#
#     def has_permission(self, request, view):
#         print("Checkin permission")
#         email_address = EmailAddress.objects.get(user=request.user)
#         return email_address.verified
