# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('name', models.CharField(help_text=b'Customers name to use as alt_text for the logo', max_length=200)),
                ('logo', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('website', models.CharField(help_text=b'If present the logo will link here', max_length=2000, blank=True)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('question', models.CharField(max_length=300)),
                ('answer', mezzanine.core.fields.RichTextField()),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'FAQ page',
                'verbose_name_plural': 'FAQ pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('heading', models.CharField(max_length=100)),
                ('subheading', models.TextField()),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('features_heading', models.CharField(default=b'Features', max_length=200)),
                ('customers_heading', models.CharField(default=b'Customers', max_length=200)),
                ('testimonials_heading', models.CharField(default=b'Testimonials', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('subtitle', models.CharField(max_length=200, blank=True)),
                ('featured_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Featured Image', blank=True)),
                ('href', models.CharField(help_text=b'A link to the finished project (optional)', max_length=2000, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio item',
                'verbose_name_plural': 'Portfolio items',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='PortfolioItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Portfolio Item Category',
                'verbose_name_plural': 'Portfolio Item Categories',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('alt_text', models.CharField(max_length=200, blank=True)),
                ('portfolioitem', models.ForeignKey(related_name='images', to='theme.PortfolioItem')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('col1_heading', models.CharField(default=b'About us', max_length=200)),
                ('col1_content', mezzanine.core.fields.RichTextField()),
                ('col2_heading', models.CharField(default=b'Useful links', max_length=200)),
                ('col3_heading', models.CharField(default=b'Follow us on Twitter', max_length=200)),
                ('col3_widget', models.TextField(help_text=b'This is a great place to put something like a twitter widget')),
                ('col4_heading', models.CharField(default=b'From the Blog', max_length=200)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image_alignment', models.CharField(default=b'LE', max_length=2, choices=[(b'LE', b'Image on left (600x363)'), (b'RI', b'Image on right (640x363'), (b'NO', b'No image')])),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('heading', models.CharField(max_length=300)),
                ('subheading', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=300, blank=True)),
                ('button_link', models.CharField(max_length=2000, blank=True)),
                ('button_icon', models.CharField(help_text=b'Name of font awesome 4.0 icon (i.e. fa-arrows). A list of icons is at http://fontawesome.io/icons/', max_length=200, blank=True)),
                ('homepage', models.ForeignKey(related_name='slides', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('content', models.TextField(help_text=b'Feel free to include html')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('homepage', models.ForeignKey(related_name='testimonials', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='categories',
            field=models.ManyToManyField(related_name='portfolioitems', verbose_name='Categories', to='theme.PortfolioItemCategory', blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='homepage',
            field=models.ForeignKey(related_name='features', to='theme.HomePage'),
        ),
        migrations.AddField(
            model_name='faq',
            name='faqpage',
            field=models.ForeignKey(related_name='faqs', to='theme.FAQPage'),
        ),
        migrations.AddField(
            model_name='customer',
            name='homepage',
            field=models.ForeignKey(related_name='customers', to='theme.HomePage'),
        ),
    ]
