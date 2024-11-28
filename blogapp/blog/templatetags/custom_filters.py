from django import template
from blog.models import Repost

register = template.Library()

@register.filter
def has_reposted(user, post):
    return Repost.objects.filter(user=user, post=post).exists()
