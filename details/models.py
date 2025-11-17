from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    patient_name = models.CharField(max_length=100)
    patient_age = models.PositiveIntegerField()
    patient_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    patient_contact = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return f"{self.patient_name}"


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = (
        ('cardiologist','Cardiologist'),
        ('dermatologist','Dermatologist'),
        ('neurologist','Neurologist'),
        ('pediatrician','Pediatrician'),
        ('psychiatrist','Psychiatrist'),
        ('radiologist','Radiologist'),
        ('surgeon','Surgeon'),
        ('general physician','Genaral Physician'),

    )
    doctor_name = models.CharField(max_length=100)
    specialization=models.CharField(max_length=30,choices=SPECIALIZATION_CHOICES)
    doctor_contact = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.doctor_name} - {self.specialization}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', "Scheduled"),
        ("pending", "Pending"),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ('no show', 'No Show'),
        ('checked in', 'Checked In'),
        ('checked out', 'Checked Out'),
        ('in progress', 'In Progress'),
        ('on hold', 'On Hold'),
        ('awaiting approval', ' Awaiting Approval'),
        ('declined', 'Declined'),
        ('missed', 'Missed'),
        ('follow-up required', 'Follow-up Required',)
    )
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    appointment_date = models.DateTimeField()
    appointment_status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return f"Appointment: {self.patient.patient_name} with Dr. {self.doctor.doctor_name}"
    

class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,related_name='treatments')
    treatment_description = models.TextField()
    treatment_cost = models.DecimalField(max_digits=10,decimal_places=2)
    treatment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Treatment for {self.appointment.patient.patient_name}"