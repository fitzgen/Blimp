from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('title', 'is_published',
                    'is_deleted', 'pub_date')
    list_filter = ('is_published', 'is_deleted', 'pub_date')
    save_on_top = True
    search_fields = ('title','content')
admin.site.register(Post, PostAdmin)
