from AutoTestPlatform.apps.InterfaceTest.models import RunPlan
from AutoTestPlatform.apps.InterfaceTest.datahandle import caserun

import time


def start_scheduler(scheduler):
    now_time = int(time.time())
    scheduler_list1 = list(RunPlan.objects.all().filter(end_time__gte=now_time, plan_type=1))
    scheduler_list2 = list(RunPlan.objects.all().filter(start_time__gte=now_time, plan_type=2))
    scheduler_list = scheduler_list1+scheduler_list2
    for scheduler_ob in scheduler_list:
        set_scheduler(scheduler, scheduler_ob)


def set_scheduler(scheduler,scheduler_ob):
    plan_type = scheduler_ob.plan_type
    plan_id = scheduler_ob.plan_id
    plan_interval = scheduler_ob.plan_interval
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(scheduler_ob.start_time))
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(scheduler_ob.end_time))
    run_data = {
        "env_id": scheduler_ob.env_id,
        "suite_id": scheduler_ob.suite_id,
        "report_name": "",
        "pro_id": scheduler_ob.pro_id
    }
    # plan_type:1-----循环    2：不循环
    if plan_type == 1:
        scheduler.add_job(caserun.get_run_info, args=[run_data], trigger='interval', seconds=plan_interval,
                          id="plan_" + str(plan_id), start_date=start_time, end_date=end_time)
    else:
        scheduler.add_job(caserun.get_run_info, args=[run_data], trigger='date', run_date=start_time,
                          id="plan_" + str(plan_id))


def modify_scheduler(scheduler, scheduler_ob):
    plan_type = scheduler_ob.plan_type
    plan_id = scheduler_ob.plan_id
    plan_interval = scheduler_ob.plan_interval
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(scheduler_ob.start_time))
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(scheduler_ob.end_time))
    # plan_type:1-----循环    2：不循环
    if plan_type == 1:
        scheduler.reschedule_job("plan_" + str(plan_id),trigger='interval', seconds=plan_interval,
                                 start_date=start_time, end_date=end_time)
    else:
        scheduler.reschedule_job("plan_" + str(plan_id), trigger='date',
                                 run_date=start_time)