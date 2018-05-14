from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('myproject.api_urls', namespace="api")),
    url(r'^auth/', include('accounts.urls', namespace="accounts")),
]
