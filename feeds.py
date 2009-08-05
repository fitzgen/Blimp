from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Post

class RssLatestPosts(Feed):
    title = "Nick Fitzgerald"
    link = "/weblog/"
    description = "Latest posts from fitzgeraldnick.com"

    def items(self):
        return Post.objects.filter(is_published=True,
                                   is_deleted=False).order_by('-pub_date')[:5]
                            
class AtomLatestPosts(RssLatestPosts):
    feed_type = Atom1Feed
    subtitle = RssLatestPosts.description
