from django.contrib import admin
from apps.profile_.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'age', 'weight', 'height', 'illness',
                    'intolerance', 'goal', 'diet', 'gender')


admin.site.register(Profile, ProfileAdmin)
