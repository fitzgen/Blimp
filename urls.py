from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', "django.views.generic.list_detail.object_list", 
            {queryset: 
                 Post.objects.filter(is_deleted=False,
                                     is_published=True).order_by("-pub_date")},
            name="blimp_index"),
        url(r'^/(?P<object_id>\d+)/$', "django.views.generic.list_detail.object_detail", 
            {queryset: 
                 Post.objects.filter(is_deleted=False,
                                     is_published=True).order_by("-pub_date")},
            name="blimp_detail"),
)
