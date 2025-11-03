from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class CustomUser(User):
    nickname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=50)   


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter("")
    
    def newest(self):
        return self.filter()


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    questions = QuestionManager()
   



class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey("CustomUser",on_delete=models.CASCADE)
    question_id = models.ForeignKey("Question",on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    question = models.ForeignKey("Question",on_delete=models.CASCADE)

class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey("Question",on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)



