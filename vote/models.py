from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from itertools import chain

class Election(models.Model):
    name = models.CharField(max_length=200)
    grade = models.IntegerField()
    can_choose_two_candidates = models.BooleanField()

    can_choose_two_candidates.boolean = True;

    def __unicode__(self):
        return self.name;

class Student(models.Model):
    osis = models.IntegerField()
    grade = models.IntegerField()

    def has_available_elections(self):
        for election in Election.objects.filter(grade=0):
            if not self.has_voted_in_election(election):
                return True
        for election in Election.objects.filter(grade=self.grade):
            if not self.has_voted_in_election(election):
                return True
        return False

    def has_voted_in_election(self, election):
        return Vote.objects.filter(election=election).count() > 0

    def __unicode__(self):
        return str(self.osis)

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    election = models.ForeignKey(Election)

    def total_votes(self):
        return Vote.objects.filter(choice_1=self).count() + Vote.objects.filter(choice_2=self).count()

    def __unicode__(self):
        return self.name

class Vote(models.Model):
    student = models.ForeignKey(Student)
    election = models.ForeignKey(Election)
    choice_1 = models.ForeignKey(Candidate, related_name='vote_choice_1')
    choice_2 = models.ForeignKey(Candidate, related_name='vote_choice_2', blank=True, null=True)

    def clean(self):
        if self.election.grade != 0 and self.student.grade != self.election.grade:
            raise ValidationError('Student cannot vote in this election.')
        if self.choice_1 == self.choice_2:
            self.choice_2 = None
        if self.choice_1.election != self.election or self.choice_2 is not None and self.choice_2.election != self.election:
            raise ValidationError('One or more selected candidates do not correspond with this election.')

    def __unicode__(self):
        return self.student.__unicode__() + ': ' + self.choice_1.__unicode__() + (', ' + self.choice_2.__unicode__() if self.choice_2 != None else '')

class VoteForm(ModelForm):
    class Meta:
        model = Vote
