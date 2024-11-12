from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def showQuestion(request): 
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.q_text for q in questions])
    return HttpResponse(f"{output}" )

def result(request, question_id):
   
    return HttpResponse(f"there is the question: {question_id}." )

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}." )