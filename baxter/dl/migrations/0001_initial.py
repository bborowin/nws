# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Story'
        db.create_table('dl_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 3, 3, 10, 28, 2, 107130))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('html', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dl', ['Story'])


    def backwards(self, orm):
        
        # Deleting model 'Story'
        db.delete_table('dl_story')


    models = {
        'dl.story': {
            'Meta': {'object_name': 'Story'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 3, 10, 28, 2, 107130)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dl']
