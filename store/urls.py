from django.conf.urls import url

from store import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^c/(?P<category_slug>\w+)/$', views.index, name='category-page'),
    url(r'^i/(?P<item_id>\d+)/$', views.item, name='item-page'),
    url(r'^checkout/$', views.checkout),
]
