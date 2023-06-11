from rest_framework import generics
from .models import Rule
from .serializers import RuleSerializer

class RuleList(generics.ListCreateAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class RuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
