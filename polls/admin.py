from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    
    #Change display of the list of questions and stacking them with multiple choices
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    #Customize the admin change list
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #Adding filter for publication date
    list_filter = ['pub_date']

    #Adding search field
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
