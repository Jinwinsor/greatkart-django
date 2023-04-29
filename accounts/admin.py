from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login',  'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    # Make the password 'READ ONLY'.
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


'''
The filter_horizontal, list_filter, and fieldsets attributes 
are used to customize the layout of the admin form for 
creating or editing user accounts. 
'''

admin.site.register(Account, AccountAdmin)
