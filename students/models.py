from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField(help_text="List your skills separated by commas")
    expertise = models.TextField(help_text="Describe your expertise")
    department = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    id_card_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    feedback_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class SkillRequest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined')
], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.skill})"

class Feedback(models.Model):
    request = models.OneToOneField('SkillRequest', on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.request} (Rating: {self.rating})"