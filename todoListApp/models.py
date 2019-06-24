from django.db import models
from django.utils import timezone

class Todo(models.Model):
    PENDING = 1
    COMPLETED = 0
    STATUS_CHOICES = (
		(PENDING, 'pending'),
		(COMPLETED, 'completed'),
	)
    title = models.CharField(max_length=250) 
    body = models.TextField(blank=True)
    creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.title