from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookView
from .api_views import BookViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .auth_views import RegisterView

router = DefaultRouter()
router.register(r"api/books", BookViewSet, basename="book-api")

urlpatterns = [
    path("", BookView.as_view(), name="book-list"),
    path("delete/<int:book_id>/", BookView.as_view(), name="book-delete"),
    path("", include(router.urls)),
    # Authentication URLs
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
]
