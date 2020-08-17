from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Question


# Create your views here.
def template(request):
    context = {'label': "Hello World!!!!!"}
    return render(request, 'template.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # render()函数的第一个位置参数是请求对象（就是view函数的第一个参数），第二个位置参数是模板。还可以有一个可选的第三参数，
    # 一个字典，包含需要传递给模板的数据。最后render函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象。

    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)