from django.conf import settings

class MediaUrlMiddleware(object):
    def process_response(self, request, response):
        response.content = response.content.replace("{{ MEDIA_URL }}",
                                                    settings.MEDIA_URL)
        return response
