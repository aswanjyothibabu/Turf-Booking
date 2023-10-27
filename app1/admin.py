from django.contrib import admin
from .models import ClientUser,Booking
# Register your models here.

admin.site.register(ClientUser)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','Game','Date_Time','Time_Needed')
admin.site.register(Booking,BookingAdmin)