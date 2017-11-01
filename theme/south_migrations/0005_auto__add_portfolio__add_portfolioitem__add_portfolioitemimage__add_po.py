# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portfolio'
        db.create_table(u'theme_portfolio', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'theme', ['Portfolio'])

        # Adding model 'PortfolioItem'
        db.create_table(u'theme_portfolioitem', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItem'])

        # Adding M2M table for field categories on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'theme_portfolioitem_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'theme.portfolioitem'], null=False)),
            ('portfolioitemcategory', models.ForeignKey(orm[u'theme.portfolioitemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfolioitemcategory_id'])

        # Adding model 'PortfolioItemImage'
        db.create_table(u'theme_portfolioitemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('portfolioitem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['theme.PortfolioItem'])),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
            ('alt_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemImage'])

        # Adding model 'PortfolioItemCategory'
        db.create_table(u'theme_portfolioitemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemCategory'])


    def backwards(self, orm):
        # Deleting model 'Portfolio'
        db.delete_table(u'theme_portfolio')

        # Deleting model 'PortfolioItem'
        db.delete_table(u'theme_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'theme_portfolioitem_categories'))

        # Deleting model 'PortfolioItemImage'
        db.delete_table(u'theme_portfolioitemimage')

        # Deleting model 'PortfolioItemCategory'
        db.delete_table(u'theme_portfolioitemcategory')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.customer': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Customer'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customers'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'})
        },
        u'theme.faq': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'FAQ'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'answer': ('mezzanine.core.fields.RichTextField', [], {}),
            'faqpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'faqs'", 'to': u"orm['theme.FAQPage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'theme.faqpage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'FAQPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.feature': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Feature'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'features'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subheading': ('django.db.models.fields.TextField', [], {})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'customers_heading': ('django.db.models.fields.CharField', [], {'default': "'Customers'", 'max_length': '200'}),
            'features_heading': ('django.db.models.fields.CharField', [], {'default': "'Features'", 'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'testimonials_heading': ('django.db.models.fields.CharField', [], {'default': "'Testimonials'", 'max_length': '200'})
        },
        u'theme.portfolio': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Portfolio', '_ormbases': [u'pages.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.portfolioitem': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'PortfolioItem', '_ormbases': [u'pages.Page']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portfolioitems'", 'blank': 'True', 'to': u"orm['theme.PortfolioItemCategory']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.portfolioitemcategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'PortfolioItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'theme.portfolioitemimage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'PortfolioItemImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolioitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['theme.PortfolioItem']"})
        },
        u'theme.slide': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'button_icon': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'button_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'button_text': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_alignment': ('django.db.models.fields.CharField', [], {'default': "'LE'", 'max_length': '2'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'theme.testimonial': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Testimonial'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'testimonials'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']