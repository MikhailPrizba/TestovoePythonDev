from django.db import models
from user.models import User
from django_enum import TextChoices


class Link(models.Model):
    class LinkTypesChoices(TextChoices):
        WEBSITE = "website"
        BOOK = "book"
        ARTICLE = "article"
        MUSIC = "music"
        VIDEO = "video"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()
    image_url = models.URLField(blank=True)
    link_type = models.TextField(
        choices=LinkTypesChoices.choices, default=LinkTypesChoices.WEBSITE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("user", "url")
