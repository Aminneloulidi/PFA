from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DemandeMentorat
from .serializers import DemandeMentoratSerializer # type: ignore

class DemandeMentoratView(APIView):
    def post(self, request):
        serializer = DemandeMentoratSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
