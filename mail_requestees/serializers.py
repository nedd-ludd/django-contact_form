from rest_framework import serializers
from .models import Mail_requestee

class Mail_requesteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail_requestee
        fields = '__all__'

