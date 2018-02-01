from django import forms

from .models import Category

class QuestionForm(forms.Form):
	category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(), empty_label=None)
	title = forms.CharField(label='Title', max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	
class AnswerForm(forms.Form):
	answer = forms.CharField(label='Answer this question:', widget=forms.Textarea)