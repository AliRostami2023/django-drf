from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'persons'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question')
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.title}"
    

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='que')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.body[:30]}"
    
    

