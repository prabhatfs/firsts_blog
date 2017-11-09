
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged, SiteRelated
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

from django.contrib.auth.models import AbstractUser

class SiteConfiguration(SiteRelated):
    '''
    A model to edit sitewide content
    '''
    col1_heading = models.CharField(max_length=200, default="About us")
    col1_content = RichTextField()
    col2_heading = models.CharField(max_length=200, default="Useful links")
    col3_heading = models.CharField(max_length=200, default="Follow us on Twitter")
    col3_widget = models.TextField(
        help_text="This is a great place to put something like a twitter widget")
    col4_heading = models.CharField(max_length=200, default="From the Blog")

class HomePage(Page):
    '''
    A page representing the format of the home page
    '''
    features_heading = models.CharField(max_length=200,
        default="Top Image")
    features_heading = models.CharField(max_length=200,
        default="Features")
    customers_heading = models.CharField(max_length=200,
        default="Customers")
    testimonials_heading = models.CharField(max_length=200,
        default="Testimonials")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


SLIDE_TYPE_CHOICES = (
    ('LE', 'Image on left (600x363)'),
    ('RI', 'Image on right (640x363'),
    ('NO', 'No image'),
)

class TopImage(Orderable):
    homepage = models.ForeignKey(HomePage, related_name="top_image")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Slide.image", "gallery"),
        format="Image", max_length=255, null=True, blank=True)

class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    #homepage = models.ForeignKey(HomePage, related_name="slides")
    image_alignment = models.CharField(max_length=2, choices=SLIDE_TYPE_CHOICES,
        default="LE")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=300)
    subheading = models.CharField(max_length=500)
    button_text = models.CharField(max_length=300, blank=True)
    button_link = models.CharField(max_length=2000, blank=True)
    button_icon = models.CharField(max_length=200, blank=True,
        help_text="Name of font awesome 4.0 icon (i.e. fa-arrows). A list "
                    "of icons is at http://fontawesome.io/icons/")


class Feature(Orderable):
    '''
    A section with a picture and content on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="features")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Slide.image", "features"),
        format="Image", max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=100)
    subheading = models.TextField()
    
    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")


class Customer(Orderable):
    '''
    A customer on a home page
    '''
    homepage = models.ForeignKey(HomePage, related_name="customers")
    name = models.CharField(max_length=200,
        help_text="Customers name to use as alt_text for the logo")
    logo = FileField(verbose_name=_("Image"),
        upload_to=upload_to("vital_theme.Slide.image", "clients"),
        format="Image", max_length=255, null=True, blank=True)
    website = models.CharField(max_length=2000, blank=True,
        help_text="If present the logo will link here")


class Testimonial(Orderable):
    '''
    A testimonial on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="testimonials")
    content = models.TextField(help_text="Feel free to include html")
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)


class FAQPage(Page):
    '''
    A page of FAQs
    '''
    content = RichTextField(blank=True)

    class Meta:
        verbose_name = _("FAQ page")
        verbose_name_plural = _("FAQ pages")


class FAQ(Orderable):
    '''
    A FAQ on a FAQ Page
    '''
    faqpage = models.ForeignKey(FAQPage, related_name="faqs")
    question = models.CharField(max_length=300)
    answer = RichTextField()


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")


class PortfolioItem(Page, RichText):
    '''
    An individual portfolio item, should be nested under a Portfolio
    '''
    subtitle = models.CharField(max_length=200, blank=True)
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("theme.PortfolioItem.featured_image", "portfolio"),
        format="Image", max_length=255, null=True, blank=True)
    categories = models.ManyToManyField("PortfolioItemCategory",
                                        verbose_name=_("Categories"),
                                        blank=True,
                                        related_name="portfolioitems")
    href = models.CharField(max_length=2000, blank=True,
        help_text="A link to the finished project (optional)")

    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")


class PortfolioItemImage(Orderable):
    '''
    An image for a PortfolioItem
    '''
    portfolioitem = models.ForeignKey(PortfolioItem, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("theme.PortfolioItemImage.file", "portfolio items"))
    alt_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class PortfolioItemCategory(Slugged):
    """
    A category for grouping portfolio items into a series.
    """

    class Meta:
        verbose_name = _("Portfolio Item Category")
        verbose_name_plural = _("Portfolio Item Categories")
        ordering = ("title",)


