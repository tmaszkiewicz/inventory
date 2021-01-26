from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(machine)
admin.site.register(svr)
admin.site.register(user)
admin.site.register(windowsLicense)
admin.site.register(windowsSvrLicense)
admin.site.register(officeLicense)
admin.site.register(term)
admin.site.register(termShift)
admin.site.register(foamFile)
admin.site.register(foamRow)
admin.site.register(message)
admin.site.register(lastRefresh)
