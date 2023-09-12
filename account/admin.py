from django.contrib import admin
from .models import UserAccount, Roles
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput)


    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'third_name', 'roles')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'third_name', 'roles', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial['password']




class UserResource(resources.ModelResource):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'third_name', 'is_active', 'is_staff', 'roles')


class UserAdmins(ImportExportModelAdmin, BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'third_name', 'roles', 'is_active', 'is_staff']
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Pesonal_info", {
            'fields':['phone_number', 'first_name', 'last_name', 'third_name']
            }),
        ("Permissions", {
            'fields':['roles', 'is_staff']
            }),

    ]
    add_fieldsets = [
        (
            None,
            {
                "classes":["wide"],
                "fields": ['username', 'email', "password1", "password2", 'phone_number', 'first_name', 'last_name', 'third_name', 'roles', 'is_active', 'is_staff'],
            },
        ),
    ]
    list_display_links = ('username',)
    search_fields = ('id', 'email', 'phone_number',)
    # filter_horizontal = ('roles',)
    resource_class = UserResource
    pass


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_roles')
    list_display_link = ('id', 'name_of_roles')




admin.site.register(UserAccount, UserAdmins)
admin.site.register(Roles, RolesAdmin)
admin.site.unregister(Group)
# admin.site.register(CodesForUser)