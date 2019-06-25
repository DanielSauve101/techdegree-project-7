from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'profile/create/$', views.create_profile, name='create_profile'),
    url(r'profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile'),

]
