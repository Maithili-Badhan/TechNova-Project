from rest_framework import serializers
from .model import BillboardReport

class BillboardReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillboardReport
        fields = ['id', 'image', 'latitude', 'longitude', 'timestamp', 'status', 'violation_rules']
        # The AI/ML team will populate violation_rules, so it's read-only for the mobile app
        read_only_fields = ['id', 'timestamp', 'status', 'violation_rules']
