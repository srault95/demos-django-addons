from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url=reverse_lazy("admin:index"), permanent=False)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('adminmce/doc/', include('django.contrib.admindocs.urls'))
    ] + urlpatterns
