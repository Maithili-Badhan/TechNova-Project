from django.db import models
from django.db.models import JSONField # Use this for most databases

class BillboardReport(models.Model):
    # --- WEB DEVELOPER'S RESPONSIBILITY (Mobile App Data) ---
    # These fields are populated by the mobile app when a user submits a report.
    # handling the upload and initial database creation.
    image = models.ImageField(upload_to='billboard_reports/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # New Field: City to handle location-specific rules
    city = models.CharField(max_length=50, blank=True, null=True)
    
    # --- AI/ML TEAM'S RESPONSIBILITY (Processing Results) ---
    # These fields are populated by the AI/ML pipeline after a report is submitted.
    # The AI/ML person will read the 'image' and 'id' from the database
    # and update these fields once their analysis is complete.
    
    # 'pending' -> 'processing' -> 'violation_found' or 'no_violation'
    status = models.CharField(max_length=20, default='pending')
    
    # This field should contain the detailed reason for violation (e.g., 'incorrect dimensions',
    # 'obscene content', 'poor placement') or be left blank if no violation is found.
    violation_reason = models.TextField(blank=True, null=True)

    # This field will store a list of rule_id's that the billboard violates.
    violation_rules = JSONField(blank=True, null=True)
    
    # New Field: To store the raw JSON output from the AI/ML model for detailed analysis
    ai_raw_output = JSONField(blank=True, null=True)

    # New Field: To track the user who submitted the report (e.g., for gamification)
    reporter_id = models.CharField(max_length=100, blank=True, null=True)
    
    # --- ADMIN/PORTAL RESPONSIBILITY (Future-proofing) ---
    # New Field: To be populated by an admin user when the report is reviewed
    reviewed_by = models.CharField(max_length=100, blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Report {self.id} - {self.status}"