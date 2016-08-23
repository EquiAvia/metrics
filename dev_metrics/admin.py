from django.contrib import admin
from dev_metrics.models import * 


#Admin Site Config
admin.site.site_header = 'Metrics'

admin.site.register(Team)
admin.site.register(ReportingPeriod)
admin.site.register(CapacityMeasure)
