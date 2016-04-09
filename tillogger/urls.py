from django.conf.urls import include, url
from django.contrib import admin

import lessons.urls


urlpatterns = [
    # Re-use lessons.urls root-view as full root view.
    url(r'^$', include(lessons.urls)),

    url(r'^lessons/', include(lessons.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
