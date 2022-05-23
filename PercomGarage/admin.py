from django.contrib import admin
from .models import Client, Intervention, Vehicules, Garage, Employe, User


admin.site.register(Client)
admin.site.register(Intervention)
admin.site.register(Vehicules)
admin.site.register(Garage)
admin.site.register(Employe)
admin.site.register(User)

