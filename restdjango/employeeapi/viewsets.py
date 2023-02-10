from restdjango import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewset):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer