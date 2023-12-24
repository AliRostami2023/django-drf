from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializes import PersonSerializers, QuestionSerializer, AnswerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
from rest_framework import mixins, generics

# Create your views here.


class Home(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializers(instance=persons, many=True)
        return Response(ser_data.data)
    

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(ser_data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status.HTTP_201_CREATED)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def put(self, request, pk):
        questions = Question.objects.get(pk=pk)
        self.check_object_permissions(request, questions)
        ser_data = QuestionSerializer(data=request.data, instance=questions, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status.HTTP_200_OK)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def delete(self, request, pk):
        questions = Question.objects.get(pk=pk)
        self.check_object_permissions(request, questions)
        questions.delete()
        return Response({'message': 'this questions deleted'}, status.HTTP_200_OK)
    

# mixin
class QuestionViewMixin(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class QuestionUpdateViewMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
# end mixin
    
# generic
class QuestionGenericApi(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionGenericUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
# end generic

