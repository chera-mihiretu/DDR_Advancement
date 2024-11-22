from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.
def showQuestion(request): 
    questions = Question.objects.order_by('-pub_date')
    context = {
        'questions': questions,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)



    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
   
    return HttpResponse(f"there is the question: {question_id}." )

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}." )