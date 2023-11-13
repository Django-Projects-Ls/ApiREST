from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all() # This is the content of Student table
  serializer_class = StudentSerializer # This is the serializer class we created before