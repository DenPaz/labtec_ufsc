from django.contrib import admin

from .models import (
    ReservaComputador,
    ReservaKitTablet,
    ReservaMesaTrabalho,
    ReservaOculusVR,
    ReservaSalaReuniao,
    ReservaTablet,
)

admin.site.register(ReservaComputador)
admin.site.register(ReservaTablet)
admin.site.register(ReservaKitTablet)
admin.site.register(ReservaOculusVR)
admin.site.register(ReservaMesaTrabalho)
admin.site.register(ReservaSalaReuniao)
