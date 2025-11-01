from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    admin = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='admin_clubs'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class ClubMembership(models.Model):
    MEMBER_ROLES = [
        ('member', 'Member'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('chairperson', 'Chairperson'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=MEMBER_ROLES, default='member')
    joined_on = models.DateTimeField(auto_now_add=True)

class Meeting(models.Model):
    """
    Represents a scheduled meeting for a club.
    """
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='meetings')
    topic = models.CharField(max_length=255)
    date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_meetings')

    def __str__(self):
        return f"{self.club.name} - {self.topic} ({self.date.strftime('%Y-%m-%d')})"


class MeetingMinutes(models.Model):
    """
    Stores the minutes document uploaded by the club's secretary for a specific meeting.
    """
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name='minutes')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    document = models.FileField(upload_to='minutes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Minutes for {self.meeting.topic}"


# Create your models here.
