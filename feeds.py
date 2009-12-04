from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Post

from datetime import datetime

class RssLatestPosts(Feed):
    author_name = "Nick Fitzgerald"
    author_email = "fitzgen@gmail.com"
    author_link = "http://fitzgeraldnick.com/"
    title = "Nick Fitzgerald"
    link = "http://fitzgeraldnick.com/weblog/"
    description = "Latest entries from fitzgeraldnick.com/weblog/"
    copyright = "Copyright (c) 2009, Nick Fitzerald"
    item_author_name = "Nick Fitzgerald"
    item_author_email = "fitzgen@gmail.com"
    item_author_link = "http://fitzgeraldnick.com/"

    def items(self):
        return Post.objects.filter(is_published=True,
                                   is_deleted=False).order_by('-pub_date')[:5]

    def item_pubdate(self, item):
        return item.pub_date


class AtomLatestPosts(RssLatestPosts):
    feed_type = Atom1Feed
    subtitle = RssLatestPosts.description
