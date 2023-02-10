from rest_framework import viewsets
# from rest_framework_swagger.views import get_swagger_view
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer