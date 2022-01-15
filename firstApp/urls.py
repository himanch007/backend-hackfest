from django.urls import path
from . import views
from .views import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User', userviewsets)
urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.userLogout,name='logout'),
    # path('api/medicalsummary', views.medicalsummaryView.as_view()),
    # path('api/medicalsummary/<int:pk>', views.medicalsummaryView.as_view()),

    # Medical-Summary path
    path('medicalSummary/<int:fk>',views.getAllMedicalSummary,name='getAllMedicalSummary'),
    path('medicalOneSummary/<int:pk>',views.getOneMedicalSummary,name='getOneMedicalSummary'),
    path('addOneRecord/<int:fk>',views.addOneRecord,name='addOneRecord'),
    path('updateRecord/<int:pk>',views.updateRecord,name='updateRecord'),
    path('deleteRecord/<int:pk>',views.deleteRecord,name='deleteRecord'),

    # Problem-List path
    path('problemList',views.getProblemList,name='getProblemList'),
    path('problemList/<int:pk>',views.getOneProblemList,name='getOneProblemList'),
    path('addOneProblemList/<int:fk>',views.addOneToProblemList,name='addOneToProblemList'),
    path('updateProblemList/<int:pk>',views.updateProblemList,name='updateProblemList'),
    path('deleteProblemList/<int:pk>',views.deleteProblemList,name='deleteProblemList'),

    # Diagnostic-Result path 
    path('diagnosticResult/<int:pk>',views.getAllDiagnosticResults,name='getAllDiagnosticResultRecords'),
    path('diagnosticOneResult/<int:pk>',views.getOneDiagnosticResults,name='getAllDiagnosticResultRecords'),
    path('addOneDignosticResult/<int:fk>',views.addOneDiagnosticRecord,name='AddOneDiagnosticRecord'),
    path('updateDiagnosticRecord/<int:pk>',views.updateDiagnosticRecord,name='updateDiagnosticsRecord'),
    path('deleteDiagnosticRecord/<int:pk>',views.deleteDiagnosticRecord,name='deleteDiagnosticsRecord'),
    
    # Past History illnesses path
    path('allPastHistoryOfIllness',views.getAllPastHistoryIllnessResult,name='getAllPastHistoryOfIllness'),
    path('pastHistoryOfIllness/<int:pk>',views.getOnePastHistoryResults,name='getOnePastHistoryOfIllness'),
    path('addOneIllnessRecord/<int:fk>',views.addOneIllnessRecord,name='addOneIllnessRecord'),
    path('updateIllnessRecord/<int:pk>',views.updateIllnessRecord,name='updateIllnessRecord'),
    path('deleteIllnessRecord/<int:pk>',views.deleteIllnessRecord,name='deleteIllnessRecord'),

    # Plan care paths
    path('planCare',views.getPlanCare,name='getPlanCare'),
    path('planCare/<int:pk>',views.getOnePlanCare,name='getOnePlanCare'),
    path('addOnePlanCare/<int:fk>',views.addOneToPlanCare,name='addOneToPlanCare'),
    path('updatePlanCare/<int:pk>',views.updatePlanCare,name='updatePlanCare'),
    path('deletePlanCare/<int:pk>',views.deletePlanCare,name='deletePlanCare'),

    # prescription paths
    path('prescription/<int:fk>',views.getPrescription,name='getPrescription'),
    path('onePrescription/<int:pk>',views.getOnePrescription,name='getOnePrescription'),
    path('addOnePrescription/<int:fk>',views.addOnePrescription,name='addOnePrescription'),
    path('updatePrescription/<int:pk>',views.updatePrescription,name='updatePrescription'),


    #patient info paths
    path('patientInfo',views.getPatientInfo,name='getPatientInfo'),
    path('patientInfo/<int:pk>',views.getOnePatientInfo,name='getOnePatientInfo'),
    path('addPatientInfo',views.addToPatientInfo,name='addToPatientInfo'),
    path('updatePatientInfo/<int:pk>',views.updatePatientInfo,name='updatePatinetInfo'),
    path('deletePatientInfo/<int:pk>',views.deletePatientInfo,name='deletePatientInfo'),
]