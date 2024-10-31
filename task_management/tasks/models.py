from django.db import models

# from django.conf import settings
# from datetime import datetime

# Create your models here.


class Task(models.Model):

    STATUS_CHOICE = [
        ('not_completed', 'Not completed'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='not_completed'
    )
    
    def save(self, *args, **kwargs):
        if self.is_completed:
            self.status = 'completed'
        else:
            self.status = 'not_completed'
        
        if self.status == 'completed':
            self.is_completed = True
        else:
            self.is_completed = False
        
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title
    