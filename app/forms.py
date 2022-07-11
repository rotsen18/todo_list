from django import forms

from app.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    content = forms.CharField(max_length=255)

    class Meta:
        model = Task
        fields = "__all__"
