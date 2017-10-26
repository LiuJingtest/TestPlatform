from django.conf.urls import url
from AutoTestPlatform.apps.AppPerformance import views

urlpatterns = [

    # url(r'^$', views.to_index, name="渲染主页"),
    url(r'devices/list$', views.devices_list, name="获取设备列表"),
    url(r'device/packages$', views.device_packages, name="获取设备信息"),

]