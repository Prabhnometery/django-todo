from django.contrib import admin
from .models import Todo

# This will allow us to view the entires which are restricted and are not able to be edited
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
