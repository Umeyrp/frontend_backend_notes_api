from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Notes
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def get_notes(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
