# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ParserCmd'
        db.create_table('dl_parsercmd', (
            ('extractcmd_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dl.ExtractCmd'], unique=True, primary_key=True)),
            ('operator', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('operands', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('dl', ['ParserCmd'])

        # Adding model 'SoupCmd'
        db.create_table('dl_soupcmd', (
            ('extractcmd_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dl.ExtractCmd'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dl.Source'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('dl', ['SoupCmd'])

        # Deleting field 'ExtractCmd.source'
        db.delete_column('dl_extractcmd', 'source_id')

        # Deleting field 'ExtractCmd.action'
        db.delete_column('dl_extractcmd', 'action')

        # Deleting field 'ExtractCmd.attribute'
        db.delete_column('dl_extractcmd', 'attribute')

        # Deleting field 'ExtractCmd.tag'
        db.delete_column('dl_extractcmd', 'tag')

        # Adding field 'ExtractCmd.target'
        db.add_column('dl_extractcmd', 'target', self.gf('django.db.models.fields.CharField')(default='target', max_length=500), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'ParserCmd'
        db.delete_table('dl_parsercmd')

        # Deleting model 'SoupCmd'
        db.delete_table('dl_soupcmd')

        # User chose to not deal with backwards NULL issues for 'ExtractCmd.source'
        raise RuntimeError("Cannot reverse this migration. 'ExtractCmd.source' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ExtractCmd.action'
        raise RuntimeError("Cannot reverse this migration. 'ExtractCmd.action' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ExtractCmd.attribute'
        raise RuntimeError("Cannot reverse this migration. 'ExtractCmd.attribute' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ExtractCmd.tag'
        raise RuntimeError("Cannot reverse this migration. 'ExtractCmd.tag' and its values cannot be restored.")

        # Deleting field 'ExtractCmd.target'
        db.delete_column('dl_extractcmd', 'target')


    models = {
        'dl.extractcmd': {
            'Meta': {'object_name': 'ExtractCmd'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.StoryElement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 6, 21, 38, 46, 462608)'}),
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
