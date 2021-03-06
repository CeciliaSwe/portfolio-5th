"""form for users to add questions"""

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
