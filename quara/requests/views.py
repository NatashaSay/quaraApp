from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from quaraDB.models import *
from .serializers import ControlSerializer


class ControlView(APIView):
    def get(self, request):
        control = Control.objects.all()
        serializer = ControlSerializer(control, many=True)
        return Response({"control": serializer.data})
