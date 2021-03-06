from django.db import models
# from django.contrib.auth.models import User


# is_doctor = models.BooleanField(default=False)
# is_doctor.contribute_to_class(User, 'is_doctor')

# create medical-summary model
class medicalsummary(models.Model):
    medication_item = models.CharField(max_length=50)
    form = models.CharField(max_length=50)
    strength_concentration = models.FloatField()
    presentation = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    expire = models.CharField(max_length=100)
    batch_id_timing = models.CharField(max_length=50)
    amount = models.FloatField()
    amount_unit = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return str(self.patient_id)


# create problem-list model
class problemList(models.Model):
    diagnosisName = models.CharField(max_length=100)
    bodySite = models.CharField(max_length=100)
    dateOfOnset = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    diagnosticCertainity = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.diagnosisName


# create Diagnostics-result model
class dignosticsresults(models.Model):
    test_name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    method_of_diagnosis = models.CharField(max_length=100)
    body_site = models.CharField(max_length=100)
    test_result = models.CharField(max_length=50)
    patient_id = models.IntegerField()

    def __str__(self):
        return str(self.patient_id)


# create Past History of illnesses model
class pasthistory(models.Model):
    diagnosis_name = models.CharField(max_length=50)
    body_site = models.CharField(max_length=100)
    date_of_onsite = models.DateField()
    severity = models.CharField(max_length=100)
    Problem_Qualifier = models.CharField(max_length=100)
    diagnostic_certainty = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return self.patient_id


# create planCare model
class planCare(models.Model):
    carePlanName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    reason = models.CharField(max_length=100)
    type_of_diet = models.CharField(max_length=100)
    bedrest = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return str(self.patient_id)


# create prescription model
class prescription(models.Model):
    medication_item = models.CharField(max_length=100)
    substance_name = models.CharField(max_length=100)
    form = models.CharField(max_length=100)
    strength = models.FloatField()
    strength_unit = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    dosage_instructions = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    max_amount = models.FloatField()
    max_amount_dose_unit = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)
    patient_id = models.IntegerField()

    def __str__(self):
        return str(self.patient_id)


# create patient info model

class patientInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
