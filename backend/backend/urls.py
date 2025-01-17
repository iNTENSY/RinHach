from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import settings
from .spectacular import urlpatterns as spectacular_urls
from core.views import IndexListView, ChangeStatusRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', IndexListView.as_view(), name='index'),
    path('change-status/', ChangeStatusRedirectView.as_view(), name='change')
] + spectacular_urls


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()