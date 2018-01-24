from django.conf.urls import url
from django.contrib import admin

from healthixapp.views import index,signup,login_view,homepage,logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^homepage/$', homepage, name='homepage'),
    url(r'^$', index, name='index'),
]
