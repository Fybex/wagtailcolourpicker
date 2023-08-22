from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page


class BasicPage(Page):

    body = StreamField([
        ('rich_text', RichTextBlock())
    ])

    # show in menu ticked by default
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
