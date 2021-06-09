from rest_framework import viewsets, permissions

from userprofile.models import PatientInfo
from screen.models import Screen
from restapi.serializers import PatientInfoSerializer, ScreenSerializer

# PatientInfo Viewset
class PatientInfoViewset(viewsets.ModelViewSet):
    queryset = PatientInfo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientInfoSerializer

# Screen Viewset
class ScreenViewset(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScreenSerializer
    def perform_create(self, serializer):
        print("------------------------", self.request.user)
        serializer.save(owner=self.request.user)
