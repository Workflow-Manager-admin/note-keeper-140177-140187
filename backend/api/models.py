from django.db import models

# PUBLIC_INTERFACE
class Note(models.Model):
    """
    The Note model represents a single note entry.
    """
    title = models.CharField(max_length=255, blank=True, default="", help_text="Title of the note.")
    content = models.TextField(blank=True, help_text="Content of the note.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the note was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the note was last updated.")

    def __str__(self):
        return self.title or f'Note {self.pk}'
