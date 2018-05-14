from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url."""
        url = reverse(
            "accounts:account_confirm_email",
            args=[emailconfirmation.key]
        )
        ret = build_absolute_uri(
            request,
            url
        )
        return ret
