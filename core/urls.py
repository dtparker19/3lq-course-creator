# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf import settings
from urllib import request
from django.contrib import admin
from django.urls import path, include  # add this
print (request.url2pathname)

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),            # UI Kits Html files
    #path("", include('apps.urlshorten.urls'))
    path("courses/", include("apps.course.urls")),
    path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns