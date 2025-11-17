from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.views import APIView
from details.models import Patient,Doctor,Appointment,Treatment
from details.serializers import PatientSerializer,DoctorSerializer,AppointmentSerializer,TreatmentSerializer,TreatmentReportSerializer
 
# Create your views here.

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class TreatmentViewSet(ModelViewSet):
    queryset = Treatment.objects.select_related(
    'appointment', 
    'appointment__patient',
    'appointment__doctor'
    ).all()
    serializer_class = TreatmentSerializer



# Treatment Report View
class TreatmentReportViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that provides a detailed hospital treatment report.
    """
    serializer_class = TreatmentReportSerializer

    def get_queryset(self):
        return Treatment.objects.select_related(
            'appointment',
            'appointment__patient',
            'appointment__doctor'
        ).all()