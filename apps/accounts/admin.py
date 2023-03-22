from django.contrib import admin
from .models import CustomUser
# Register your models here.
# register customuser model
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
        'classes': ('wide',),
        'fields': ('is_staff', 'is_active')

    }),
    )
   
admin.site.register(CustomUser, CustomUserAdmin)
