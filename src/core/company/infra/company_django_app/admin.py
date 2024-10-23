from django.contrib import admin

from .models import Company, Contract, Employee

admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Employee)
