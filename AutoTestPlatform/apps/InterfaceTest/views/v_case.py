import json

from django.shortcuts import HttpResponse

from AutoTestPlatform.apps.InterfaceTest.datahandle import case


def case_list(req):
    """
    获取项目下的case列表+
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
    resp = case.get_pro_case_list(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_detail(req):
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = case.get_case_detail(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_create(req):
    """
    创建case
    请求方法：post
    如：
    {
        "pro_id": 1,   项目id
        "api_id": 1,    接口id
        "case_desc": "1111",    用例描述
        "case_name": "1",       用例名
        "depnd_api_id": 1,         依赖接口id
        "check_id": 2,        验证器id
        "input_data": "11",     请求输入
        "exp_data": "11",       期待返回
        "case_schema": "1",     schema检验
        "case_protocol": "http",    请求协议
        "case_url": "url",      请求的url
        "case_method": "post",      请求方式
        "exp_status": 200,      期待状态码
        "exp_resp_header": "242",       期待响应头
        "param_type": "json",        参数格式
        "suite_list":[1,2]      套件列表
    }
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = case.create_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_edit(req):
    """
    编辑case的基本信息
    请求方法：post
    如：
    {
	    "case_id":1,
        "pro_id": 1,   项目id
        "api_id": 1,    接口id
        "case_desc": "1111",    用例描述
        "case_name": "1",       用例名
        "depnd_api_id": 1,         依赖接口id
        "check_id": 2,        验证器id
        "input_data": "11",     请求输入
        "exp_data": "11",       期待返回
        "case_schema": "1",     schema检验
        "case_protocol": "http",    请求协议
        "case_url": "url",      请求的url
        "case_method": "post",      请求方式
        "exp_status": 200,      期待状态码
        "exp_resp_header": "242",       期待响应头
        "param_type": "json",        参数格式
        "suite_list":[1,2]      套件列表
}
    :return:
    如：
    成功：
    {
      "code": 1,
      "msg": "保存成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = case.edit_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_del(req):
    """
   删除case
   请求方法：post
   如：
   {
     "case_id": 1,    case的id
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
    resp = case.del_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def case_run(req):
    """
       运行用例
       请求方法：post
       如：
        {
        "case_id":1,        case_id
        "env_id":4          环境id
        }
       :return:
       如：
       成功：
    {
  "data":
  {
        "request_body": "{\"username\": \"liujing3@supernano.com\", \"pwd\": \"670b14728ad9902aecba32e22fa4f6bd\"}",
        "status_code": 200,
        "result_check": 1,
        "response_body": {
          "data": {
            "realname": "刘静3",
            "orgId": 19,
            "orgName": "测试技术部",
            "applyApp": "1",
            "headimg": "http://oa.supernano.com/static/head-img/uploads/219.jpg",
            "email": "liujing3@supernano.com",
            "hid": "liujing3",
            "taskApp": "1",
            "username": "liujing3@supernano.com",
            "accessToken": "704e8e873ae196e83fa3fb9861287823|219",
            "entryTime": "2015-07-08",
            "position": "游戏测试",
            "companyName": "湖南纳米娱乐",
            "phone": "14726968415",
            "noticeApp": "1",
            "hpwd": "000000",
            "uid": "219"
          },
          "code": 20000,
          "msg": "登录成功"
        },
        "exp_data": "刘静",
        "url": "http://oa.supernano.com/index.php?r=api/login/login",
        "schema": {
          "type": "object",
          "$schema": "http://json-schema.org/draft-04/schema#",
          "required": [
            "data",
            "msg",
            "code"
          ],
          "properties": {
            "data": {
              "type": "object",
              "required": [
                "username",
                "hid",
                "email",
                "noticeApp",
                "applyApp",
                "taskApp",
                "position",
                "orgId",
                "uid",
                "hpwd",
                "companyName",
                "accessToken",
                "entryTime",
                "realname",
                "phone",
                "headimg",
                "orgName"
              ],
              "properties": {
                "realname": {
                  "type": "string"
                },
                "orgId": {
                  "type": "integer"
                },
                "orgName": {
                  "type": "string"
                },
                "hid": {
                  "type": "string"
                },
                "applyApp": {
                  "type": "string"
                },
                "headimg": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "noticeApp": {
                  "type": "string"
                },
                "taskApp": {
                  "type": "string"
                },
                "username": {
                  "type": "string"
                },
                "accessToken": {
                  "type": "string"
                },
                "entryTime": {
                  "type": "string"
                },
                "position": {
                  "type": "string"
                },
                "companyName": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "hpwd": {
                  "type": "string"
                },
                "uid": {
                  "type": "string"
                }
              }
            },
            "code": {
              "type": "integer"
            },
            "msg": {
              "type": "string"
            }
          }
        },
        "schema_check": 1
      },
      "code": 1,
      "msg": "删除成功"
    }
    """
    data = json.loads(str(req.body, encoding="utf-8"))
    resp = case.run_case(data)
    return HttpResponse(json.dumps(resp), content_type="application/json")

