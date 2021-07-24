from django.contrib import admin
from .models import User, SelfAssessment
# Register your models here.
admin.site.register([User, SelfAssessment])
