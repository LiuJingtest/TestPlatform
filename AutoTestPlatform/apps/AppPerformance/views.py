# import json
#
# from django.shortcuts import HttpResponse
#
# from AutoTestPlatform.apps.AppPerformance.data_handle import devices
#
#
# def devices_list(req):
#     data = json.loads(str(req.body, encoding="utf-8"))
#     resp = devices.getDevicesList()
#     return HttpResponse(json.dumps(resp), content_type="application/json")
#
#
# def device_packages(req):
#     data = json.loads(str(req.body, encoding="utf-8"))
#     resp = devices.getDevicePackages(data)
#     return HttpResponse(json.dumps(resp), content_type="application/json")