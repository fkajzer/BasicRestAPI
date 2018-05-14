from allauth.account import views as allauth_views
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        allauth_views.confirm_email,
        name="account_confirm_email"
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        views.CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
