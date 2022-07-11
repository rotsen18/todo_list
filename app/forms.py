from django import forms

from app.models import Task


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={'type': 'datetime-local'}
        )
    )

    class Meta:
        model = Task
        fields = "__all__"
