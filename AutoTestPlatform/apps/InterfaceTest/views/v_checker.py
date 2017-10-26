import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import checker


def check_create(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.create_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_list(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.get_check_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.get_check_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_edit(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.edit_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_delete(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.del_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_run(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = checker.run_check(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")