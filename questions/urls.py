"""
urls for questions app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionsList.as_view(), name='questions'),
    path('manage/', views.manage_questions, name='manage_questions'),
    path('add/', views.add_question, name='add_question'),
]