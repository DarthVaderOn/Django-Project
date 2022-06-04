import re
from tags_app.models import Tag
from django.db.models.signals import post_save
from django.dispatch import receiver
from publication_app.models import Post


@receiver(post_save, sender=Post)
def create_tag(sender, instance, created, *args, **kwargs):
    for tag_name in re.findall(r'#(\w+)', instance.text):
        tag, is_created = Tag.objects.get_or_create(title=tag_name)
        tag.posts.add(instance)

