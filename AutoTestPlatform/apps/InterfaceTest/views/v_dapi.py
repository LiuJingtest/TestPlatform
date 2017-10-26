import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import dapi


def dapi_list(req):
    """
       获取项目所有的依赖接口列表
       请求方法：post
       如：
       {
        "pro_id":50      项目id
        }
       :return:
       如：
       成功：
       {
  "msg": "获取成功",
  "code": 1,
  "data": [
        {
          "depnd_api_url": "{{host}}/index.php?r=api/login/login",
          "depnd_api_id": 1,
          "depnd_id": 0,
          "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
          "depnd_api_method": "post",
          "depnd_api_desc": "测试描述",
          "depnd_api_type": "json",
          "depnd_api_name": "获取uid",
          "pro_id": 2,
          "depnd_api_protocol": "http"
        },
        {
          "depnd_api_url": "{{host}}/index.php?r=api/login/login",
          "depnd_api_id": 4,
          "depnd_id": 0,
          "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
          "depnd_api_method": "post",
          "depnd_api_desc": "测试描述",
          "depnd_api_type": "json",
          "depnd_api_name": "获取uid",
          "pro_id": 2,
          "depnd_api_protocol": "http"
        }
      ]
    }
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.get_dapi_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_detail(req):
    """
       获取单个依赖接口详情
       请求方法：post
       如：
      {
    "depnd_api_id":1    依赖接口id
    }
       :return:
       如：
       成功：
       {
  "data": {
    "depnd_api_name": "获取uid",
    "depnd_api_protocol": "http",
    "depnd_api_desc": "测试描述",
    "depnd_api_method": "post",
    "depnd_api_type": "json",
    "depnd_api_id": 1,
    "depnd_api_url": "{{host}}/index.php?r=api/login/login",
    "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
    "pro_id": 2,
    "depnd_id": 0
  },
  "msg": "获取成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.get_dapi_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_create(req):
    """
       创建依赖接口
       请求方法：post
       如：
       {"depnd_api_name": "获取uid",      依赖接口名
        "depnd_api_protocol": "http",       依赖接口请求协议
        "depnd_api_desc": "测试描述",       依赖接口描述
        "depnd_api_method": "get",          依赖接口请求方式
        "depnd_api_type": "post",            依赖接口请求数据格式
        "depnd_api_url": "{{host}}/index.php?r=api/login/login",    依赖接口请求url
        "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",    请求体
        "pro_id": 2,    项目id
        "depnd_id": 0   当前依赖接口所需依赖的接口id
        }
       :return:
       如：
       成功：
       {
  "msg": "创建成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.create_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_edit(req):
    """
       创建依赖接口
       请求方法：post
       如：
       {
           "depnd_api_id": 3,       需要修改的依赖接口id
       "depnd_api_name": "获取uid",      依赖接口名
        "depnd_api_protocol": "http",       依赖接口请求协议
        "depnd_api_desc": "测试描述",       依赖接口描述
        "depnd_api_method": "get",          依赖接口请求方式
        "depnd_api_type": "post",            依赖接口请求数据格式
        "depnd_api_url": "{{host}}/index.php?r=api/login/login",    依赖接口请求url
        "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",    请求体
        "pro_id": 2,    项目id
        "depnd_id": 0   当前依赖接口所需依赖的接口id
        }
       :return:
       如：
       成功：
       {
  "msg": "修改成功",
  "code": 1
}
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.edit_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_delete(req):
    """
           删除依赖接口
           请求方法：post
           如：
           {
         "depnd_api_id": 3   依赖接口id
    }
           :return:
           如：
           成功：
         {
      "msg": "删除成功",
      "code": 1
    }
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.del_dapi(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def dapi_run(req):
    """
      运行依赖接口
      请求方法：post
      如：
      {
        "depnd_api_id":1,
        "env_id":4
    }
      :return:
      如：
      成功：
    {
      "code": 1,
      "data": {
        "status_code": 200,
        "url": "http://oa.supernano.com/index.php?r=api/login/login",
        "request_body": "{\"username\": \"liujing3@supernano.com\", \"pwd\": \"670b14728ad9902aecba32e22fa4f6bd\"}",
        "response_body": {
          "code": 20000,
          "data": {
            "noticeApp": "1",
            "username": "liujing3@supernano.com",
            "phone": "14726968415",
            "position": "游戏测试",
            "entryTime": "2015-07-08",
            "taskApp": "1",
            "accessToken": "f22bda895ee41a50fab92d625ecae4bc|219",
            "hpwd": "000000",
            "orgId": 19,
            "orgName": "测试技术部",
            "email": "liujing3@supernano.com",
            "realname": "刘静3",
            "headimg": "http://oa.supernano.com/static/head-img/uploads/219.jpg",
            "uid": "219",
            "hid": "liujing3",
            "applyApp": "1",
            "companyName": "湖南纳米娱乐"
          },
          "msg": "登录成功"
        }
      },
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = dapi.run_d_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")