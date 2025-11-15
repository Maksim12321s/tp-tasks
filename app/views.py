from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,View
from django.core.paginator import Paginator
from app.models import *
# Create your views here.
class IndexView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        questions = Question.questions.get_BestQuestions()
        for i in questions:
            if len(i.text) > 30:
                i.text = i.text[:30] + '...'
        GetMembersTags(context)
        context["page_obj"] = paginate(questions,request,5)
        return render(request,'index.html', context)

class SettingsView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        GetMembersTags(context)
        return render(request,'settings.html', context)


class LoginView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        GetMembersTags(context)
        return render(request,'login.html', context)


class RegisterView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        GetMembersTags(context)
        return render(request,'signup.html', context)


class QuestionView(View):
    def get(self, request,q_id):
        context = {}
        question = Question.objects.get(id=q_id)
        answers = Answer.objects.filter(question_id=q_id)
        GetMembersTags(context)
        context["page_obj"] = paginate(answers,request,4)
        context["question"] = question
        return render(request,'question.html', context)


class TagsView(View):
    def get(self, request,q_tag):
        context = {}
        print(q_tag)
        tag = get_object_or_404(Tag, Name = q_tag)
        questions = Question.questions.get_by_tag(q_tag)
        for i in questions:
            if len(i.text) > 30:
                i.text = i.text[:30] + '...'
        GetMembersTags(context)
        context["page_obj"] = paginate(questions,request,5)
        context["tag"] = q_tag
        return render(request,'tags.html', context)


class AskView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        GetMembersTags(context)
        return render(request,'ask.html', context)
    


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list,per_page)
    page = paginator.get_page(request.GET.get("page"))
    return page


def GetMembersTags(context):
    q = Question.questions.get_BestQuestions()[:10]
    p_t = []
    b_m = []
    for i in q:
        p_t += (i.tag_names)
        b_m.append(i.author.nickname)
    context["best_members"] = b_m
    context["popular_tags"] = p_t