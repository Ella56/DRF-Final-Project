from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Reply)