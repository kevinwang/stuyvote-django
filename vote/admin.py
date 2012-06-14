from vote.models import *
from django.contrib import admin

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'can_choose_two_candidates')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('osis', 'grade')

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'election', 'total_votes')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('student', 'election', 'choice_1', 'choice_2')

admin.site.register(Election, ElectionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote, VoteAdmin)
