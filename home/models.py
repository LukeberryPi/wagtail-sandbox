from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    custom_title = models.CharField(max_length=255, help_text="Custom title for the homepage")

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]

class ChildPage(Page):
    custom_title = models.CharField(max_length=255, help_text="Custom title for the child page")

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]
