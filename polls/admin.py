from django.contrib import admin
from polls.models import Choice, Poll

# Register your models here.

"""
# Original code
admin.site.register(Poll)
"""

"""
# First modification
class PollAdmin(admin.ModelAdmin):
	fields = ('pub_date', 'question')

admin.site.register(Poll, PollAdmin)
"""


"""
# Second modification
## Stacked Inline format
class ChoiceInLine(admin.StackedInline):
	model = Choice
	extra = 3

## List format
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)
"""


# Third modification
## Tabular Inline format
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

## Column format
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [ChoiceInLine]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)