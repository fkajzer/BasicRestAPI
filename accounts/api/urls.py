from django.conf.urls import url
from rest_auth import views as rest_auth_views

from . import views

urlpatterns = [
    # URLs that do not require a session or valid token
    url(
        r'^login/$',
        views.LoginView.as_view(),
        name='login'
    ),
    # URLs that require a user to be logged in with a valid session / token.
    url(
        r'^password/change/$',
        rest_auth_views.PasswordChangeView.as_view(),
        name='password_change'
    ),
]
