from django.contrib import admin
from .models import Post, Comments


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title','date_created')


admin.site.register(Post, PostModelAdmin)  
admin.site.register(Comments)  