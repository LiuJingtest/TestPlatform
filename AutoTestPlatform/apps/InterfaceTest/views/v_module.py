import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import module


def module_list(req):
    """
    获取项目下的模块列表
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
      "code": 1,
      "msg": "获取成功",
      "data": [
        {
          "pro_id": 5,
          "module_id": 1,
          "module_desc": "ceshimiaoshu111111",
          "module_name": "ceshiming111111"
        }
      ]
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = module.get_module_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_detail(req):
    """
    获取模块详情
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "获取成功",
      "code": 1,
      "data": {
        "module_desc": "ceshimiaoshu111111",
        "module_id": 1,
        "pro_id": 5,
        "module_name": "ceshiming111111"
      }
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = module.get_module_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_create(req):
    """
    创建模块
    :param req:
    请求方法：post
    参数：
        项目id：pro_id    模块名：module_name    模块描述：module_desc
    如：
        {
        "pro_id":5,
        "module_name":"ceshiming",
        "module_desc":"ceshimiaoshu"
        }
    :return:
    如：
    成功：
    {
      "msg": "创建模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = module.create_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_edit(req):
    """
    编辑模块
    :param req:
    请求方法：post
    参数：
        项目id：pro_id    模块id：module_id    模块名：module_name    模块描述：module_desc
    如：
        {
        "pro_id":5,
        "module_id":1,
        "module_name":"ceshiming",
        "module_desc":"ceshimiaoshu"
        }
    :return:
    如：
    成功：
    {
      "msg": "编辑模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = module.edit_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_del(req):
    """
    编辑模块
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "删除模块成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = module.del_module(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_api_list(req):
    """
    获取模块下的接口列表
    :param req:
    请求方法：post
    参数：
        项目id：module_id
    如：
        {
        "module_id":1,
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
    resp = module.get_module_api_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def module_case_list(req):
    """
    获取模块下的用例列表
    :param req:
    请求方法：post
    参数：
        模块id：module_id
    如：
        {
        "module_id":1,
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
    resp = module.get_module_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")
