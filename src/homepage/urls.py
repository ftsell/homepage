"""
URL configuration for homepage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path("admin/openid-auth/", include("simple_openid_connect.integrations.django.urls")),
    path("admin/", admin.site.urls),
    path("", include("homepage.core.urls")),
    path("blog/", include("homepage.blog.urls")),
    path("api/", include("homepage.api.urls")),
    path("metrics/", include("homepage.metrics.urls")),
]

handler404 = "homepage.core.views.not_found_view"
