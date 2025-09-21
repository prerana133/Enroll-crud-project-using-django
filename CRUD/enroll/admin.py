from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
    ordering=('id',)
    list_editable=('name','email')
    readonly_fields=('id',)

