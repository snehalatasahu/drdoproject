from django.contrib import admin
from .models import Post, Picture, RecruitmentPost

# Register your models here.
admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(RecruitmentPost)