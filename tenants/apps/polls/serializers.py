from .views import Poll
from rest_framework.serializers import ModelSerializer


class PollSerializer(ModelSerializer):
  class Meta:
    model = Poll
    fields = '__al__'