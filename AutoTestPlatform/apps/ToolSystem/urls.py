from django.conf.urls import url
from AutoTestPlatform.apps.ToolSystem import views

urlpatterns = [

    # url(r'^$', views.to_index, name="渲染主页"),
    url(r'request_repeat$', views.req_repeat, name="重复请求"),

]