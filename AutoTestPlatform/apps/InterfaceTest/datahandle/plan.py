import time

from AutoTestPlatform.apps.tools import plantool
from ..models import RunPlan
from AutoTestPlatform.apps.tools import jsontool


def get_plan_list(data):
    pro_id = data["pro_id"]
    status = data["status"]
    body = []
    now_time = int(time.time())
    if status == 0:  # 全部
        plan_list = RunPlan.objects.all().filter(pro_id=pro_id)
    elif status == 1:  # 进行中
        plan_list1 = list(RunPlan.objects.all().filter(end_time__gte=now_time, plan_type=1, pro_id=pro_id))
        plan_list2 = list(RunPlan.objects.all().filter(start_time__gte=now_time, plan_type=2, pro_id=pro_id))
        plan_list = plan_list1 + plan_list2
    elif status == 2:  # 已完成
        plan_list = list(RunPlan.objects.all().filter(end_time__lte=now_time, pro_id=pro_id))
    for a in list(plan_list):
        a = jsontool.class_to_dict(a)
        del (a['_state'])
        body.append(a)
    return {
        "code": 1,
        "msg": "获取成功",
        "data": body
    }


def get_plan_detail(data):
    plan_id = data["plan_id"]
    data = RunPlan.objects.all().get(plan_id=plan_id)
    data_json = jsontool.convert_to_dict(data)
    del (data_json['_state'])
    return {
        "code": 1,
        "msg": "获取成功",
        "data": data_json
    }


def add_job(data, scheduler):
    plan_name = data["plan_name"]
    plan_type = data["plan_type"]
    plan_interval = data["plan_interval"]
    start_time = time.mktime(time.strptime(data["start_time"],'%Y-%m-%d %H:%M:%S'))
    end_time = time.mktime(time.strptime(data["end_time"],'%Y-%m-%d %H:%M:%S'))
    env_id = data["env_id"]
    suite_id = data["suite_id"]
    pro_id = data["pro_id"]
    scheduler_ob = RunPlan.objects.create(plan_name=plan_name, plan_type=plan_type, plan_interval=plan_interval,
                                          start_time=start_time, end_time=end_time, env_id=env_id, suite_id=suite_id,
                                          pro_id=pro_id)
    plantool.set_scheduler(scheduler, scheduler_ob)
    return {
        "code": 1,
        "msg": "添加完毕"
    }


def remove_job(data, scheduler):
    plan_id = data["plan_id"]
    RunPlan.objects.get(plan_id=plan_id).delete()
    sche = scheduler.get_job("plan_"+str(plan_id))
    if sche is None:
        pass
    else:
        scheduler.remove_job("plan_"+str(plan_id))
    return {
        "code": 1,
        "msg": "删除成功"
    }


def edit_plan(data, scheduler):
    plan_id = data["plan_id"]
    plan_name = data["plan_name"]
    plan_type = data["plan_type"]
    plan_interval = data["plan_interval"]
    start_time = time.mktime(time.strptime(data["start_time"], '%Y-%m-%d %H:%M:%S'))
    end_time = time.mktime(time.strptime(data["end_time"], '%Y-%m-%d %H:%M:%S'))
    RunPlan.objects.filter(plan_id=plan_id).update(
        plan_name=plan_name, plan_type=plan_type, plan_interval=plan_interval,start_time=start_time, end_time=end_time)
    scheduler_ob = RunPlan.objects.get(plan_id=plan_id)
    sche = scheduler.get_job("plan_" + str(plan_id))
    if sche is None:
        pass
    else:
        plantool.modify_scheduler(scheduler, scheduler_ob)
    return {
        "code": 1,
        "msg": "修改成功"
    }