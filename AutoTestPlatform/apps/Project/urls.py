from django.conf.urls import url
from AutoTestPlatform.apps.Project import views

urlpatterns = [
    url(r'list$', views.pro_list, name="获取项目列表"),
    url(r'detail$', views.pro_detail, name="获取项目详情"),
    url(r'create$', views.pro_create, name="创建项目"),
    url(r'edit$', views.pro_edit, name="修改编辑项目"),
    url(r'delete$', views.pro_del, name="删除项目"),
]