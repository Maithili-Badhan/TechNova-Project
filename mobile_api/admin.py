from django.contrib import admin
from .model import BillboardReport

@admin.register(BillboardReport)
class BillboardReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'latitude', 'longitude', 'status')
    list_filter = ('status',)
    search_fields = ('violation_reason',)
