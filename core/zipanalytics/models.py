from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ZipcodeStats(models.Model):
    zipcode = models.CharField(_("Zip Code"), max_length=6)
    week = models.IntegerField(_("Week Number"))
    cases = models.IntegerField(_("Weekly Cases"))
    tests = models.IntegerField(_("Weekly Tests"))
    deaths = models.IntegerField(_("Weekly Deaths"))

    def __str__(self):
        return '{}-Week{}'.format(self.zipcode, self.week)

    class Meta:
        unique_together = (('zipcode', 'week'))
