from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)