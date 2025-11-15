from django.contrib import admin
from app.models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("login","email")
    list_filter = ("login",)
    search_fields = ("login","nickname")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title","author","created_at")

class TagAdmin(admin.ModelAdmin):
    list_display = ("id","Name")

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("user","question")

class LikeAdmin(admin.ModelAdmin):
    list_display = ("author","question")
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Like,LikeAdmin)