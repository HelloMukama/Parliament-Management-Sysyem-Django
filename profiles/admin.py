from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser, Profile


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser

    # Ref: https://www.youtube.com/watch?v=1BeZxMbSZNI
    fieldsets = (
        *UserAdmin.fieldsets, (
                'More than 2 names', {
                'fields': ('middle_name', )
                }
            )
        )

    list_display = [
            'username', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'email', 
            'is_staff', 
            ]
    search_fields = ('first_name', 'last_name', 'is_staff')


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user',
                    'slug',
                    'is_mp',
                    'is_thespeaker',
                    'region_name',
                    # 'district',
                    # 'phone_number',
                    # 'email',
                    'email',
                    # 'timestamp',
                    # 'updated',
                    )
    search_fields = ('user', 'region_name', 'district')


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)
