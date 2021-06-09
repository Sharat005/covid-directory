from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from utils.models_util import YesNo, Gender

# Model for Eligibility Form
class Screen(models.Model):
    patient = models.ForeignKey("userprofile.PatientInfo", verbose_name=_(
        "Patient ID"), on_delete=models.CASCADE)
    screen_age_yn = models.IntegerField(
        _("Are you between the ages 40-80?"), choices=YesNo.choices)
    screen_age = models.IntegerField(_("Specify age:"), null=True, blank=True)
    screen_gender = models.IntegerField(
        _("Please confirm your gender"), choices=Gender.choices, null=True, blank=True)
    screen_smoking_yn = models.IntegerField(
        _("Are you a current or former smoker?"), choices=YesNo.choices, null=True, blank=True)
    screen_smoking_amount = models.IntegerField(
        _("On average, how many packs do or did you smoke per day?"), null=True, blank=True)
    screen_smoking_years = models.IntegerField(
        _("How many years have you (or had you) smoked?"), null=True, blank=True)
    screen_packyears = models.IntegerField(
        _("Packyear Calculation Result"), null=True, blank=True)
    screen_20packyears_yn = models.IntegerField(
        _("B1b. Based on your calculation, does the subject have 10 pack-year smoking history?"), choices=YesNo.choices, null=True, blank=True)
    screen_pregnancy_yn = models.IntegerField(
        _("(FEMALES ONLY) Are you pregnant, breast-feeding, or planning to become pregnant in the next 3 months?"), choices=YesNo.choices, null=True, blank=True)
    screen_rx_respiratoryinfection_yn = models.IntegerField(
        _("C2. Have you received a course of antibiotics or systemic steroids for respiratory infection within the past 4 weeks?"), choices=YesNo.choices, null=True, blank=True)
    screen_hx_asthma_yn = models.IntegerField(
        _("Do you have a history of asthma?"), choices=YesNo.choices, null=True, blank=True)
    screen_hx_asthma_age = models.IntegerField(
        _("Please provide age when diagnosed."), null=True, blank=True)
    screen_hx_lungdisease_yn = models.IntegerField(
        _("Do you have a history of lung disease?"), choices=YesNo.choices, null=True, blank=True)
    screen_hx_lungdisease = models.CharField(
        _("Please specify"), max_length=300, blank=True)
    screen_diabetes_yn = models.IntegerField(
        _("Do you have Diabetes Type I?"), choices=YesNo.choices, null=True, blank=True)
    screen_lungcancer_yn = models.IntegerField(
        _("Do you have lung cancer or a history of lung cancer?"), choices=YesNo.choices, null=True, blank=True)
    screen_dx_additional_yn = models.IntegerField(
        _("Do you have narrow-angle glaucoma, bladder-neck obstruction or severe renal impairment or urinary retention?"), choices=YesNo.choices, null=True, blank=True)
    screen_investigationaldrug_yn = models.IntegerField(
        _("Are you currently or have you in the past 30 days participated in any other clinical trials involving an investigational drug?"), choices=YesNo.choices, null=True, blank=True)
    screen_hx_atrialfibrillation_yn = models.IntegerField(
        _("Do you have a history of atrial fibrillation?"), choices=YesNo.choices, null=True, blank=True)
    screen_therapy_atrialfibrillation_yn = models.IntegerField(
        _("Have you been on therapy for your atrial fibrillation for 6 months or more?"), choices=YesNo.choices, null=True, blank=True)
    screen_treatment_atrialfibrillation_yn = models.IntegerField(
        _("Has your atrial fibrillation been well controlled with treatment for 6 months or more?"), choices=YesNo.choices, null=True, blank=True)
    screen_bph_yn = models.IntegerField(
        _("Do you have Benign Prostatic Hyperplasia (BPH)?"), choices=YesNo.choices, null=True, blank=True)
    screen_treatment_bph_yn = models.IntegerField(
        _("Are you on stable treatment for BPH?"), choices=YesNo.choices, null=True, blank=True)
    screen_comments = models.CharField(
        _("Any other information would you like to provide."), max_length=300, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    
