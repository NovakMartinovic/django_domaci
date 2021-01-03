from django.urls import path
from django.contrib.auth import logout

from . import views
#from ..myWebsite import settings
from django.conf.urls import url
app_name = 'poruke'

urlpatterns = [
    path('', views.test_poruke, name='test_poruke'),
    path('main', views.IndexView.as_view(), name='index'),
    #path(r'^$', views.root, name='poruke_root'),
    path('broj/<int:broj>/', views.broj, name='poruke_broj'),
    path('intro_video/', views.intro_video, name='intro_video'),
    url(r'search/$', views.SearchFormView.as_view(), name='search'),
    url(r'register/$', views.UserFormView.as_view(), name='register'),
    #path(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #/poruke/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /poruke/poruka/add/
    url(r'poruke/add$', views.PorukaCreate.as_view(), name='poruka-add'),

    # /poruke/poruka/1/
    url(r'poruke/(?P<pk>[0-9]+)/$', views.PorukaUpdate.as_view(), name='poruka-update'),

    # /poruke/poruka/1/delete/
    url(r'poruke/(?P<pk>[0-9]+)/delete/$', views.PorukaDelete.as_view(), name='poruka-delete'),
]
