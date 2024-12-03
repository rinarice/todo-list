from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[(True, "Done"), (False, "Not Done")],
        widget=forms.RadioSelect,
        label="Task Status",
        help_text="Select 'Done' if the task is completed or 'Not Done' otherwise.",
    )

    class Meta:
        model = Task
        fields = "__all__"
