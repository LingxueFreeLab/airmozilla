from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<template_name>\w+\.html)$',
        views.partial_template,
        name='partial_template'),
    url(r'^api/yours/$',
        views.your_events,
        name='your_events'),
    url(r'^api/save/$',
        views.save_upload,
        name='save_upload'),
    url(r'^api/(?P<id>\d+)/$',
        views.event_edit,
        name='edit'),
    url(r'^api/(?P<id>\d+)/archive/$',
        views.event_archive,
        name='archive'),
    url(r'^api/(?P<id>\d+)/screencaptures/$',
        views.event_screencaptures,
        name='screencaptures'),
    url(r'^api/(?P<id>\d+)/picture/$',
        views.event_picture,
        name='picture'),
    url(r'^api/(?P<id>\d+)/summary/$',
        views.event_summary,
        name='summary'),
    url(r'^api/(?P<id>\d+)/video/$',
        views.event_video,
        name='video'),
    url(r'^api/(?P<id>\d+)/publish/$',
        views.event_publish,
        name='publish'),
    url(r'^api/(?P<id>\d+)/delete/$',
        views.event_delete,
        name='delete'),
    # Do this to avoid any undefined api calls to be attempted as an
    # html pushstate thing in ui-router.
    url(r'^api/',
        'django.views.defaults.page_not_found'),
    url(r'^vidly/webhook/$',
        views.vidly_media_webhook,
        name='vidly_media_webhook'),
    # lastly
    url(r'',
        views.home,
        name='home'),
)
