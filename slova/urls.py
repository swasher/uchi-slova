from django.conf.urls import url

from slova import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^grid/$', views.grid, name='grid'),
    url(r'^add_word/$', views.add_word, name='add_word'),
    url(r'^delete_word/$', views.delete_word, name='delete_word'),
    url(r'^change_points/$', views.change_points, name='change_points'),
]
