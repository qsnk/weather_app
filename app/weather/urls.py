from django.urls import path, include
from weather.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cities', CityViewSet)
router.register(r'history', UserSearchHistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
]