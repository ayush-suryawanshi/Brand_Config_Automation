import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Brand_Config_Approval_Portal.settings")
django.setup()

from core.models import Scheme



Scheme.objects.all().delete()