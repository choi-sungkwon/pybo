from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question, Answer


def index(request):
    question_list = Question.objects.order_by('-created_at')

    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.save()
            return redirect('pybo:index')
    else:
        form=QuestionForm()
        context={'question_list':question_list,'form':form}
        return render(request,'pybo/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(False)
            answer.question=question
            answer.save()
            return redirect('pybo:detail',question.id)
    else:

        form=AnswerForm()
        context={'question':question,'form':form}
        return render(request,'pybo/detail.html',context)

def answer_delete(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)
    question=answer.question
    answer.delete()
    return redirect('pybo:detail',question.id)

def answer_update(request,answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method=='POST':
        form=AnswerForm(request.POST,instance=answer)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.question=answer.question
            answer.save()
            return redirect('pybo:detail', answer.question.id)
    else:

        form=AnswerForm(instance=answer)
        context={'answer':answer,'form':form}
        return render(request,'pybo/answer_update.html',context)

def question_delete(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    question.delete()
    return redirect('pybo:index')

def question_update(request, question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.method=='POST':
        form =QuestionForm(request.POST,instance=question)
        if form.is_valid():
            question=form.save(commit=False)
            question.save()
            return redirect('pybo:index')
    else:
        form=QuestionForm(instance=question)
        context={'question':question,'form':form}
        return render(request,'pybo/question_update.html',context)