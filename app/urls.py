from django.urls import path,re_path
from app.views import IndexView,AskView,LoginView,QuestionView,RegisterView,SettingsView,TagsView,HotQ
urlpatterns = [
    re_path(r'^settings',SettingsView.as_view(),name = "settings"),
    re_path(r'^tags/(?P<q_tag>[\w-]+)',TagsView.as_view(), name = "tags"),
    re_path(r'^login',LoginView.as_view(), name = "login"),
    re_path(r'^question/(?P<q_id>\d+)',QuestionView.as_view(), name = "question"),
    re_path(r'^register',RegisterView.as_view(), name = "register"),
    re_path(r'^ask',AskView.as_view(), name = "ask"),
    re_path(r'^hot',HotQ.as_view(), name = "hotquestions"),
    path('',IndexView.as_view(), name="mainpage")
]
