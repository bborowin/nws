# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StoryElement'
        db.create_table('dl_storyelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('dl', ['StoryElement'])

        # Deleting field 'ExtractCmd.data'
        db.delete_column('dl_extractcmd', 'data')

        # Adding field 'ExtractCmd.element'
        db.add_column('dl_extractcmd', 'element', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['dl.StoryElement']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'StoryElement'
        db.delete_table('dl_storyelement')

        # Adding field 'ExtractCmd.data'
        db.add_column('dl_extractcmd', 'data', self.gf('django.db.models.fields.CharField')(default='<none>', max_length=250), keep_default=False)

        # Deleting field 'ExtractCmd.element'
        db.delete_column('dl_extractcmd', 'element_id')


    models = {
        'dl.extractcmd': {
            'Meta': {'object_name': 'ExtractCmd'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.StoryElement']"}),
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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.Source']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 3, 17, 35, 24, 716257)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'dl.storyelement': {
            'Meta': {'object_name': 'StoryElement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['dl']
