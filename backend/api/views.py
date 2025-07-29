from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def health(request):
    """Simple health check endpoint."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class NoteListCreateAPIView(generics.ListCreateAPIView):
    """
    List all notes or create a new note.
    GET: Returns a list of notes. Supports search with the ?q= query parameter.
    POST: Creates a new note with 'title' and 'content'.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all().order_by('-updated_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(content__icontains=q)
        return qs

# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a note by ID.
    GET: Returns a note.
    PUT/PATCH: Updates a note.
    DELETE: Deletes a note.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
