# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.usuario.models import Country, City, Language, User, Code

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(User)
admin.site.register(Code)
