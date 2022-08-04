from .views import NewsView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsView, basename="news")

urlpatterns = [
    path('', include(router.urls)),
]