from rest_framework import serializers
from userprofile.models import PatientInfo
from screen.models import Screen

# PatientInfo Serializer
class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'

# Screen Serializer
class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'