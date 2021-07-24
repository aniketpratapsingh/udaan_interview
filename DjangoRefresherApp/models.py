from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255, null=False)
    mobile_number=models.CharField(max_length=11, null=False)
    pin_code=models.CharField(max_length=8, null=False)
    is_admin=models.BooleanField(default=False, null=False)
    covid_status=models.CharField(max_length=20, default='not_tested', null=False)

class SelfAssessment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.CharField(max_length=20, null=False)
    travel_history =  models.BooleanField(null=False)
    covid_contact = models.BooleanField(null=False)

