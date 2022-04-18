from rest_framework import serializers

from connected_devices.models import Mouth


class MouthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mouth
        fields = ('id', 'host', 'username', 'password', 'exe', 'room')
