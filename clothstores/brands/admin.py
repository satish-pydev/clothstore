from django.contrib import admin
from .models import customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display =['name','add']
admin.site.register(customer,CustomerAdmin)
