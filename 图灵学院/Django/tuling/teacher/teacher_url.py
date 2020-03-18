from django.conf.urls import include, url
from django.contrib import admin

from . import views  # 当前目录用 . 号

urlpatterns = [
    # Examples:
    # url(r'^$', 'tuling.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'liudana/', views.do_app),

    
]
