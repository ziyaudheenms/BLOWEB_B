from django.contrib import admin
from .models import Blog , Category , Like , Profile ,Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Profile)

admin.site.register(Comment)
