from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Register your models here.
class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('email', 'name', 'NimOrNip', 'is_staff', 'is_active')  # Update 'nim' to 'NimOrNip'
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'NimOrNip')}),  # Update 'nim' to 'NimOrNip'
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'NimOrNip', 'is_staff', 'is_active', 'is_superuser')}  # Update 'nim' to 'NimOrNip'
        ),
    )
    search_fields = ('email', 'name', 'NimOrNip')  # Update 'nim' to 'NimOrNip'
    ordering = ('email',)

admin.site.register(MyUser, MyUserAdmin)
