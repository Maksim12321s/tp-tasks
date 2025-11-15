from django.db import models
from datetime import datetime
from app.managers import QuestionManager


class CustomUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=50,default="static/img/avatar.png")   
    password = models.CharField(max_length=50)
    login = models.CharField(max_length=50,unique=models.UniqueConstraint)
    email = models.CharField(max_length=50)
    objects = models.Manager()
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name="Заголовок вопроса",max_length=50)
    text = models.CharField(verbose_name="Текст вопроса",max_length=500)
    author = models.ForeignKey("CustomUser",verbose_name="автор вопроса",null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(db_comment="Дата публикации")
    like_count = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Количество лайков")
    tags = models.ManyToManyField("Tag",blank=True)
    questions = QuestionManager()
    objects = models.Manager()
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
   



class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("CustomUser",on_delete=models.CASCADE)
    question = models.ForeignKey("Question",on_delete=models.CASCADE)
    text = models.CharField(max_length=500,verbose_name="Текст вопроса")
    objects = models.Manager()
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50,verbose_name="Название тега",unique=True)
    objects = models.Manager()
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey("Question",on_delete=models.CASCADE)
    author = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    objects = models.Manager()
    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"