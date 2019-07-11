"""lecture-drf-yasg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

APISchemaView = get_schema_view(
    openapi.Info(
        title='FastCampus API',
        default_version='v1',
        description='FastCampus API Documentation',
        contact=openapi.Contact(email='dev@lhy.kr'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns_apis = [
    path('blog/', include('blog.urls')),
]
urlpatterns = [
    path('doc/', APISchemaView.with_ui('redoc', cache_timeout=0)),

    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns_apis)),
]
