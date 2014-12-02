from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^play/$', 'play.views.webplay', name='web_play'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^download/pins/', 'pins.views.download_pins'),
)
