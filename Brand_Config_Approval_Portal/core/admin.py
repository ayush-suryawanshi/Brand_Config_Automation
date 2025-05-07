from django.contrib import admin 
from .models import *


admin.site.register(Manager)
admin.site.register(Scheme)
admin.site.register(Input_Row)
admin.site.register(Email)
admin.site.register(EmailAttachment)
admin.site.register(Email_Failure_Tracker)

