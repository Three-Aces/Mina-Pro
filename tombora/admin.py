from django.contrib import admin
from .models import Member


# Register your models here.
# admin.site.register(Members)

@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ('username', 'user_email', 'registered_on')
    list_filter = ('username', 'registered_on')
    search_fields = ('username', 'user_email')
