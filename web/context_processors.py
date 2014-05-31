from django.conf import settings

def public_settings(request):
    try:
        extra_context = {}
        for s in settings.PUBLIC_SETTINGS:
            extra_context[s] = getattr(settings, s)
        return extra_context
    except:
        return {}
