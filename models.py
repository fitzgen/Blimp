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

    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return unicode(self.title)

    def get_absolute_url(self):
        return reverse("blimp_detail", args=[self.id,])

    def comments_open(self):
        delta = datetime.datetime.now() - self.pub_date
        return delta.days < 28
