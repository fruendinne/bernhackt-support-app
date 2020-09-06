from django.contrib import admin

# Register your models here.
from support.models import Flow
from support.models import FlowStep
from support.models import Tag
from support.models import TroubleshootingLogicBlock


admin.site.register(Flow)
admin.site.register(FlowStep)
admin.site.register(Tag)
admin.site.register(TroubleshootingLogicBlock)
