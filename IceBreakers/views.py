from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import random

from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for reading and updating questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view(['GET'])
def getData(request):
    queryset = Question.objects.all()
    serializer = QuestionSerializer(queryset, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def getRandom(request):
#     total_questions = Question.objects.aggregate(total=Count('id'))['total']
#     if not total_questions > 0:
#         return Response({'message': 'No questions available'}, status=404)
#
#     random_index = random.randint(0, total_questions - 1)
#     random_question = Question.objects.all()[random_index]
#     serializer = QuestionSerializer(random_question)
#     return Response(serializer.data)

@api_view(['GET'])
def my_test(request):
    newQuestion = Question(question="this is the question")
    newQuestion.save()
    return Response({"Success": "I think it worked."})

class RandomQuestion(APIView):
    def get(self, request):
        approved_questions = Question.objects.filter(approved=True)
        # total_questions = Question.objects.aggregate(total=Count('id'))['total']
        total_questions = approved_questions.count()
        if not total_questions > 0:
            return Response({'message': 'No questions available'}, status=404)

        random_index = random.randint(0, total_questions - 1)
        random_question = approved_questions[random_index]
        serializer = QuestionSerializer(random_question)
        return Response(serializer.data)

    # def post(self, request):
    #     data = request.POST.get('data', None)
    #     print(data)
    #     # obj = Question()
    #     return Response({"Test": "Sample response"})

    # def put(self, request):
    #     return Response({"Test": "Sample response"})

