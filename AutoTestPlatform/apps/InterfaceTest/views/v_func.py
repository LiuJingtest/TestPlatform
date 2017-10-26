import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import func


def func_create(req):
    """
   创建方法
   请求方法：post
   如：
   {
        "pro_id":1,                 项目id
        "func_name":"test",             方法名
        "func_code":"wkcjkdwhwjkh",         方法代码
        "func_desc":"hwbchjdcgxd"           方法描述
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
    resp = func.create_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_list(req):
    """
   获取项目下方法列表
   请求方法：post
   如：
   {
        "pro_id":1                 项目id
    }
   :return:
   如：
   成功：
   {
  "code": 1,
  "data": [
    {
      "func_desc": "hwbchjdcgxd",
      "pro_id": 1,
      "func_code": "wkcjkdwhwjkh",
      "func_name": "test",
      "func_id": 2
    }
  ],
  "msg": "获取成功"
}
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = func.get_func_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_detail(req):
    """
    获取方法详情
    请求方法：post
    如：
    {
         "func_id":1                 方法id
     }
    :return:
    如：
    成功：
    {
      "data": {
        "func_name": "test",
        "func_id": 2,
        "pro_id": 1,
        "func_desc": "hwbchjdcgxd",
        "func_code": "wkcjkdwhwjkh"
      },
      "code": 1,
      "msg": "获取成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = func.get_func_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_edit(req):
    """
    编辑方法
    请求方法：post
    如：
    {
         "func_id":1,                方法id
         "func_name":"test",             方法名
        "func_code":"wkcjkdwhwjkh",         方法代码
        "func_desc":"hwbchjdcgxd"           方法描述
     }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "编辑成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = func.edit_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_delete(req):
    """
    删除方法
    请求方法：post
    如：
    {
         "func_id":1                 方法id
     }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = func.del_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def func_run(req):
    """
    运行方法
    请求方法：post
    如：
    {
         "func_code":"jdshgjegdj"              方法代码
     }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = func.run_func(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")