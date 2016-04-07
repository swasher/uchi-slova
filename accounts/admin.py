from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import CustomizedUser
from slova.models import Slova

class CustomizedUserInline(admin.StackedInline):
    model = CustomizedUser
    can_delete = False
    verbose_name_plural = 'CustomizedUser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomizedUserInline, )



# Re-register UserAdmin
#admin.site.unregister(User)
admin.site.register(CustomizedUser)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Slova)