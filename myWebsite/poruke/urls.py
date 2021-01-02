from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.root, name='poruke_root'),
    path('broj/<int:broj>/', views.broj, name='poruke_broj'),
    path('intro_video/', views.intro_video, name='intro_video'),
    path(r'search/$', views.SearchFormView.as_view(), name='search'),
    path(r'register/$', views.UserFormView.as_view(), name='register'),
    #path(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #/poruke/1
    path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /poruke/poruka/add/
    path(r'poruke/add$', views.PorukaCreate.as_view(), name='poruka-add'),

    # /poruke/poruka/1/
    path(r'poruke/(?P<pk>[0-9]+)/$', views.PorukaUpdate.as_view(), name='poruka-update'),

    # /poruke/poruka/1/delete/
    path(r'poruke/(?P<pk>[0-9]+)/delete/$', views.PorukaDelete.as_view(), name='poruka-delete'),
]
