from django.conf.urls import url
from . import views

app_name = 'principal'

urlpatterns = [

    url(r'^$', views.main_base_view, name='main_base'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

]