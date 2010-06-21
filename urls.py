from django.conf.urls.defaults import *

from feeds import AtomLatestPosts
from models import Post
from views import post_detail

feeds = {
    "latest-atom": AtomLatestPosts,
}

info_dict = {
    "queryset": Post.objects.filter(is_deleted=False,
                                    is_published=True).order_by("-pub_date"),
}

list_dict = {
    "paginate_by": 5,
}
list_dict.update(info_dict)

# Old urls that need to redirect to new places.
legacy_urls = (
    (r"^feeds/latest-rss/$", "/weblog/feeds/latest-atom/"),
)

urlpatterns = patterns("")

for old, new in legacy_urls:
    urlpatterns += patterns("",
                            (old,
                             'django.views.generic.simple.redirect_to',
                             {'url': new }))

urlpatterns += patterns('',
    url(r'^$', "django.views.generic.list_detail.object_list", list_dict, name="blimp_index"),
    url(r'^(?P<object_id>\d+)/$', post_detail, name="blimp_detail"),

    # direct-to-template
    url(r'^contact/$', "django.views.generic.simple.direct_to_template",
        {"template": "Blimp/contact.html"}, name="blimp_contact"),

    # feeds
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # comments
    # url(r'^comments/', include('django.contrib.comments.urls')),
)
