from django.contrib import admin
from .models import PostQuery
from .models import PostComment

# Register your models here.
admin.site.register(PostQuery)
admin.site.register(PostComment)
