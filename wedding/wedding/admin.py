from django.contrib import admin

from wedding.models import Guest, GuestPost

class GuestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guest, GuestAdmin)

class GuestPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(GuestPost, GuestPostAdmin)