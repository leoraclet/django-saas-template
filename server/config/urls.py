from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic.base import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken.views import obtain_auth_token


# Sentry debug endpoint
def trigger_error(_):
    return HttpResponse(1 / 0)


sitemaps = {}
admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)  # type: ignore

# Internationalization
urlpatterns = i18n_patterns(
    path(r"", include("apps.core.urls"), name="home"),
    path(r"chat/", include("apps.chat.urls"), name="chat"),
    path(r"ht/", include("health_check.urls")),
    # ==============================================================================
    # Allauth
    # ==============================================================================
    path(r"", include("allauth.idp.urls")),
    path(r"accounts/", include("allauth.urls"), name="accounts"),
    path(r"accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    path(settings.ADMIN_URL, admin.site.urls, name="admin"),
    # ==============================================================================
    # Djstripe
    # ==============================================================================
    path(r"djstripe/", include("djstripe.urls", namespace="djstripe")),
    # ==============================================================================
    # API
    # ==============================================================================
    # Include the allauth headless URLs for API endpoints
    path(r"_allauth/", include("allauth.headless.urls")),
    path(
        r"api/",
        include(
            [
                path(r"", include("apps.core.api.urls")),
                # Here you can include other API apps ...
            ]
        ),
    ),
    # ==============================================================================
    # API Documentation
    # ==============================================================================
    path(r"api-auth/", include("rest_framework.urls")),
    path(r"api/auth-token/", obtain_auth_token, name="obtain_auth_token"),
    path(r"api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(r"api/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path(r"api/swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
    # ==============================================================================
    # Internationalization
    # ==============================================================================
    path(r"i18n/", include("django.conf.urls.i18n")),
)

urlpatterns += [
    # ==============================================================================
    # Debugging, testing and monitoring
    # ==============================================================================
    path(r"sentry-debug/", trigger_error),
    # ==============================================================================
    # Site map
    # ==============================================================================
    path(r"sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap-xml"),
]

if bool(settings.DEBUG):
    # Silk
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
    # Debug toolbar and browser reload
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    # Static and media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
