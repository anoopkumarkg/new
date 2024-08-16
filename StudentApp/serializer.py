from .models import StudentTable
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentTable
        fields='__all__'