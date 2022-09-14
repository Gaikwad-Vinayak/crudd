from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import librarymanagement_module

class librarymanagement_module_serilizeres(serializers.ModelSerializer):
    class Meta:
        model=librarymanagement_module
        fields='__all__'