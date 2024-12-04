from django import forms
from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[(True, "Done"), (False, "Not Done")],
        widget=forms.RadioSelect,
        label="Task Status",
        help_text="Select 'Done' if the task is completed or 'Not Done' "
                  "otherwise.",
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "status", "tags", "deadline"]
