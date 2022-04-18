from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bot.views import BotViewSet
from connected_devices.views import MouthViewSet

router = DefaultRouter()
router.register(r'bot', BotViewSet, basename='bot')
router.register(r'mouth', MouthViewSet, basename='mouth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
