from rest_framework import serializers
from .models import Student

class Student_serilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')
