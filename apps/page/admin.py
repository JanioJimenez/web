# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.page.models import Idiom, Info, Community, Compiler, Profile

admin.site.register(Idiom)
admin.site.register(Info)
admin.site.register(Community)
admin.site.register(Compiler)
admin.site.register(Profile)