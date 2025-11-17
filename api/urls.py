from django.urls import path,include
from rest_framework_nested import routers
from details.views import PatientViewSet,DoctorViewSet,AppointmentViewSet,TreatmentViewSet,TreatmentReportViewSet

router = routers.DefaultRouter()
router.register('patients',PatientViewSet,basename='patients')
router.register('doctors',DoctorViewSet,basename='doctors')
router.register('appointments',AppointmentViewSet,basename='appointments')
router.register('treatments',TreatmentViewSet,basename='treatments')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('reports',TreatmentReportViewSet.as_view({'get': 'list'}),name='reports')
]
