from django.contrib import admin
from .models import PersonalNote
from .models import Note
# Register your models here.

# Allows interface to show specific record fields on Administrative Interface
# Administrator Feature, Not Admin 
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Registering Models reveal on Admin Interface
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
    