# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'parent_vendor'
        db.create_table('furniture_parent_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('furniture', ['parent_vendor'])

        # Adding model 'vendor'
        db.create_table('furniture_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('multy', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('shipping', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('furniture', ['vendor'])

        # Adding model 'item'
        db.create_table('furniture_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('list', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cost', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['furniture.vendor'])),
        ))
        db.send_create_signal('furniture', ['item'])

        # Adding model 'salestax'
        db.create_table('furniture_salestax', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('furniture', ['salestax'])

        # Adding model 'catalogue'
        db.create_table('furniture_catalogue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['furniture.vendor'])),
        ))
        db.send_create_signal('furniture', ['catalogue'])

        # Adding model 'contact'
        db.create_table('furniture_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['furniture.parent_vendor'])),
        ))
        db.send_create_signal('furniture', ['contact'])


    def backwards(self, orm):
        # Deleting model 'parent_vendor'
        db.delete_table('furniture_parent_vendor')

        # Deleting model 'vendor'
        db.delete_table('furniture_vendor')

        # Deleting model 'item'
        db.delete_table('furniture_item')

        # Deleting model 'salestax'
        db.delete_table('furniture_salestax')

        # Deleting model 'catalogue'
        db.delete_table('furniture_catalogue')

        # Deleting model 'contact'
        db.delete_table('furniture_contact')


    models = {
        'furniture.catalogue': {
            'Meta': {'object_name': 'catalogue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['furniture.vendor']"})
        },
        'furniture.contact': {
            'Meta': {'object_name': 'contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['furniture.parent_vendor']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'furniture.item': {
            'Meta': {'object_name': 'item'},
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['furniture.vendor']"})
        },
        'furniture.parent_vendor': {
            'Meta': {'object_name': 'parent_vendor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'furniture.salestax': {
            'Meta': {'object_name': 'salestax'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'furniture.vendor': {
            'Meta': {'object_name': 'vendor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multy': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'shipping': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['furniture']