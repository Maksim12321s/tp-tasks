from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import Like, Question

@receiver(post_save, sender=Like)
def increment_like_count(sender, instance, created, **kwargs):
    if created:
        Question.objects.filter(pk=instance.question_id).update(like_count=F('like_count') + 1)

@receiver(post_delete, sender=Like)
def decrement_like_count(sender, instance, **kwargs):
    Question.objects.filter(pk=instance.question_id).update(like_count=F('like_count') - 1)