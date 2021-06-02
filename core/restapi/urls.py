from rest_framework import routers
from .restapi import PatientInfoViewset, ScreenViewset

router = routers.DefaultRouter()
router.register('patientinfo', PatientInfoViewset, 'patientinfo')
router.register('screen', ScreenViewset, 'screen')

urlpatterns = router.urls
