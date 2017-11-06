# firsts_blog
firstsynch blog in mezzanine



I have put on TopImage model in theme model file and slide has been removed, for this 
i had to remove only foreign field of home page in Slide Model.




Now i need to integrate blog in that page 

and the top menu should be integrated with categories




I need to modify below file to right new function for blog post
mezzanine/mezzanine/blog/templatetags/blog_tags.py

I need to put code for home page with blog_tags and 
for different categories , i need to setup separate module.


Like below i need to perform the task,

<div><!-- Recent Posts -->
{% load blog_tags keyword_tags i18n %}
{% blog_recent_posts 5 as recent_posts %}
{% if recent_posts %}
<h2>Recent Articles <span class="amp">&amp;</span> Ruminations</h2>
{% for recent_post in recent_posts %}
<h3><a href="{{ recent_post.get_absolute_url }}"
{{ recent_post.title }}</a></h3>
<h4>{{ recent_post.publish_date|timesince }} {% trans "ago" %}</h4>
<div class="recent-summary">
{{ recent_post.description_from_content|safe|typogrify }}

<a href="{{ recent_post.get_absolute_url }}" class="label
label-inverse">{% trans "read more&hellip;" %}</a>
<hr>
</div><!-- /recent-summary -->
{% endfor %}
{% endif %}
</div><!-- /Recent Posts -->



