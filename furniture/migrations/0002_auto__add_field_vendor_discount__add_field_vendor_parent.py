# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'vendor.discount'
        db.add_column('furniture_vendor', 'discount',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'vendor.parent'
        db.add_column('furniture_vendor', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['furniture.parent_vendor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'vendor.discount'
        db.delete_column('furniture_vendor', 'discount')

        # Deleting field 'vendor.parent'
        db.delete_column('furniture_vendor', 'parent_id')


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
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multy': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['furniture.parent_vendor']"}),
            'shipping': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['furniture']