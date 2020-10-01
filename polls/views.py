from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("hello, world. you're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def owner(request):
    return HttpResponse("Hello, world. 0d85eb24 is the polls index.")