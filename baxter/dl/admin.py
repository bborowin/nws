from django.contrib import admin
from baxter.dl.models import Source, Story, StoryElement, ExtractCmd, SoupCmd, ParserCmd

admin.site.register(Source)
admin.site.register(Story)
admin.site.register(StoryElement)
admin.site.register(SoupCmd)
admin.site.register(ParserCmd)
