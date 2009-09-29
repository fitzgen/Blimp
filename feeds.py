from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Post

from datetime import datetime

class RssLatestPosts(Feed):
    author_name = "Nick Fitzgerald"
    author_email = "fitzgen@gmail.com"
    title = "Nick Fitzgerald"
    link = "http://fitzgeraldnick.com/weblog/"
    description = "Latest posts from fitzgeraldnick.com"

    def items(self):
        return Post.objects.filter(is_published=True,
                                   is_deleted=False).order_by('-pub_date')[:5]

    def item_pubdate(self, item):
        date = item.pub_date
        return datetime(date.year, date.month, date.day)


class AtomLatestPosts(RssLatestPosts):
    feed_type = Atom1Feed
    subtitle = RssLatestPosts.description
