from django.contrib import admin
from main.models import ToDo
# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title'),
admin.site.register(ToDo, ToDoAdmin)