from pyexpat import model
from rest_framework import serializers
from .models import AddStaff


class AddStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStaff
        fields = '__all__'
