from django.db import models
from django.contrib.postgres.aggregates import ArrayAgg 

class QuestionManager(models.Manager):
    def get_Newest(self):
        return self.get_queryset().select_related("author").annotate(answ_kol = models.Count('answer'),tag_names=ArrayAgg('tags__Name', distinct=True)).order_by("created_at")
    def get_BestQuestions(self):
        return self.get_queryset().select_related("author").annotate(answ_kol = models.Count('answer'),tag_names=ArrayAgg('tags__Name', distinct=True)).order_by('-like_count')[:100]
    def get_Q(self,id):
        return self.select_related("author").annotate(tag_names=ArrayAgg('tags__Name', distinct=True)).get(id=id)
    def get_by_tag(self,Tag):
        return self.filter(tags__Name = Tag).annotate(answ_kol = models.Count('answer'),tag_names=ArrayAgg('tags__Name', distinct=True)).select_related("author").prefetch_related('tags')