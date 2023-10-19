# from django.http import HttpResponse
#
#
# def start(request):
#     return HttpResponse('Добро пожаловать.')


from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


# Получить вопросы и отобразить их.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/index.html', context)


# Показать конкретный вопрос и варианты выбора ответа.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Вопроса не существует')
    return render(request, 'questions/detail.html', {'question': question})


# Получить вопрос и отобразить результаты.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questions/results.html', {'question': question})


# Голосовать за вопрос.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'questions/detail.html', {
            'question': question,
            'error_message': 'Вы не выбрали ответ',
        })
    else:
        # Возврат после успешной обработки запроса. Предотвращение двойной публикации данных, если
        # пользователь нажимает кнопку «Назад».
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
