from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post


def post_detail(request, object_id, *args, **kwargs):
    context = {}
    post = context["object"] = get_object_or_404(Post, pk=object_id)

    try:
        next_post = Post.objects.filter(is_deleted=False,
                                        is_published=True,
                                        pub_date__gt=post.pub_date).order_by("-pub_date")[0]
        context["next_post"] = next_post
    except IndexError:
        pass

    try:
        prev_post = Post.objects.filter(is_deleted=False,
                                        is_published=True,
                                        pub_date__lt=post.pub_date).order_by("-pub_date")[0]
        context["prev_post"] = prev_post
    except IndexError:
        pass

    return render_to_response("Blimp/post_detail.html",
                              context,
                              context_instance=RequestContext(request))
