# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileInLine(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = "UserProfiles"

class UserAdmin(BaseUserAdmin):
	inlines = (UserProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
