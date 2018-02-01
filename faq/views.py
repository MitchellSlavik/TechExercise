from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Category, Question, Answer
from .forms import QuestionForm, AnswerForm

def index(request):
	context = {'all_categories': Category.objects.all()}
	return render(request, 'index.html', context)

def categories(request, cat):
	category = get_object_or_404(Category, short_name=cat)
	context = {'questions': Question.objects.filter(category=category)}
	return render(request, 'category.html', context)
	
def question(request, id):
	context = {'question': get_object_or_404(Question, pk=id), 'form': AnswerForm()}
	return render(request, 'question.html', context)
	
def newQuestion(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = Question(title=form.cleaned_data['title'], body=form.cleaned_data['body'], category=form.cleaned_data['category'])
			question.save();
			return redirect('question', id=question.id)
	else:
		form = QuestionForm()

	return render(request, 'newquestion.html', {'form': form.as_table()})
	
def submitAnswer(request):
	question = Question.objects.get(id=request.GET['id'])
	form = AnswerForm(request.POST)
	if form.is_valid():
		answer = Answer(answer=form.cleaned_data['answer'], question=question)
		answer.save()
	return redirect('question', id=question.id)