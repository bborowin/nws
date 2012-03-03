# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tuple'
        db.create_table('lexer_tuple', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('lexer', ['Tuple'])


    def backwards(self, orm):
        
        # Deleting model 'Tuple'
        db.delete_table('lexer_tuple')


    models = {
        'lexer.tuple': {
            'Meta': {'object_name': 'Tuple'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lexer']
