from django.conf.urls.defaults import *

from models import Post
from feeds import RssLatestPosts, AtomLatestPosts

feeds = {
    "latest-atom": AtomLatestPosts,
    "latest-rss": RssLatestPosts,
}

info_dict = {
    "queryset": Post.objects.filter(is_deleted=False,
                                    is_published=True).order_by("-pub_date")
}

urlpatterns = patterns('',
    url(r'^$', "django.views.generic.list_detail.object_list", info_dict, name="blimp_index"),
    url(r'^(?P<object_id>\d+)/$', "django.views.generic.list_detail.object_detail", info_dict, name="blimp_detail"),

    # direct-to-template
    url(r'^contact/$', "django.views.generic.simple.direct_to_template",
        {"template": "Blimp/contact.html"}, name="blimp_contact"),

    # feeds
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # comments
    url(r'^comments/', include('django.contrib.comments.urls')),
)
