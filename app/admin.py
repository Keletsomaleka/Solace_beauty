from django.contrib import admin
from .models import Technician,Category,Appointment

# Register your models here.
admin.site.register(Technician)
admin.site.register(Category)
admin.site.register(Appointment)