
from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from .models import (SiteConfiguration,
                    HomePage, Slide, Feature, Customer, Testimonial,
                    FAQPage, FAQ,
                    Portfolio, PortfolioItem, PortfolioItemImage,
                    PortfolioItemCategory)


admin.site.register(SiteConfiguration, SingletonAdmin)


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class FeatureInline(TabularDynamicInlineAdmin):
    model = Feature


class CustomerInline(TabularDynamicInlineAdmin):
    model = Customer


class TestimonialInline(TabularDynamicInlineAdmin):
    model = Testimonial


class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, FeatureInline, CustomerInline, TestimonialInline)


admin.site.register(HomePage, HomePageAdmin)


class FAQInline(TabularDynamicInlineAdmin):
    model = FAQ


class FAQPageAdmin(PageAdmin):
    inlines = (FAQInline,)


admin.site.register(FAQPage, FAQPageAdmin)


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage
    max_num = 3


class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)


admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
