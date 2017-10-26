import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import api


def api_list(req):
    """
    获取项目下的接口列表
    :param req:
    请求方法：post
    参数：
        项目id：pro_id
    如：
        {
        "pro_id":5,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "module_id": 1,
          "api_id": 1,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "34",
          "api_param": "username,pwd",
          "pro_id": 5,
          "api_desc": "登录",
          "api_name": "登录接口",
          "api_url": "{host}/login"
        },
        {
          "module_id": 1,
          "api_id": 2,
          "api_protocol": "http",
          "api_method": "post",
          "api_type": "12",
          "api_param": "email",
          "pro_id": 5,
          "api_desc": "忘记密码",
          "api_name": "忘记密码接口",
          "api_url": "{host}/forgetpwd"
        }
      ],
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = api.get_api_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_detail(req):
    """
   获取项目下的接口列表
   :param req:
   请求方法：post
   参数：
       接口id：api_id
   如：
       {
       "api_id":1,
       }
   :return:
   如：
   成功：
       {
      "msg": "获取成功",
      "code": 1,
      "data": {
        "api_param": "username,pwd",
        "api_id": 1,
        "module_id": 1,
        "pro_id": 5,
        "api_url": "{host}/login",
        "api_method": "post",
        "api_type": "34",
        "api_protocol": "http",
        "api_name": "登录接口",
        "api_desc": "登录"
      }
    }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = api.get_api_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_create(req):
    """
    创建接口
    请求方法：post
    参数：
    如：
        {
        "module_id": 1,                  模块id
        "pro_id": 5,                     项目id
        "api_url": "{host}/login",       接口url
        "api_method": "post",            请求方法：get，post，put，detele
        "param_type": "34",                请求类型
        "api_protocol": "http",          请求协议：http，tcp，udp等等（待定）
        "api_name": "登录接口",           接口名字
        "api_desc": "登录"                接口描述
      }
    :return:
    如：
    成功：
    {
      "msg": "创建接口成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = api.create_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_edit(req):
    """
    修改编辑接口
        请求方法：post
    如：
       {
        "api_param": "username,pwd",     接口参数
        "module_id": 1,                  模块id
        "pro_id": 5,                     项目id
        "api_id": 5,                     接口id
        "api_url": "{host}/login",       接口url
        "api_method": "post",            请求方法：get，post，put，detele
        "api_type": "34",                请求类型
        "api_protocol": "http",          请求协议：http，tcp，udp等等（待定）
        "api_name": "登录接口",           接口名字
        "api_desc": "登录"                接口描述
      }
    :return:
    如：
    成功：
    {
      "msg": "编辑接口成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = api.edit_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_del(req):
    """
    删除接口
    请求方法：post
    参数：
        接口id：api_id
    如：
        {
        "api_id":1,
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
    resp = api.del_api(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def api_case_list(req):
    """
    获取接口下的case列表+
    请求方法：post
    参数：
        接口id：api_id
    如：
        {
        "api_id":1,
        }
    :return:
    如：
    成功：
    {
      "data": [
        {
          "case_name": "正确登录",
          "input_data": "请求参数",
          "exp_data": "期待输出",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "正向验证",
          "check_type": 0,
          "case_id": 1,
          "api_id": 1,
          "is_set": 1
        },
        {
          "case_name": "密码错误",
          "input_data": "请求参数2",
          "exp_data": "期待输出2",
          "pro_id": 5,
          "module_id": 1,
          "case_desc": "反向验证",
          "check_type": 0,
          "case_id": 2,
          "api_id": 1,
          "is_set": 1
        }
      ],
      "msg": "获取成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = api.get_api_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")
