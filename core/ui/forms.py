from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from screen.models import Screen
from userprofile.models import PatientInfo

class PatientInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientInfoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PatientInfo
        fields = '__all__'


class ScreenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScreenForm, self).__init__(*args, **kwargs)

    def clean(slef):
        cleaned_data = super().clean()
        patient = cleaned_data.get('patient')
        count = Screen.objects.filter(patient=patient.id).count()
        if(count >= 3):
            raise ValidationError(
                "Sorry, you can only check your eligibility 3 times."
            )

    class Meta:
        model = Screen
        fields = '__all__'

class ZipForm(forms.Form):
    zipcode = forms.IntegerField(label="Zipcode", required=True)