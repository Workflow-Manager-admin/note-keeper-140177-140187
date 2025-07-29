from django.contrib import admin
from .models import Note

# PUBLIC_INTERFACE
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
