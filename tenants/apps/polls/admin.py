from django.contrib import admin
from .models import Poll   
from tenants.apps.tenant.utils import tenant_from_request                                                                                                                                                                                              
# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ["question", "created_by", "pub_date"]
    readonly_fields = ["pub_date"]

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)