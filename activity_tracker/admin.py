from django.contrib import admin

# Register your models here.
from .models import Activity, Athlete

admin.site.register(Activity)
admin.site.register(Athlete)