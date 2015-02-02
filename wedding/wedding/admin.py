from django.contrib import admin

from core.models import Guest, GuestPost

class GuestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guest, GuestAdmin)

class GuestPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(GuestPost, GuestPostAdmin)