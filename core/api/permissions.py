from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class HasVerifiedEmailAddress(permissions.BasePermission):
    message = "Your email hasn't been verified yet."

    def has_permission(self, request, view):
        if "email" in request.data:
            user_queryset = User.objects.filter(
                email=request.data["email"]
            ).prefetch_related("emailaddress_set")
            if user_queryset.exists():
                email_queryset = user_queryset[0].emailaddress_set.filter(
                    email=request.data["email"])
                print("Here")
                if email_queryset.exists():
                    print(email_queryset[0].verified)
                    return email_queryset[0].verified
        return False
