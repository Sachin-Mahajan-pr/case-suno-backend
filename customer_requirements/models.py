from django.db import models

# Create your models here.
class Requirement(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        INFORMATION_RECEIVED = (
            "information_received",
            "Information Received",
        )
        REVIEWED = "reviewed", "Reviewed"
        SERVICE_PROPOSED = "service_proposed", "Service Proposed"
        PAYMENT_PENDING = "payment_pending", "Payment Pending"
        CONVERTED = "converted", "Converted"

    class Urgency(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    reference_id = models.CharField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(max_length=120)
    internal_notes = models.TextField(blank=True, default="")
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=80)

    requirement_type = models.CharField(max_length=100)
    description = models.TextField()
    other_party = models.CharField(
        max_length=255,
        blank=True,
    )

    urgency = models.CharField(
        max_length=10,
        choices=Urgency.choices,
        default=Urgency.MEDIUM,
    )

    consent_given = models.BooleanField(default=False)

    documents = models.JSONField(default=list, blank=True)

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NEW,
    )

    reviewed_by = models.ForeignKey(
        "accounts.AdminUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_requirements",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference_id} - {self.name}"
