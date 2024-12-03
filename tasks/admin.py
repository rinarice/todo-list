from django.contrib import admin

from tasks.models import Task, Tag
from tasks.forms import TaskForm


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ("content", "created_at", "deadline", "status_display")
    search_fields = ("content",)
    list_filter = ("status", "tags")
    ordering = ("-created_at",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "content",
                    "deadline",
                    "status",
                    "tags",
                )
            },
        ),
    )

    def status_display(self, obj):
        return "✅ Done" if obj.status else "❌ Not Done"

    status_display.admin_order_field = "status"
    status_display.short_description = "Done / Not Done"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
