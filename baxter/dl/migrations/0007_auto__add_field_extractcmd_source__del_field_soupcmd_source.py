# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ExtractCmd.source'
        db.add_column('dl_extractcmd', 'source', self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['dl.Source']), keep_default=False)

        # Deleting field 'SoupCmd.source'
        db.delete_column('dl_soupcmd', 'source_id')


    def backwards(self, orm):
        
        # Deleting field 'ExtractCmd.source'
        db.delete_column('dl_extractcmd', 'source_id')

        # User chose to not deal with backwards NULL issues for 'SoupCmd.source'
        raise RuntimeError("Cannot reverse this migration. 'SoupCmd.source' and its values cannot be restored.")


    models = {
        'dl.extractcmd': {
            'Meta': {'object_name': 'ExtractCmd'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.StoryElement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.Source']"}),
            'target': ('django.db.models.fields.CharField', [], {'default': "'target'", 'max_length': '500'})
        },
        'dl.parsercmd': {
            'Meta': {'object_name': 'ParserCmd', '_ormbases': ['dl.ExtractCmd']},
            'extractcmd_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dl.ExtractCmd']", 'unique': 'True', 'primary_key': 'True'}),
            'operands': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dl.soupcmd': {
            'Meta': {'object_name': 'SoupCmd', '_ormbases': ['dl.ExtractCmd']},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'extractcmd_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dl.ExtractCmd']", 'unique': 'True', 'primary_key': 'True'}),
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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 6, 21, 41, 24, 833888)'}),
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
