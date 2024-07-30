from django.db import models

class TodoItem(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Kolom description tetap bisa kosong
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title