"""form for super user to add products"""

from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """
    Form to add question
    """
    class Meta:
        """
        Meta data for question form
        """
        model = Question
        fields = '__all__'
