from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from utils.models_util import YesNo, Phone1Type, Phone2Type
from utils.models_util import TimeMerediem, States, RecruitmentSources
from utils.models_util import Gender, Race, Ethnicity

# Patient Info / User Profile
class PatientInfo(models.Model):
    name_first = models.CharField(_("First Name"), max_length=50)
    name_middle = models.CharField(_("Middle Name"), max_length=50, blank=True)
    name_last = models.CharField(_("Last Name"), max_length=50)
    dob = models.DateField(
        _("Date of Birth"), auto_now=False, auto_now_add=False)
    phone1 = PhoneNumberField(_("Primary Phone Number"))
    phone1_type = models.IntegerField(
        _("Type of Phone"), choices=Phone1Type.choices)
    phone1_text_yn = models.IntegerField(
        _("Are you willing to receive text messages at this number?"), choices=YesNo.choices, null=True, blank=True)
    contact_basetime_survey = models.IntegerField(
        _("When is the best time to contact you?"), choices=TimeMerediem.choices)
    phone2 = PhoneNumberField(
        _("Secondary Phone Number"), null=True, blank=True)
    phone2_type = models.IntegerField(
        _("Type of Phone"), choices=Phone2Type.choices, null=True, blank=True)
    phone2_text_yn = models.IntegerField(
        _("Are you willing to receive text messages at this number?"), choices=YesNo.choices, null=True, blank=True)
    address1 = models.CharField(
        _("Address 1 (Building no. & Street name)"), max_length=100)
    address2 = models.CharField(
        _("Address 2 (If applicable, Unit/Apt no.)"), max_length=100, blank=True)
    city = models.CharField(_("City"), max_length=50)
    state = models.IntegerField(_("State"), choices=States.choices)
    zipcode = models.CharField(_("Zip Code"), max_length=6)
    voicemail_yn_survey = models.IntegerField(
        _("May the UIC Breathe Chicago Center leave you a voicemail the above number?"), choices=YesNo.choices)
    copd_yn_survey = models.IntegerField(
        _("Has a doctor told you that you have Chronic Obstructive Pulmonary Disease (COPD)?"), choices=YesNo.choices)
    copd_exacerbation_yn_survey = models.IntegerField(
        _("Have you had a COPD exacerbation (flare-up) requiring treatment within the last 6 weeks"), choices=YesNo.choices, null=True, blank=True)
    smoking_yn_survey = models.IntegerField(
        _("Have you ever smoked cigarettes?"), choices=YesNo.choices)
    smoking_now_yn_survey = models.IntegerField(
        _("Do you now smoke cigarettes (as of 1 month ago)?"), choices=YesNo.choices, null=True, blank=True)
    smoking_start_survey = models.IntegerField(
        _("How old were you when you first started regular cigarette smoking?"), null=True, blank=True)
    smoking_stop_survey = models.IntegerField(
        _("If you stopped smoking cigarettes completely, how old were you when you stopped?"), null=True, blank=True)
    smoking_amount_survey = models.IntegerField(
        _("On the average of the entire time you smoked, how many cigarettes do/did you smoke per day? (20 cigarettes = 1 pack)?"), null=True, blank=True)
    rx_bp_yn_survey = models.IntegerField(
        _("Are you using any blood pressure medicines?"), choices=YesNo.choices)
    rx_bp_survey = models.CharField(
        _("Please list the blood pressure medicine you currently use."), max_length=300, blank=True)
    recruitment_source_survey = models.IntegerField(
        _("Where did you hear about us?"), choices=RecruitmentSources.choices)
    recruitment_source_other_survey = models.CharField(
        _("Please specify 'Other'"), max_length=100, blank=True)
    
    current_age = models.IntegerField(_("Current Age"), null=True, blank=True)
    gender = models.IntegerField(_("5. Gender"), choices=Gender.choices)
    race = models.IntegerField(_("5.1. Race"), choices=Race.choices)
    ethnicity = models.IntegerField(
        _("5.2. Ethnicity"), choices=Ethnicity.choices)
    email_yn = models.IntegerField(
        _("13. Do you have an e-mail address?"), choices=YesNo.choices)
    email = models.EmailField(_("Email address"), max_length=254, blank=True)
    created_at = models.DateTimeField(_("Created at:"), auto_now_add=True)
    class Meta:
        unique_together = (('name_first', 'name_last', 'dob', 'phone1'))

    def __str__(self):
        return '{} {}'.format(self.name_last, self.name_first)