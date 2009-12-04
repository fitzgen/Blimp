from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.comments.signals import comment_was_posted
from akismet import Akismet, AkismetError
from django.core.mail import mail_admins
import datetime

class Post(models.Model):
    """A blog post or entry or whatever you want to call it."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.NullBooleanField(default=False,
                                          blank=True,
                                           null=True)
    is_deleted = models.NullBooleanField(default=False,
                                         blank=True,
                                         null=True)
    pub_date = models.DateTimeField()

    def get_absolute_url(self):
        return "".join(["http://fitzgeraldnick.com", reverse("blimp_detail", args=[self.id,])])

    def comments_open(self):
        delta = datetime.date.today() - self.pub_date
        return delta.days < 14

#class Link(models.Model):
#    """A link from Google Reader"""
#    author = models.CharField(max_length=255)
#    content = models.TextField()
#    link = models.URLField(verify_exists=False)
#    pub_date = models.DateField()
#    title = models.CharField(max_length=255)
#
#    def get_absolute_url(self):
#        return self.link


# Signals

def on_comment(sender, comment, request, *args, **kwargs):
    akismet = Akismet(agent="http://fitzgeraldnick.com")
    akismet.setAPIKey(key=settings.AKISMET_API_KEY,
                      blog_url="http://fitzgeraldnick.com/")

    if akismet.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }

        try:
            if akismet.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                comment.is_public = False
                comment.save()

                subject = "New comment marked as spam"
                message = comment.get_as_text()

            else:
                subject = "New comment"
                message = comment.get_as_text()

        except AkismetError, e:
            comment.is_public = False
            comment.save()
            mail_admins("AkismetError, Possibly a spam message, comment not public",
                        comment.get_as_text())
            raise e

    else:
        subject = "Akismet api key verification failed"
        message = subject

    message += "\n\n===============================\n\n%s" % comment.get_as_text()
    mail_admins(subject, message)

comment_was_posted.connect(on_comment)
