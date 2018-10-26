from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.utils import timezone

from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #返回最近的5个问题不包括未来
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

    """
    Question.objects.filter（pub_date__lte = timezone.now（））返回一个查询集，其中包含pub_date小于或等于的问题
     - 即早于或等于 - timezone.now。
    """

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args = (question.id,)))

