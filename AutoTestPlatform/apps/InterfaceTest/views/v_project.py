from django.shortcuts import HttpResponse
import logging
import json

from AutoTestPlatform.apps.InterfaceTest.datahandle import project


logger = logging.getLogger('django')


def pro_list(req):
    resp = project.get_pro_list()
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = project.get_pro_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_create(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = project.create_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_edit(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = project.edit_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def pro_del(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = project.del_pro(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")
