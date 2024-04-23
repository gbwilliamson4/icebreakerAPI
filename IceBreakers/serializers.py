from django.contrib.auth.models import Group, User
from .models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = ['question', 'contributor']
        fields = '__all__'