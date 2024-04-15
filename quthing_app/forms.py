from django import forms
from quthing_app.models import QuthingPatientModel
#from quthing_app.models import QuthingStaffModel

class PatientForms(forms.ModelForm):
    class Meta:
        model = QuthingPatientModel
        fields = '__all__'


# class StaffForms(forms.ModelForm):
#     class Meta:
#         model = QuthingStaffModel
#         fields = '__all__'