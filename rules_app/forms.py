# rules_app/forms.py
from django import forms
from .models import Example

class ClickableSentenceWidget(forms.TextInput):
    template_name = 'clickable_sentence_widget.html'

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ['sentence', 'highlightedIndices', 'rule']  # Include all fields that you want in the form
        widgets = {
            'sentence': ClickableSentenceWidget(),
        }
