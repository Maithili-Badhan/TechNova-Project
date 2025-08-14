from django.urls import path
from .views import BillboardReportCreateView

urlpatterns = [
    path('report/', BillboardReportCreateView.as_view(), name='create-report'),
]
