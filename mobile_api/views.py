from rest_framework import generics, parsers
from .model import BillboardReport
from .serializers import BillboardReportSerializer

class BillboardReportCreateView(generics.CreateAPIView):
    """
    API endpoint for the mobile app to create a new billboard report.
    Expects a POST request with an image file and JSON data.
    """
    queryset = BillboardReport.objects.all()
    serializer_class = BillboardReportSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def perform_create(self, serializer):
        report = serializer.save()
        
        # --- AI/ML Integration Point ---
        # The report is saved with a 'pending' status.
        # The AI/ML system should monitor for new reports, process the image,
        # and update the 'status' and 'violation_rules' fields based on the analysis.
        
        print(f"Report {report.id} created. Waiting for AI/ML processing.")
