from tenants.apps.tenant.utils import tenant_from_request
from rest_framework import viewsets
from .models import Poll
from .serializers import PollSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)