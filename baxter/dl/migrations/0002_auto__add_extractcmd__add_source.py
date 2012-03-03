# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ExtractCmd'
        db.create_table('dl_extractcmd', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dl.Source'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('dl', ['ExtractCmd'])

        # Adding model 'Source'
        db.create_table('dl_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_base', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('dl', ['Source'])


    def backwards(self, orm):
        
        # Deleting model 'ExtractCmd'
        db.delete_table('dl_extractcmd')

        # Deleting model 'Source'
        db.delete_table('dl_source')


    models = {
        'dl.extractcmd': {
            'Meta': {'object_name': 'ExtractCmd'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'data': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.Source']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dl.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url_base': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'dl.story': {
            'Meta': {'object_name': 'Story'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 3, 10, 37, 52, 35352)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dl']
