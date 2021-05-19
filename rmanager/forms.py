from django import forms

class TaskSubmitForm(forms.Form):
    CHOICES =(
    ("1", "DIAG"),
    ("2", "START"),
    ("3", "STOP"),
    )
    trg = forms.CharField(label='Trg', max_length=3)
    action = forms.ChoiceField(label='Action',choices=CHOICES)
