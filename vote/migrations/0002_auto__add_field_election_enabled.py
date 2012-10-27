# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Election.enabled'
        db.add_column('vote_election', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Election.enabled'
        db.delete_column('vote_election', 'enabled')


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
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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