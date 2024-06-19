from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户的学习主题"""
    text = models.CharField(max_length=200)
    date_add = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()