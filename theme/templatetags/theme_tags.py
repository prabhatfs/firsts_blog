
from mezzanine import template
from mezzanine.utils.sites import current_site_id

from theme.models import SiteConfiguration

register = template.Library()


@register.as_tag
def get_site_conf():
    """
    Adds the `SiteConfiguration` to the context
    """
    return SiteConfiguration.objects.get_or_create(site_id=current_site_id())[0]

@register.as_tag
def blog_ranges(l):
	return range(3,len(l),3)

def blog_lookup(d, key):
	return d[key]

def blog_slice(d,start):
	if len(d) > start + 3:
		return d[start:start+3]
	else:
		return d[start:]

register.filter('blog_lookup', blog_lookup)
register.filter('blog_slice', blog_slice)