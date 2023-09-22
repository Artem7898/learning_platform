from django.db import models
from django.contrib.auth.models import User
from .validators.custom_validators import validate_video_link


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField(validators=[validate_video_link])
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product)


class ViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched_time_seconds = models.IntegerField()
    status = models.CharField(max_length=20, choices=[("WATCHED", "Просмотрено"), ("NOT_WATCHED", "Не просмотрено")])
    viewed_at = models.DateTimeField(auto_now=True)
