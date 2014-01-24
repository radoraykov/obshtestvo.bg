# coding=utf-8
# Django settings for mysite project.
from django.utils.datastructures import SortedDict
from server.settings_app import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
SESSION_ENGINE = "django.contrib.sessions.backends.file"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Sofia'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'restful.middleware.HttpMergeParameters',
    'restful.middleware.HttpMethodOverride',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # Before using CSRF make sure it's ONLY enabled when user is logging in or already logged in via cookies
    # Make sure it's not enabled for RESTful requests authenticated via Basic, Digest or OAuth
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'restful.middleware.ResponseFormatDetection',
    'restful.error_handler.ErrorHandler',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'server.wsgi.application'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'restful',
    'web',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

MEMBER_POSITIONS = {
    "design": "дизайн",
    "photography": "фотография",
    "illustrations": "илюстрации",
    "accounting": "счетоводство",
    "law": "юридическа знания",
    "fund gathering": "фондонабиране",
    "code": "код",
    "business analysis": "бизнес анализа",
    "copyright": "копирайт",
    "pr": "PR",
    "marketing": "маркетинг",
    "ideas": "идеи",
    "donation": "дарение",
}

FAKE_DB = SortedDict()
FAKE_DB["openparliament"] = {
    "name": "Отворен Парламент",
    "name_full": "Отворен Парламент",
    "preview": "openparliament.png",
    "fb_group": "https://www.facebook.com/groups/obshtestvo.parlament/",
    "repo": "https://github.com/obshtestvo/rating-gov-representatives",
    "homepage": 1,
    "slug": "openparliament"
}
FAKE_DB["pitaigi"] = {
    "name": "Pitaigi.bg",
    "name_full": "Pitaigi.bg (Питай ги)",
    "url": "http://foi.obshtestvo.bg/",
    "preview": "pitaigi.jpg",
    "fb_group": "https://www.facebook.com/groups/pitaigi.bg/",
    "repo": "https://github.com/obshtestvo/alaveteli-bulgaria",
    "homepage": 2,
    "slug": "pitaigi"
}
FAKE_DB["grada.me"] = {
    "name": "Grada.me",
    "name_full": "Grada.me (Града ми)",
    "url": "http://www.grada.me/",
    "preview": "gradame.jpg",
    "fb_group": "https://www.facebook.com/groups/obshtestvo.reallife.bug.tracker/",
    "repo": "https://github.com/obshtestvo-idei/real-life-bug-tracker",
    "homepage": 3,
    "slug": "grada.me"
}
FAKE_DB["recycle"] = {
    "name": "RE:CYCLE",
    "name_full": "RE:CYCLE",
    "preview": "recycle.jpg",
    "url": "http://recycle.obshtestvo.bg/",
    "fb_group": "https://www.facebook.com/groups/obshtestvo.recycle/",
    "repo": "https://github.com/obshtestvo/recycle",
    "homepage": 4,
    "slug": "recycle"
}
FAKE_DB["knowyourmp"] = {
    "name": "Опознай депутата",
    "name_full": "Alerts",
    "url": "http://deputati.obshtestvo.bg/",
    "preview": "knowyourmp.jpg",
    "fb_group": "https://www.facebook.com/groups/567844279938127/",
    "repo": "https://github.com/obshtestvo/knowyourmp",
    "homepage": 5,
    "slug": "knowyourmp"
}
FAKE_DB["howto"] = {
    "name": "Howto.bg",
    "name_full": "Howto.bg (Как да ... в България)",
    "url": "http://www.howto.bg/",
    "preview": "howto.jpg",
    "homepage": 6,
    "fb_group": "https://www.facebook.com/groups/oficialen.sait.na.grazhdanina.qna/",
    "repo": "rrrrrrrr",
    "slug": "howto"
}
FAKE_DB["alerts"] = {
    "name": "Обществени Известия",
    "name_full": "Alerts",
    "url": "http://alerts.obshtestvo.bg/",
    "preview": "alerts.jpg",
    "repo": "https://github.com/obshtestvo/state-alerts",
    "fb_group": "None",
    "homepage": False,
    "slug": "alerts"
}