import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.ToolSystem import tools


def req_repeat(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = tools.request_repeat(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")
