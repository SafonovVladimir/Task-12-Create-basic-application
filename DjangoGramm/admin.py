from django.contrib import admin
from django.contrib.auth.models import Permission
from django_extensions.admin import ForeignKeyAutocompleteAdmin


class PermissionAdmin(ForeignKeyAutocompleteAdmin):
    # User is your FK attribute in your model
    # first_name and email are attributes to search for in the FK model
    related_search_fields = {
        'user': ('first_name', 'email'),
    }
    fields = ('user', 'avatar', 'is_active')


admin.site.register(Permission, PermissionAdmin)
