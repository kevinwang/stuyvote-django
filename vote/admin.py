from vote.models import *
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    list_display = ('osis', 'grade', 'has_voted')

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'total_votes')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('student', 'choice_1', 'choice_2')

admin.site.register(Student, StudentAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote, VoteAdmin)
