from django.contrib import admin
from .models import NewsPost


class NewsPostAdmin(admin.ModelAdmin):
    list_display = (
        'date_posted',
        'title',
    )

    search_fields = [
        'title',
        'content'
    ]


admin.site.register(NewsPost, NewsPostAdmin)
