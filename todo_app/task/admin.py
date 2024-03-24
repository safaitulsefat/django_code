from django.contrib import admin
from task.models import TaskModel
# Register your models here.
class taskModelAdmin(admin.ModelAdmin):
    list_display=['id','tasktitle','taskdescription','is_completed']
admin.site.register(TaskModel)
