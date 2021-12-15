from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class UserAdmin(UserAdmin):
    fieldsets = (
        ('System_credentials', {'fields':('username', 'password', 'email')}),
        ('Personal_info', {'fields': ('first_name',  'last_name')}),
        # ('Permissions', {'fields':('user_type')})
    )
    list_display = ['username',]

admin.site.register(User,UserAdmin)