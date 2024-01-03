from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *


from posts.api_views import *
from users.api_views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/drf-auth/", include("rest_framework.urls")),
    path("posts", include("posts.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", home_view, name="home_page"),
    path("users/", include("users.urls")),
    path("titles/", titles_view, name="titles"),
    path(
        "api/token/create/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
