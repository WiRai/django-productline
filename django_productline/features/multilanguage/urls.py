def introduce_get_multilang_urls():

    def get_multilang_urls():
        return []

    return get_multilang_urls


def refine_get_urls(original):

    def get_urls():
        from django_productline.urls import get_multilang_urls
        from django.conf.urls.i18n import i18n_patterns
        from django.conf import settings
        return original() + i18n_patterns(*get_multilang_urls(), prefix_default_language=settings.PREFIX_DEFAULT_LANGUAGE)

    return get_urls
