# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ParserCmd'
        db.delete_table('dl_parsercmd')

        # Deleting model 'SoupCmd'
        db.delete_table('dl_soupcmd')

        # Adding field 'ExtractCmd.operator'
        db.add_column('dl_extractcmd', 'operator', self.gf('django.db.models.fields.CharField')(max_length=50, null=True), keep_default=False)

        # Adding field 'ExtractCmd.operands'
        db.add_column('dl_extractcmd', 'operands', self.gf('django.db.models.fields.CharField')(max_length=500, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ParserCmd'
        db.create_table('dl_parsercmd', (
            ('extractcmd_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dl.ExtractCmd'], unique=True, primary_key=True)),
            ('operator', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('operands', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('dl', ['ParserCmd'])

        # Adding model 'SoupCmd'
        db.create_table('dl_soupcmd', (
            ('action', self.gf('django.db.models.fields.CharField')(default='findAll', max_length=50)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('extractcmd_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dl.ExtractCmd'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dl', ['SoupCmd'])

        # Deleting field 'ExtractCmd.operator'
        db.delete_column('dl_extractcmd', 'operator')

        # Deleting field 'ExtractCmd.operands'
        db.delete_column('dl_extractcmd', 'operands')


    models = {
        'dl.extractcmd': {
            'Meta': {'object_name': 'ExtractCmd'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.StoryElement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operands': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.Source']"}),
            'target': ('django.db.models.fields.CharField', [], {'default': "'target'", 'max_length': '500'})
        },
        'dl.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url_base': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'dl.story': {
            'Meta': {'object_name': 'Story'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dl.Source']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 7, 23, 7, 9, 483251)'}),
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
