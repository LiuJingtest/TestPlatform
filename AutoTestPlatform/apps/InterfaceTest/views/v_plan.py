import json
from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import plan
from .. import serversrun

scheduler = BackgroundScheduler()

def plan_create(req):
    """
    创建计划
    请求方法：post
    如：
    {
        "pro_id":4,        项目id
        "suite_id":5,      套件id
        "env_id":6,         环境id
        "plan_name":"test",     计划名
        "plan_type":1,          计划类型，1代表循环，2代表不循环
        "plan_interval":60,     间隔时间（以秒为单位）（前端的选项为下拉框，秒，分，时，日，周，月，需要计算计算出来再传给后端）
        "start_time":"2016-12-9 17:15:00",      开始时间，日期格式不能如例子所示
        "end_time":"2016-12-9 17:30:59"         结束时间，日期格式不能如例子所示（当类型为不循环时，默认为开始时间）
    }
    :return:
    如：
    成功：
   {
      "code": 1,
      "msg": "添加完毕"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = plan.add_job(data, scheduler)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def plan_delete(req):
    """
       删除计划
       请求方法：post
       如：
      {
            "plan_id":32            计划id
        }
       :return:
       如：
       成功：
      {
         "code": 1,
         "msg": "删除完毕"
       }
       """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = plan.remove_job(data, scheduler)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def plan_edit(req):
    """
   编辑计划
   请求方法：post
   如：
  {
        "plan_id":38,
        "plan_name":"test",
        "plan_type":2,
        "plan_interval":60,
        "start_time":"2016-12-9 17:25:25",
        "end_time":"2016-12-9 17:30:59"
    }
    PS：只能编辑以上的值，其他值不允许重新编辑
   :return:
   如：
   成功：
  {
     "code": 1,
        "msg": "修改成功"
   }
   """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = plan.edit_plan(data, scheduler)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def plan_list(req):
    """
      获取计划列表
      请求方法：post
      如：
     {
           "pro_id":4,
       }
      :return:
      如：
      成功：
     {
  "msg": "获取成功",
  "code": 1,
  "data": [
    {
      "plan_interval": 5,
      "suite_id": 5,
      "plan_id": 25,
      "pro_id": 4,
      "start_time": 1481274000,
      "plan_name": "test",
      "end_time": 1481274000,
      "env_id": 6,
      "plan_type": 2
    },
    {
      "plan_interval": 5,
      "suite_id": 5,
      "plan_id": 26,
      "pro_id": 4,
      "start_time": 1481268180,
      "plan_name": "test",
      "end_time": 1481274000,
      "env_id": 6,
      "plan_type": 2
    }
  ]
}
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = plan.get_plan_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def plan_detail(req):
    """
      获取计划列表
      请求方法：post
      如：
     {
           "plan_id":25
       }
      :return:
      如：
      成功：
     {
  "msg": "获取成功",
  "code": 1,
  "data":
    {
      "plan_interval": 5,
      "suite_id": 5,
      "plan_id": 25,
      "pro_id": 4,
      "start_time": 1481274000,
      "plan_name": "test",
      "end_time": 1481274000,
      "env_id": 6,
      "plan_type": 2
    }
}
      """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = plan.get_plan_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")