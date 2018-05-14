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
    url(
        r'^password/reset/$',
        rest_auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    # URLs that require a user to be logged in with a valid session / token.
    url(
        r'^logout/$',
        rest_auth_views.LogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^user/$',
        rest_auth_views.UserDetailsView.as_view(),
        name='user_details'
    ),
    url(
        r'^password/change/$',
        rest_auth_views.PasswordChangeView.as_view(),
        name='password_change'
    ),
]
