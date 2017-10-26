import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import suite


def suite_list(req):
    """
    获取套件列表
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
      "msg": "获取成功",
      "code": 1,
      "data": [
        {
          "suite_id": 1,
          "suite_desc": "全功能专用用例",
          "suite_name": "全功能测试",
          "pro_id": 5
        },
        {
          "suite_id": 2,
          "suite_desc": "冒烟专用用例",
          "suite_name": "冒烟测试",
          "pro_id": 5
        },
        {
          "suite_id": 3,
          "suite_desc": "测试描述",
          "suite_name": "测试名字",
          "pro_id": 5
        }
      ]
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suite.get_suite_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_detail(req):
    """
    获取套件详情
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
        }
    :return:
    如：
    成功：
    {
      "msg": "获取成功",
      "data": {
        "suite_desc": "全功能专用用例",
        "suite_id": 1,
        "pro_id": 5,
        "suite_name": "全功能测试"
      },
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suite.get_suite_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_create(req):
    """
    创建套件
    请求方法：post
    参数：
        项目id：pro_id     套件名：suite_name   套件描述：suite_desc
    如：
        {
        "suite_name": "全功能测试2",
        "pro_id": 5,
        "suite_desc": "全功能专用用例2"
      }
    :return:
    如：
    成功：
    {
      "msg": "创建套件成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suite.create_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_edit(req):
    """
    修改编辑套件
        请求方法：post
    参数：
        项目id：pro_id     套件id：suite_id    套件名：suite_name   套件描述：suite_desc
    如：
        {
        "suite_id":1,
        "suite_name": "全功能测试2",
        "pro_id": 5,
        "suite_desc": "全功能专用用例2"
      }
    :return:
    如：
    成功：
    {
      "msg": "编辑套件成功",
      "code": 1
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = suite.edit_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_del(req):
    """
    删除套件
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
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
    resp = suite.del_suite(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def suite_case_list(req):
    """
    获取套件下的case列表
    请求方法：post
    参数：
        模块id：suite_id
    如：
        {
        "suite_id":1,
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
    resp = suite.get_suite_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")