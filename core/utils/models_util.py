from django.db import models
from django.utils.translation import gettext as _

def compute_eligibility(form):
    data = form.cleaned_data
    # User is ineligible if meets any of the following criteria
    if(data['screen_smoking_yn'] == 0 or 
        data['screen_smoking_amount'] or 
        data['screen_diabetes_yn'] == 1 or
        data['screen_lungcancer_yn'] == 1 or
        data['screen_hx_atrialfibrillation_yn'] == 1 or 
        data['screen_dx_additional_yn'] == 1 or 
        data['screen_treatment_bph_yn'] == 0):
        return "not_eligible"
    return "eligible"
    
# Options for Yes/No questions
class YesNo(models.IntegerChoices):
    NO = 0, _("No")
    YES = 1, _("Yes")

# Options for Gender
class Gender(models.IntegerChoices):
    Male = 1, _("Male")
    Female = 2, _("Female")
    Refused = 3, _("Refused")

# Phone Type
class Phone1Type(models.IntegerChoices):
    Landline = 1, _("Landline")
    Cell = 2, _("Cell")


class Phone2Type(models.IntegerChoices):
    Home = 1, _("Home")
    Cell = 2, _("Cell")

# Time Merediem AM/PM
class TimeMerediem(models.IntegerChoices):
    AM = 1, _("AM")
    PM = 2, _("PM")

# Recruitment sources
class RecruitmentSources(models.IntegerChoices):
    facebook = 1, _("Facebook")
    instagram = 2, _("Instagram")
    email = 3, _("Email")
    flyers = 4, _("Flyers")
    craigslist = 5, _("Craigslist")
    referral = 6, _("Referral")
    other = 99, _("Other")

# Race
class Race(models.IntegerChoices):
    native = 1, _("American Indian/Alaskan Native")
    asian = 2, _("Asian")
    black = 3, _("Black/African American")
    hawaii = 4, _("Native Hawaiian/Pacific Islander")
    white = 5, _("Whtie")
    other = 6, _("Other")
    unknown = 7, _("Unknown")

# Ethnicity
class Ethnicity(models.IntegerChoices):
    hispanic = 1, _("Hispanic/Latino")
    not_hispanic = 2, _("Not Hispanic/Latino")
    unknown = 3, _("Unknown")

# United States List
class States(models.IntegerChoices):
    illinois = 13, _("Illinois")
    alabama = 1, _("Alabama")
    alaska = 2, _("Alaska")
    arizona = 3, _("Arizona")
    arkansas = 4, _("Arkansas")
    california = 5, _("California")
    colorado = 6, _("Colorado")
    connecticut = 7, _("Connecticut")
    delaware = 8, _("Delaware")
    florida = 9, _("Florida")
    georgia = 10, _("Georgia")
    hawaii = 11, _("Hawaii")
    idaho = 12, _("Idaho")
    indiana = 14, _("Indiana")
    iowa = 15, _("Iowa")
    kansas = 16, _("Kansas")
    kentucky = 17, _("Kentucky")
    louisiana = 18, _("Louisiana")
    maine = 19, _("Maine")
    maryland = 20, _("Maryland")
    massachusetts = 21, _("Massachusetts")
    michigan = 22, _("Michigan")
    minnesota = 23, _("Minnesota")
    mississippi = 24, _("Mississippi")
    missouri = 25, _("Missouri")
    montana = 26, _("Montana")
    nebraska = 27, _("Nebraska")
    nevada = 28, _("Nevada")
    newhampshire = 29, _("New Hampshire")
    newjersey = 30, _("New Jersey")
    newmexico = 31, _("New Mexico")
    newyork = 32, _("New York")
    northcarolina = 33, _("North Carolina")
    northdakota = 34, _("North Dakota")
    ohio = 35, _("Ohio")
    oklahoma = 36, _("Oklahoma")
    oregon = 37, _("Oregon")
    pennsylvania = 38, _("Pennsylvania")
    rhodeisland = 39, _("Rhode Island")
    southcarolina = 40, _("South Carolina")
    southdakota = 41, _("South Dakota")
    tennessee = 42, _("Tennessee")
    texas = 43, _("Texas")
    utah = 44, _("Utah")
    vermont = 45, _("Vermont")
    virginia = 46, _("Virginia")
    washington = 47, _("Washington")
    westvirginia = 48, _("West Virginia")
    wisconsin = 49, _("Wisconsin")
    wyoming = 50, _("Wyoming")
