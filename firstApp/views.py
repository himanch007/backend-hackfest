from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

#for apis
from .serializers import medicalsummarySerializer,dignosticsresultSerializer,pasthistorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import medicalsummary,dignosticsresult,pasthistory

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = UserCreationForm()
    return render(request, "register.html", {"form": f})

def signin(request):
    if request.method == "POST":
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pd = f.cleaned_data['password']
            user = authenticate(username = un, password = pd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
    else:
        f = AuthenticationForm()
    return render(request, 'signin.html', {'form': f})

def home(request):
    return render(request, 'home.html',  {'name': request.user})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/signin')


# Medical summary api's
# Get all the records
@api_view(['GET'])
def getAllMedicalSummary(request):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.all()
        serialize = medicalsummarySerializer(medicalRecord, many=True)
        return Response(serialize.data)

# Get only one record based on id
@api_view(['GET'])
def getOneMedicalSummary(request, pk):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(medicalRecord, many=False)
        return Response(serialize.data)

# Add one record
@api_view(['POST'])
def addOneRecord(request):
    if request.method == 'POST':
        serialize = medicalsummarySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# Update a record based on id
@api_view(['POST'])
def updateRecord(request, pk):
    if request.method == 'POST':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(instance=medicalRecord, data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)

# Delete a record
@api_view(['DELETE'])
def deleteRecord(request, pk):
    if request.method == 'DELETE':
        medicalRecord = medicalsummary.objects.get(id=pk)
        medicalRecord.delete()
        return Response("Record deleted successfully")

# class medicalsummaryView(APIView):
#     def get(self, request):
#         player1 = medicalsummary.objects.all()
#         serialize = medicalsummarySerializer(player1, many=True)
#         return Response(serialize.data)

#     def get(self, request, pk, format=None):
#         player1 = medicalsummary.objects.get(id=pk)
#         serialize = medicalsummarySerializer(player1, many=False)
#         return Response(serialize.data)
    
#     def post(self, request):
#         serialize = medicalsummarySerializer(data=request.data)
#         if(serialize.is_valid()):
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors)



# diagnostics-result api
# view all diagnostics records
@api_view(['GET'])
def getAllDiagnosticResults(request):
    if request.method == 'GET':
        diagnosticRecord =dignosticsresult.objects.all()
        serialize = dignosticsresultSerializer(diagnosticRecord, many=True)
        return Response(serialize.data)

#view one diagnostic records
@api_view(['GET'])
def getOneDiagnosticResults(request,pk):
    if request.method == 'GET':
        diagnosticRecord =dignosticsresult.objects.get(id=pk)
        serialize = dignosticsresultSerializer(diagnosticRecord, many=False)
        return Response(serialize.data)

# Add one diagnostic-result 
@api_view(['POST'])
def addOneDiagnosticRecord(request):
    if request.method == 'POST':
        serialize = dignosticsresultSerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# Update Diagnostic result record
@api_view(['POST'])
def updateDiagnosticRecord(request, pk):
    if request.method == 'POST':
        diagnosticRecord = dignosticsresult.objects.get(id=pk)
        serialize = dignosticsresultSerializer(instance= diagnosticRecord , data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)


# Delete a Diagnostic Result record
@api_view(['DELETE'])
def deleteDiagnosticRecord(request, pk):
    if request.method == 'DELETE':
        dignosticRecord = dignosticsresult.objects.get(id=pk)
        dignosticRecord.delete()
        return Response(" Dignostics Result Record deleted successfully")


# Past_History_of_illness api

# View all Patient Past_history_illnesses 
@api_view(['GET'])
def getAllPastHistoryIllnessResult(request):
    if request.method == 'GET':
        pastRecord =pasthistory.objects.all()
        serialize = pasthistorySerializer(pastRecord, many=True)
        return Response(serialize.data)

#view one  Patient Past_history_illnesses record
@api_view(['GET'])
def getOnePastHistoryResults(request,pk):
    if request.method == 'GET':
        pastRecord =pasthistory.objects.get(id=pk)
        serialize = pasthistorySerializer(pastRecord, many=False)
        return Response(serialize.data)

# Add one Patient Past_history_illnesses record
@api_view(['POST'])
def addOneIllnessRecord(request):
    if request.method == 'POST':
        serialize = pasthistorySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)


# Update Patient Past_history_illnesses record
@api_view(['POST'])
def updateIllnessRecord(request, pk):
    if request.method == 'POST':
        pastRecord = pasthistory.objects.get(id=pk)
        serialize = pasthistorySerializer(instance= pastRecord , data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)


# Delete a Patient Past_history_illnesses record
@api_view(['DELETE'])
def deleteIllnessRecord(request, pk):
    if request.method == 'DELETE':
        pastRecord = pasthistory.objects.get(id=pk)
        pastRecord.delete()
        return Response(" Past History Illness Record deleted successfully")