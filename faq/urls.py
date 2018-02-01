from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('category/<cat>', views.categories, name='category'),
	path('question/<int:id>', views.question, name='question'),
	path('newquestion/', views.newQuestion, name='newquestion'),
	path('submitanswer/', views.submitAnswer, name='submitanswer')
]