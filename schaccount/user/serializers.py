from pyexpat import model
from rest_framework import serializers
from .models import AddStaff, AddStudents


class AddStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStaff
        fields = '__all__'


class AddStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStudents
        fields = '__all__'
