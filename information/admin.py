from django.contrib import admin
from .models import StudentInformation, ExtendedInformation

# Register your models here.
admin.site.register(StudentInformation)
admin.site.register(ExtendedInformation)
