from details.models import Patient,Doctor,Appointment,Treatment
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='appointment.patient.patient_name', read_only=True)
    # dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    class Meta:
        model = Treatment
        fields = ['id','patient_name','appointment','treatment_description','treatment_cost','treatment_date']



# Treatment Report Serializer

class TreatmentReportSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='appointment.patient.patient_name', read_only=True)
    patient_gender = serializers.CharField(source='appointment.patient.patient_gender', read_only=True)
    patient_age = serializers.IntegerField(source='appointment.patient.patient_age', read_only=True)
    doctor_name = serializers.CharField(source='appointment.doctor.doctor_name', read_only=True)
    doctor_specialization = serializers.CharField(source='appointment.doctor.specialization', read_only=True)
    appointment_date = serializers.DateTimeField(source='appointment.appointment_date', read_only=True)

    class Meta:
        model = Treatment
        fields = [ 'patient_name', 'patient_gender','patient_age', 'doctor_name','doctor_specialization','appointment_date', 'treatment_description', 'treatment_cost', 'treatment_date', ]