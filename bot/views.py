# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from bot.models import BotIdentity
from bot.serializer import BotSerializer


class BotViewSet(ModelViewSet):
    serializer_class = BotSerializer
    permission_classes = (AllowAny,)
    queryset = BotIdentity.objects.all()
    lookup_field = 'key'
