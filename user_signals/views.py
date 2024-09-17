from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import *
import threading

# Create your views here.

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    print(f"View running in thread: {threading.current_thread().name}")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)