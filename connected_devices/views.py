# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from connected_devices.models import Mouth
from connected_devices.serializer import MouthSerializer


class MouthViewSet(ModelViewSet):
    serializer_class = MouthSerializer
    permission_classes = (AllowAny,)
    queryset = Mouth.objects.all()
