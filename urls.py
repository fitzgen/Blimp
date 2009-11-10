from django.conf.urls.defaults import *

from feeds import RssLatestPosts, AtomLatestPosts
from models import Post
from views import post_detail

feeds = {
    "latest-atom": AtomLatestPosts,
    "latest-rss": RssLatestPosts,
}

info_dict = {
    "queryset": Post.objects.filter(is_deleted=False,
                                    is_published=True).order_by("-pub_date")
}

list_dict = {
        "queryset": info_dict["queryset"][:10],
        "extra_context": {"short": True},
}
list_dict.update(info_dict)

urlpatterns = patterns('',
    url(r'^$', "django.views.generic.list_detail.object_list", list_dict, name="blimp_index"),
    url(r'^(?P<object_id>\d+)/$', post_detail, name="blimp_detail"),

    # direct-to-template
    url(r'^contact/$', "django.views.generic.simple.direct_to_template",
        {"template": "Blimp/contact.html"}, name="blimp_contact"),

    # feeds
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # comments
    url(r'^comments/', include('django.contrib.comments.urls')),
)
