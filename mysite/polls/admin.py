from django.contrib import admin
from polls.models import Poll, Choice

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

# Register your models here.
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
