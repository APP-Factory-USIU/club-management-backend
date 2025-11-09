from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Club(models.Model):
    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    admin = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='admin_clubs'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_by= models.DateTimeField(auto_now=True)

class ClubMembership(models.Model):
    MEMBER_ROLES = [
        ('member', 'Member'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('chairperson', 'Chairperson'),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    role_in_club  = models.CharField(max_length=20, choices=MEMBER_ROLES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

