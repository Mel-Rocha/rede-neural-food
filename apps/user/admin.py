from django.contrib import admin
from apps.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'name', 'age', 'weight', 'height', 'illness',
                    'intolerance', 'goal', 'diet', 'gender')


admin.site.register(User, UserAdmin)
