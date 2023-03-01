from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('fullName','user','userType','username','status')
    # ordering: 
    search_fields=('fullName','userType','username','status')

admin.site.register(Product)

admin.site.register(BorderRegistration)