from django.contrib import admin
from baxter.dl.models import Source, ExtractCmd, Story, StoryElement

admin.site.register(Source)
admin.site.register(ExtractCmd)
admin.site.register(Story)
admin.site.register(StoryElement)
