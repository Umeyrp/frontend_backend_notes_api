from rest_framework import serializers
from .models import Notes  # sobald du ein Model hast


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
