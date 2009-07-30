from django.db import models

class Post(models.Model):
    """A blog post or entry or whatever you want to call it."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=False,
                                       blank=True,
                                       null=True)
    is_deleted = models.BooleanField(default=False,
                                     blank=True,
                                     null=True)
    pub_date = models.DateField()
