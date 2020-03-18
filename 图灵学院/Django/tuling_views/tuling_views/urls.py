from django.conf.urls import include, url
from django.contrib import admin

from teacher_app import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'tuling_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^teacher/', v.teacher),
    url(r'^v2_exp/', v.v2_exception),


    # 重定向，服务器端跳转
    url(r'^v10_1/', v.v10_1),
    url(r'^v10_2/', v.v10_2),
    url(r'^v11/', v.v11, name="v11"),
]
