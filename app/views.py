from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.core.paginator import Paginator

# Create your views here.
class IndexView(View):
    def get(self, request,*args,**kwargs):
        context = {}
        questions = []
        for i in range(0,30):
            questions.append(
                {'id': i,
                 'text': "some text",
                 'title': "title" + str(i),
                 'tags':["bender", "black-jack"]}
            )
            if len(questions[i]["text"]) > 10:
                questions[i]["text"] = questions[i]["text"][:11]
        
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
        answers = []
        question = {
            "id": q_id,
            "tags": ["black-jack","bender"],
            "title": "How to build a moon park?" + str(q_id),
            "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "
        }
        for i in range(6):
            answers.append(
                {"id" : i,
                 "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}
            )
        GetMembersTags(context)
        context["page_obj"] = paginate(answers,request,4)
        context["question"] = question
        return render(request,'question.html', context)


class TagsView(View):
    def get(self, request,q_tag):
        context = {}
        questions = []
        for i in range(0,30):
            questions.append(
                {'id': i,
                 'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                 'title': "title" + str(i),
                 "tags":["bender","black-jack"]}
            )
            if len(questions[i]["text"]) > 50:
                questions[i]["text"] = questions[i]["text"][:51] + '...'
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
    p_t = ["python",
           
           "TechnoPark",
           "MYSQL",
           "Mail.ru",
           "Firefox",
           "python",
           "TechnoPark",
           "MYSQL",
           "MYSQL",
           "Mail.ru",
           "Firefox",
           "python",
           "TechnoPark"
           ]
    b_m = ["Mr. Freeman",
        "Dr. House",
        "Bender",
        "V. Pupkin"
        ]
    context["best_members"] = b_m
    context["popular_tags"] = p_t