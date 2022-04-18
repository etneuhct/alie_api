from rest_framework import serializers

from bot.models import BotIdentity


class BotSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotIdentity
        fields = ('id', 'name', 'voice', 'gender', 'key', 'created_at')

    def create(self, validated_data):
        bot, created = BotIdentity.objects.update_or_create(
            key=self.validated_data['key'],
            defaults=self.validated_data
        )
        return bot
