# yourapp/templatetags/hreflang_tags.py
from django import template
from django.utils.translation import get_language
from django.urls import reverse

register = template.Library()

@register.simple_tag
def hreflang_links(request):
    LANGUAGES = [
        ('en-us', 'English (US)'),
        ('fr', 'French'),
        ('de', 'German'),
        ('da', 'Danish'),
        ('pt', 'Portuguese'),
        ('nl', 'Dutch'),
        ('es', 'Spanish'),
    ]

    hreflang_tags = []
    current_path = request.path

    # Balise x-default
    hreflang_tags.append(
        f'<link rel="alternate" hreflang="x-default" href="https://www.lightmeet.fr{current_path}" />'
    )

    # Balises hreflang pour chaque langue
    for lang_code, lang_name in LANGUAGES:
        href = f'https://www.lightmeet.fr/{lang_code}{current_path}'
        hreflang_tags.append(
            f'<link rel="alternate" hreflang="{lang_code}" href="{href}" />'
        )

    return '\n'.join(hreflang_tags)
