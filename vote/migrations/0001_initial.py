# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Election'
        db.create_table('vote_election', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grade', self.gf('django.db.models.fields.IntegerField')()),
            ('can_choose_two_candidates', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('vote', ['Election'])

        # Adding model 'Student'
        db.create_table('vote_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osis_digest', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('grade', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('vote', ['Student'])

        # Adding model 'Candidate'
        db.create_table('vote_candidate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.Election'])),
        ))
        db.send_create_signal('vote', ['Candidate'])

        # Adding model 'Vote'
        db.create_table('vote_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.Student'])),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.Election'])),
            ('choice_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vote_choice_1', to=orm['vote.Candidate'])),
            ('choice_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='vote_choice_2', null=True, to=orm['vote.Candidate'])),
            ('time_voted', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('vote', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Election'
        db.delete_table('vote_election')

        # Deleting model 'Student'
        db.delete_table('vote_student')

        # Deleting model 'Candidate'
        db.delete_table('vote_candidate')

        # Deleting model 'Vote'
        db.delete_table('vote_vote')


    models = {
        'vote.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vote.election': {
            'Meta': {'object_name': 'Election'},
            'can_choose_two_candidates': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vote.student': {
            'Meta': {'object_name': 'Student'},
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'osis_digest': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'vote.vote': {
            'Meta': {'object_name': 'Vote'},
            'choice_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vote_choice_1'", 'to': "orm['vote.Candidate']"}),
            'choice_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'vote_choice_2'", 'null': 'True', 'to': "orm['vote.Candidate']"}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.Student']"}),
            'time_voted': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['vote']