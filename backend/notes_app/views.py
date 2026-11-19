from django.shortcuts import render
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import viewsets

# Create your views here.


# ModelViewSet (Viewset mit allen Http-Methoden)
class NoteModelViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
