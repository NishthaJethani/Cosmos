from django.db import models
from students.models import Student
from wardens.models import Warden


class LeaveApplication(models.Model):
    STATUS_CHOICES=(
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    )

    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.CharField(max_length=255)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leave_applications')
    leave_approver = models.ForeignKey(Warden, on_delete=models.SET_NULL, null=True, blank=True, related_name='leave_applications')
