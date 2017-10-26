myApp.controller('APICaseCtrl',function($scope,$http,$cookieStore,$timeout,$location,$rootScope) {
    var pro_id = $cookieStore.get("currProID");
    var moduleId=0;
    var apiId=0;
    var caseId=0;
    $scope.showBtn=false;
    $scope.showModule=true;
    $scope.List=["active"];
    $scope.envList="";
    $scope.suite_list=[];
    $scope.varInfoShow=true;
    $scope.moduleList="";
    $scope.module={
        "module_desc": "",
        "module_id": "",
        "pro_id": pro_id,
        "module_name": ""
    }
    $scope.suiteList="";
    $scope.suite={
        "suite_desc": "",
        "suite_id": 0,
        "pro_id": pro_id,
        "suite_name": ""
    };
    $scope.methodType=["GET","POST","PUT","DELETE"];
    $scope.protocolType=["http","https"];
    //$scope.typeType=["json","raw","text"];
    $scope.typeType=["json"];
    $scope.apiList="";
    $scope.api={
        "pro_id": pro_id,
        "api_id": 0,
        "module_id": $scope.module.module_id,
        "api_desc": "",
        "api_param": "",
        "api_url": "",
        "api_method": "",
        "api_type": "",
        "api_protocol": "",
        "api_name": ""
    };

    $scope.caseList="";
    $scope.case={
        "case_id":0,
        "pro_id": pro_id,
        "api_id": 0,
        "case_desc": "",
        "case_name": "",
        "depnd_api_id": 0,
        "check_id": 0,
        "input_data": "",
        "exp_data": "",
        "case_schema": "",
        "case_protocol": "",
        "case_url": "",
        "case_method": "",
        "exp_status": 200,
        "exp_resp_header": "",
        "param_type": "",
        "suite_list":[]
    }
    $scope.report={
        "report_name": "",
        "start_time": "",
        "suite_id": 1,
        "fail_num": 1,
        "pro_id": pro_id,
        "pass_num": 1,
        "result_id": 50,
        "end_time": 1478621079
    }
    $scope.check1={
        "check_name": "",
        "check_id": 0,
        "pro_id": pro_id,
        "check_desc": "",
        "check_code": ""
    }
    $scope.depnd={
        "depnd_api_name": "",
        "depnd_api_protocol": "",
        "depnd_api_desc": "",
        "depnd_api_method": "",
        "depnd_api_type": "",
        "depnd_api_id": 0,
        "depnd_api_url": "",
        "depnd_api_param": "",
        "pro_id": pro_id,
        "depnd_id": 0
    }

    $scope.showCase=[];
    $timeout(function(){
        $http.post('interface/project/env/list',{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.envList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $http.post("interface/project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
                $scope.apiDep=new Object();
                $scope.apiDep.depnd_api_name="无";
                $scope.apiDep.depnd_api_id=0;
                $scope.apiDepList.unshift($scope.apiDep);
            }else{
                alert(response.msg)
            }
        })
        $http.post("interface/project/check/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.checkList=response.data;
                $scope.check1=new Object();
                $scope.check1.check_desc="默认";
                $scope.check1.check_id=0;
                $scope.checkList.unshift($scope.check1);
            }else{
                alert(response.msg)
            }
        })
        $scope.showAllAPI=true;
        $http.post('interface/project/module/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.moduleList = response.data;
            }else{
                alert(response.msg);
            }
        });
        for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
        }
        $scope.List[0]="active"
        $http.post('interface/project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
                $scope.totalItems=$scope.apiList.length;
                $scope.currentPage = 1;
                $scope.pageChanged();
                $scope.showCase=[];
                 for(var i=0;i<$scope.apiList.length;i++){
                    $scope.showCase[i]=false;
                 }
            }else{
                alert(response.msg)
            }
        })
        $scope.showBtn=false;
        $scope.showBtn1=true;
        $http.post('interface/project/suite/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.suiteList = response.data;
            }else{
                alert(response.msg);
            }
        });
    })

    $scope.pageChanged=function(){
        $http.post('interface/project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
                $scope.totalItems=$scope.apiList.length;
                $scope.pageList=[];
                if($scope.totalItems>0){
                    if($scope.currentPage==Math.ceil($scope.apiList.length/10)){
                        for(var i=0;i<$scope.apiList.length-($scope.currentPage-1)*10;i++){
                            $scope.pageList[i]=$scope.apiList[($scope.currentPage-1)*10+i];
                        }
                    }else{
                        for(var i=0;i<10;i++){
                            $scope.pageList[i]=$scope.apiList[($scope.currentPage-1)*10+i];
                        }
                    }
                }
            }
        })
    }

    $scope.showAll=function(){
        for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
        }
        $scope.List[0]="active";
        $http.post('interface/project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
                $scope.pageChanged();
                $scope.showCase=[];
                 for(var i=0;i<$scope.apiList.length;i++){
                    $scope.showCase[i]=false;
                 }
            }else{
                alert(response.msg)
            }
        })
         $scope.showBtn=false;
         $scope.showBtn1=true;
         $scope.showAllAPI=true;
    }

    $scope.active1 = function(id) {
         for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
         }
         $scope.List[id+1]='active';
         $scope.List[0]="disactive";
         $scope.module=$scope.moduleList[id];
         $scope.showId=$scope.module.module_id;
         $scope.showBtn=true;
         $scope.showBtn1=false;
         $scope.showAllAPI=false;
         $http.post('interface/project/module/apiList',{
             "module_id":$scope.module.module_id
         }).success(function(response){
             if(response.code==1){
                 $scope.apiList=response.data;
                 $scope.totalItems=$scope.apiList.length;
                 $scope.pageList=[];
                 if($scope.totalItems>0){
                    if($scope.currentPage==Math.ceil($scope.apiList.length/10)){
                        for(var i=0;i<$scope.apiList.length-($scope.currentPage-1)*10;i++){
                            $scope.pageList[i]=$scope.apiList[($scope.currentPage-1)*10+i];
                        }
                    }else{
                        for(var i=0;i<10;i++){
                            $scope.pageList[i]=$scope.apiList[($scope.currentPage-1)*10+i];
                        }
                    }
                 }
                 $scope.showCase=[];
                 for(var i=0;i<$scope.apiList.length;i++){
                    $scope.showCase[i]=false;
                 }
             }else{
                 alert(response.msg);
             }
         })
    }

    $scope.run=function(){
        $("#runModule").modal();
        $scope.report_name="";
        $scope.env="无";
        $scope.suite="";
    }


      $scope.change = function() {
           proCtrl.model_id = $scope.test;
      };

    $scope.report_name="";
    $scope.showLoading=false;
    $scope.saveRun=function(envId,suiteId){
        if(envId==undefined){
            envId=0;
        }
        if(suiteId==undefined){
            suiteId=0;
        }
        $scope.showLoading=true;
        $http.post('interface/project/case/run',{
            "suite_id":suiteId,
            "pro_id":pro_id,
            "env_id":envId,
            "report_name": $scope.report_name
        }).success(function(response){
            if(response.code==1){
                $scope.report=response.data;
                $scope.showLoading=false;
                $rootScope.caseRun=1;
                $location.url('/interface/project/testReport');
                $rootScope.active(8);
                //$rootScope.showDetail($rootScope.resultList[0]);
            }else{
                alert(response.msg)
            }
        })
        $("#runModule").modal('hide');
        $("#loading").modal();

    }

    $scope.addModule=function(){
        $scope.module="";
        $("#AddModule").modal();
    }

    $scope.saveModule=function(){
        if($scope.module.module_name==null){
            $scope.module.module_name="";
        }
        if($scope.module.module_desc==null){
            $scope.module.module_desc="无";
        }
        $http.post('interface/project/module/create',{
            "pro_id":pro_id,
            "module_name":$scope.module.module_name,
            "module_desc":$scope.module.module_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddModule").modal('hide');
                $http.post('interface/project/module/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.moduleList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

     $scope.editModule=function(){
         $("#editModule").modal();
     }

     $scope.saveModule=function(){
        if($scope.module.module_name==null){
            $scope.module.module_name="";
        }
        if($scope.module.module_desc==null){
            $scope.module.module_desc="无";
        }
        $http.post('interface/project/module/create',{
            "pro_id":pro_id,
            "module_name":$scope.module.module_name,
            "module_desc":$scope.module.module_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddModule").modal('hide');
                $http.post('interface/project/module/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.moduleList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
     }

     $scope.cfModoule=function(id){
        $("#cfModule").modal();
        moduleId=id;
    }

    $scope.delModule=function(){
        $("#cfModule").modal('hide');
        $http.post('interface/project/module/delete',{
            "module_id":moduleId,
        }).success(function (response1) {
            if(response1.code==1){
                $http.post('interface/project/module/list', {
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.moduleList = response.data;
                     }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response1.msg);
            }
        });
    }

    $scope.addSuite=function(){
         $scope.suite="";
        $("#AddSuite").modal();
    }

    $scope.saveSuite=function(){
        if($scope.suite.suite_name==null){
            $scope.suite.suite_name="";
        }
        if($scope.suite.suite_desc==null){
            $scope.suite.suite_desc="无";
        }
        $http.post('interface/project/suite/create',{
            "pro_id":pro_id,
            "suite_name":$scope.suite.suite_name,
            "suite_desc":$scope.suite.suite_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddSuite").modal('hide');
                $http.post('interface/project/suite/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.suiteList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.addApi=function(){
        $http.post('interface/project/module/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.moduleList = response.data;
            }else{
                alert(response.msg);
            }
        });
        $scope.api="";
        $("#addapi").modal();
    }

    $scope.saveAPI=function(id){
        if($scope.api.api_name==null){
            $scope.api.api_name="";
        }
        if($scope.api.api_desc==null){
            $scope.api.api_desc="无";
        }
        if(id==""){
            id=0;
        }
        if($scope.api.api_protocol==undefined){
            $scope.api.api_protocol="http";
        }
        if($scope.api.api_method==undefined){
            $scope.api.api_method="POST";
        }
        if($scope.api.param_type==undefined){
            $scope.api.param_type="json";
        }
        $http.post('interface/project/api/create',{
            "module_id": id,
            "pro_id": pro_id,
            "api_url": $scope.api.api_url,
            "api_method": $scope.api.api_method,
            "param_type": $scope.api.param_type,
            "api_protocol": $scope.api.api_protocol,
            "api_name": $scope.api.api_name,
            "api_desc": $scope.api.api_desc
        }).success(function (response) {
            if(response.code==1){
                $("#addapi").modal('hide');
                if($scope.showAllAPI){
                    $http.post('interface/project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                             $scope.pageChanged();
                             $scope.showCase=[];
                             for(var i=0;i<$scope.apiList.length;i++){
                                $scope.showCase[i]=false;
                             }
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('interface/project/module/apiList',{
                     "module_id":$scope.showId
                     }).success(function(response2){
                         if(response2.code==1){
                             $scope.apiList=response2.data;
                             $scope.pageChanged();
                             $scope.showCase=[];
                             for(var i=0;i<$scope.apiList.length;i++){
                                $scope.showCase[i]=false;
                             }
                         }else{
                             alert(response2.msg);
                         }
                     })
                }
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.selected=0;
    $scope.editapi=function(id){
        $http.post('interface/project/api/detail',{
            "api_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.api=response.data;
                $scope.api.api_method=$scope.api.api_method.toLocaleUpperCase();
                $scope.selected=$scope.api.module_id;
            }else{
                alert(response.msg);
            }
        })
        $("#editapi").modal();
    }

    $scope.saveEditAPI=function(id){
        if($scope.api.api_name==null){
            $scope.api.api_name="";
        }
        if($scope.api.api_desc==null){
            $scope.api.api_desc="无";
        }
        $http.post('interface/project/api/edit',{
            "module_id": id,
            "pro_id": pro_id,
            "api_id": $scope.api.api_id,
            "api_url": $scope.api.api_url,
            "api_method": $scope.api.api_method,
            "param_type": $scope.api.param_type,
            "api_protocol": $scope.api.api_protocol,
            "api_name": $scope.api.api_name,
            "api_desc": $scope.api.api_desc
        }).success(function (response) {
            if(response.code==1){
                $("#editapi").modal('hide');
                if($scope.showAllAPI){
                     $http.post('interface/project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                             $scope.pageChanged();
                             $scope.showCase=[];
                             for(var i=0;i<$scope.apiList.length;i++){
                                $scope.showCase[i]=false;
                             }
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('interface/project/module/apiList',{
                        "module_id":$scope.showId
                     }).success(function(response2){
                     if(response2.code==1){
                         $scope.apiList=response2.data;
                         $scope.pageChanged();
                         $scope.showCase=[];
                         for(var i=0;i<$scope.apiList.length;i++){
                            $scope.showCase[i]=false;
                         }
                     }else{
                         alert(response2.msg);
                     }
                 })
                }
            }else {
                alert(response.msg);
            }
        });
    }

    $scope.cfDelapi=function(id){
        $("#cfAPI").modal();
        apiId=id;
    }

    $scope.delAPI=function(){
        $("#cfAPI").modal('hide');
        $http.post('interface/project/api/delete',{
            "api_id":apiId,
        }).success(function (response1) {
            if(response1.code==1){
                if($scope.showAllAPI){
                    $http.post('interface/project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                             $scope.pageChanged();
                             $scope.showCase=[];
                             for(var i=0;i<$scope.apiList.length;i++){
                                $scope.showCase[i]=false;
                             }
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('interface/project/module/apiList',{
                     "module_id":$scope.showId
                     }).success(function(response2){
                         if(response2.code==1){
                             $scope.apiList=response2.data;
                             $scope.pageChanged();
                             $scope.showCase=[];
                             for(var i=0;i<$scope.apiList.length;i++){
                                $scope.showCase[i]=false;
                             }
                         }else{
                             alert(response2.msg);
                         }
                     })
                }
            }else{
                alert(response1.msg);
            }
        })
    }

    $scope.getAPICase=function(id,index){
        for(var i=0;i<$scope.showCase.length;i++){
            if(i!=index){
                $scope.showCase[i]=false;
            }
        }
        $http.post('interface/project/api/caseList',{
            "api_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.caseList=response.data;
                $scope.showinfo=[];
                for(var i=0;i<$scope.caseList.length;i++){
                    $scope.showinfo[i]=false;
                }
                $scope.showCase[index]=!$scope.showCase[index];
            }else{
                alert(response.msg);
            }
        })
    }
    $scope.check=[];

    $scope.addCase=function(){
        $scope.case={
            "case_id":0,
            "pro_id": pro_id,
            "api_id": 0,
            "case_desc": "",
            "case_name": "",
            "depnd_api_id": 0,
            "check_id": 0,
            "input_data": "",
            "exp_data": "",
            "case_schema": "",
            "case_protocol": "",
            "case_url": "",
            "case_method": "",
            "exp_status": 200,
            "exp_resp_header": "",
            "param_type": "",
            "suite_list":[],
            "front_sql":"",
            "rear_sql":"",
            "is_run_sql":0
        };
        $scope.selectedApi=0;
        $scope.api="";
        $scope.suite_list = [];
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.check[i]=false;
        }
        $("#AddCase").modal();
    }

    $scope.getApi=function(obj,apiId){
        $scope.case=obj;
        $http.post("interface/project/api/detail",{
            "api_id":apiId
        }).success(function(response){
            if(response.code==1){
                $scope.api=response.data;
                $scope.selectedApi=$scope.api.api_id;
                $scope.case.case_url=$scope.api.api_url;
                $scope.case.case_protocol=$scope.api.api_protocol;
                $scope.case.case_method=$scope.api.api_method;
            }else{
                alert(response.msg)
            }
        })
    }

     var suite_list=[];
    $scope.addSuiteList=function(index,id){
        if($scope.check[index]==true){
            suite_list[index]=id;
        }else{
            suite_list[index]="";
        }
    }

    $scope.saveCase=function(apiId,apiDepId){
        if(apiId==undefined){
            apiId=0;
        }
        if(apiDepId==undefined){
            apiDepId=0;
        }
        $scope.case.depnd_api_id=apiDepId;
        $scope.case.api_id=apiId;
        for(var i=0;i<$scope.check.length;i++){
             if($scope.check[i]==true){
                $scope.suite_list.push(suite_list[i]);
            }
        }
        if($scope.case.case_name==null){
            $scope.case.case_name="";
        }
        if($scope.case.case_desc==null){
            $scope.case.case_desc="无";
        }
        if($scope.case.input_data==null){
            $scope.case.input_data="";
        }
        if($scope.case.exp_data==null){
            $scope.case.exp_data="";
        }
        if($scope.case.case_schema==null){
            $scope.case.case_schema="";
        }
        if($scope.case.case_protocol==null){
            $scope.case.case_protocol="";
        }
        if($scope.case.case_url==null){
            $scope.case.case_url="";
        }
        if($scope.case.case_method==null){
            $scope.case.case_method="";
        }
        if($scope.case.exp_header==null){
            $scope.case.exp_header="";
        }
        if($scope.case.param_type==null){
            $scope.case.param_type="";
        }
        if($scope.case.exp_status==null){
            $scope.case.exp_status=0;
        }
        $http.post('interface/project/case/create',{
            "api_id": $scope.case.api_id,
            "pro_id": pro_id,
            "case_desc": $scope.case.case_desc,
            "case_name": $scope.case.case_name,
            "suite_list":$scope.suite_list,
            "depnd_api_id":$scope.case.depnd_api_id,
            "check_id": 0,
            "input_data": $scope.case.input_data,
            "exp_data": $scope.case.exp_data,
            "case_schema": $scope.case.case_schema,
            "case_protocol": $scope.case.case_protocol,
            "case_url": $scope.case.case_url,
            "case_method": $scope.case.case_method,
            "exp_status": $scope.case.exp_status,
            "exp_header":$scope.case.exp_header,
            "param_type": $scope.case.param_type,
            "front_sql":$scope.case.front_sql,
            "rear_sql":$scope.case.rear_sql,
            "is_run_sql":1
        }).success(function(response){
            if(response.code==1) {
                $http.post('interface/project/api/caseList',{
                    "api_id":$scope.case.api_id
                }).success(function(response1){
                    $scope.caseList=response1.data;
                    $scope.showinfo=[];
                    for(var i=0;i<$scope.caseList.length;i++){
                        $scope.showinfo[i]=false;
                    }
                })
            }else{
                alert(response.msg);
            }
        })
        $("#AddCase").modal('hide');
    }

    $scope.str="";
    $scope.exp="";
    $scope.showSelectId=0;
    $scope.al=["active","disactive","disactive"];

    $scope.schema="";
    $scope.active2=function(index,obj){
        $scope.case=obj;
        for(i=0;i<3;i++){
            $scope.al[i]="disactive";
        }
        $scope.al[index]="active";
        $scope.showSelectId=index;
        $scope.showParamId=0;
        /*
        if($scope.str==""){
            if(obj.is_set==1){
                $scope.str=obj.input_data.replace(/\'/ig,"\"");
            }else{
                $scope.param = $scope.api.api_param.split(',');
                $scope.str='{';
                for(var i=0;i<$scope.param.length-1;i++){
                    $scope.str = $scope.str +'"'+ $scope.param[i]+'" :"undefined", ';
                }
                $scope.str = $scope.str  +'"'+ $scope.param[$scope.param.length-1] + '" :"undefined"}';
            }
        }*/
        /*$scope.str=obj.input_data;
        $scope.exp = obj.exp_data;
        $scope.schema=obj.case_schema;
        $scope.showParamId=2;*/
        //$scope.showParam2();
    }

    var editApiId=0;
    $scope.showinfo=[];
    $scope.infoCase=function(obj,index){
        for(var i=0;i<$scope.showinfo.length;i++){
            if(i!=index){
                $scope.showinfo[i]=false;
            }
        }
        $scope.showinfo[index]=!$scope.showinfo[index];
        $scope.str="";
        $scope.al=["active","disactive","disactive"];
        $scope.showSelectId=0;
        $scope.selected2=obj.depnd_api_id;
        $scope.selected3=obj.check_id;
        $http.post("interface/project/case/detail", {
            "case_id": obj.case_id
        }).success(function (response) {
            if (response.code == 1) {
                $scope.case = response.data;
                for(var i=0;i<$scope.case.suite_list.length;i++){
                    for(var j=0;j<$scope.suiteList.length;j++){
                        if($scope.suiteList[j].suite_id==$scope.case.suite_list[i]){
                            $scope.check[j]=true;
                            suite_list[j]=$scope.suiteList[j].suite_id;
                        }
                    }
                }
                $http.post('interface/project/api/detail', {
                    "api_id": $scope.case.api_id
                }).success(function (response) {
                    if (response.code == 1) {
                        $scope.api = response.data;
                    } else {
                        alert(response.msg);
                    }
                })
                if(obj.check_id==0){
                    $scope.check1.check_name="默认";
                }else{
                    $http.post("interface/project/check/detail", {
                        "check_id": obj.check_id
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.check1 = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
                if(obj.depnd_api_id==0){
                    $scope.depnd.depnd_api_name="无"
                }else{
                    $http.post("interface/project/dapi/detail", {
                        "depnd_api_id": obj.depnd_api_id
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.depnd = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
            }else{
                alert(response.msg)
            }
        })
    }
    var value;
    var totalValue;
    var paramValue;
    $scope.param=[];

    $scope.canshu=[];
    var stringId;
    var textId;
    $scope.showParam1=function(){
        stringId=1;
        $scope.showParamId=1;
        if(textId==1){
            $scope.str=angular.toJson($scope.case.input_data)
            $scope.str=$scope.str.replace(/\'/ig,"\"");
        }
        value=$scope.str.replace('{','');
        value=value.replace('}','');
        totalValue=value.split(',');
        $scope.param=[];
        $scope.canshu=[];
        for(var i=0;i<totalValue.length;i++){
            totalValue[i] = totalValue[i].replace(' ','');
            paramValue=totalValue[i].split(':');
            $scope.param[i] = paramValue[0].replace(/\"/ig,"");
            $scope.canshu[i] = paramValue[paramValue.length-1].replace(' ','');
        }
    }

    $scope.showParam2=function(){
        $scope.showParamId=2;
        textId=1;
        if(stringId==1){
            $scope.str="";
            $scope.str='{'
            for(var i=0;i<$scope.param.length-1;i++){
                $scope.str = $scope.str +'"'+ $scope.param[i]+'" :'+ $scope.canshu[i]+', ';
            }
            $scope.str = $scope.str +'"'+$scope.param[$scope.param.length-1] + '" :'+ $scope.canshu[$scope.param.length-1]+'}';
        }
        $scope.textValue=$scope.str;
    }

    $scope.addParam1=function(){
        $scope.param.push(" ");
    }

    $scope.saveParam1=function(id){
         $scope.str='{'
         for(var i=0;i<$scope.param.length-1;i++){
             $scope.str = $scope.str +'"'+ $scope.param[i]+'" :'+ $scope.canshu[i]+', ';
         }
         $scope.str = $scope.str +'"'+$scope.param[$scope.param.length-1] + '" :'+ $scope.canshu[$scope.param.length-1]+'}';
         $scope.case.input_data=angular.fromJson($scope.str);
         $http.post('interface/project/case/edit/req',{
             "case_id":id,
             "input_data":$scope.case.input_data,
             "depnd_api_id":0
         }).success(function(response){
             if(response.code==0){
                 alert(response.msg);
            }
        })
    }

    $scope.saveParam2=function(obj){
        //$scope.case.input_data=eval("("+$scope.case.input_data+")");
        $scope.case=obj;
        $http.post('interface/project/case/edit',{
            "case_id":$scope.case.case_id,
            "api_id": $scope.case.api_id,
            "pro_id": pro_id,
            "case_desc": $scope.case.case_desc,
            "case_name": $scope.case.case_name,
            "suite_list":$scope.suite_list,
            "depnd_api_id":$scope.case.depnd_api_id,
            "check_id": $scope.case.check_id,
            "input_data": $scope.case.input_data,
            "exp_data": $scope.case.exp_data,
            "case_schema": $scope.case.case_schema,
            "case_protocol": $scope.case.case_protocol,
            "case_url": $scope.case.case_url,
            "case_method": $scope.case.case_method,
            "exp_status": $scope.case.exp_status,
            "exp_header":$scope.case.exp_header,
            "param_type": $scope.case.param_type,
            "front_sql":$scope.case.front_sql,
            "rear_sql":$scope.case.rear_sql,
            "is_run_sql":1
        }).success(function(response){
            if(response.code==0){
                alert(response.msg);
            }
        })
    }

    var delParam=0;
    var delCaseId=0;
    var index=0;

    $scope.cfDelParam=function(caseId,value){
        $("#cfParam").modal();
        delCaseId=caseId;
        delParam=value;
    }

    $scope.delParam=function(){
        index=$scope.param.indexOf(delParam);
        $scope.param.splice(index,1);
        $scope.canshu.splice(index,1)
        $scope.saveParam1(delCaseId);
        $("#cfParam").modal('hide');
    }

    /*
    $scope.saveExp=function(obj,data,schema){
        if(obj.case_header==""){
            obj.case_header=" ";
        }
        if(obj.case_type==1){
            $http.post('project/case/edit/resp',{
                "case_id": obj.case_id,
                 "exp_data": data,
                 "check_id": obj.check_id,
                "case_schema":schema
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }else{
            $http.post('project/rcd_case/edit',{
                "case_id":obj.case_id,
                "pro_id":pro_id,
                "api_id":obj.api_id,
                "module_id":obj.module_id,
                "case_url": obj.case_url,
                "case_method" :obj.case_method,
                "case_protocol":obj.case_protocol,
                "case_header":obj.case_header,
                "input_data":obj.input_data,
                "exp_data": data,
                "check_id":obj.check_id,
                "case_name":obj.case_name,
                "case_desc":obj.case_desc,
                "depnd_api_id":obj.depnd_api_id,
                "resp_type":obj.resp_type,
                "suite_list":obj.suite_list,
                "case_schema":schema
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }
    }*/

    $scope.cfDelCase=function(obj){
        $("#cfCase").modal();
        caseId=obj.case_id;
        apiId=obj.api_id;
    }

    $scope.delCase=function(){
        $http.post('interface/project/case/delete',{
            "case_id":caseId
        }).success(function(response){
            if(response.code==1){
                $("#cfCase").modal("hide");
                $http.post('interface/project/api/caseList',{
                    "api_id":apiId
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.caseList=response1.data;
                        $scope.showinfo=[];
                        for(var i=0;i<$scope.caseList.length;i++){
                            $scope.showinfo[i]=false;
                        }
                    }else{
                        alert(response1.msg);
                    }
                })
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.copyCase=function(obj){
        $scope.case=obj;
        $scope.saveCase($scope.case.api_id,$scope.case.depnd_api_id);
    }


    var suiteIndex=0;
    $scope.editCase = function (obj) {
        $scope.case=obj;
        $scope.selected1=$scope.case.api_id;
        $scope.suite_list=[];
        $("#EditCase").modal();
        if($scope.selected3==0){
            $scope.selected3="无"
        }
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.check[i]=false;
            suite_list[i]=-1;
        }
        for(var i=0;i<$scope.case.suite_list.length;i++){
            for(var j=0;j<$scope.suiteList.length;j++){
                if($scope.suiteList[j].suite_id==$scope.case.suite_list[i]){
                    $scope.check[j]=true;
                    suite_list[j]=$scope.suiteList[j].suite_id;
                }
            }
        }
    }

    $scope.saveEditCase=function(obj,apiId,depntId,checkId){
        $scope.case=obj;
        $scope.suite_list=[];
        for(var i=0;i<$scope.check.length;i++){
             if($scope.check[i]==true){
                $scope.suite_list.push(suite_list[i]);
            }
        }
        if($scope.case.case_name==null){
            $scope.case.case_name="";
        }
        if($scope.case.case_desc==null){
            $scope.case.case_desc="无";
        }
        $http.post('interface/project/case/edit',{
            "case_id":$scope.case.case_id,
            "api_id": apiId,
            "pro_id": pro_id,
            "case_desc": $scope.case.case_desc,
            "case_name": $scope.case.case_name,
            "suite_list":$scope.suite_list,
            "depnd_api_id":depntId,
            "check_id": checkId,
            "input_data": $scope.case.input_data,
            "exp_data": $scope.case.exp_data,
            "case_schema": $scope.case.case_schema,
            "case_protocol": $scope.case.case_protocol,
            "case_url": $scope.case.case_url,
            "case_method": $scope.case.case_method,
            "exp_status": $scope.case.exp_status,
            "exp_header":$scope.case.exp_header,
            "param_type": $scope.case.param_type,
            "front_sql":$scope.case.front_sql,
            "rear_sql":$scope.case.rear_sql,
            "is_run_sql":1
        }).success(function(response){
            if(response.code==1) {
                $scope.selected2=depntId;
                $scope.selected3=checkId;
                $http.post('interface/project/api/caseList',{
                    "api_id":apiId
                }).success(function(response1){
                    $scope.caseList=response1.data;
                    $scope.showinfo=[];
                    for(var i=0;i<$scope.caseList.length;i++){
                        $scope.showinfo[i]=false;
                    }
                })
                if(checkId==0){
                    $scope.check1.check_desc="默认";
                }else{
                    $http.post("interface/project/check/detail", {
                        "check_id": checkId
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.check1 = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
                if(depntId==0){
                    $scope.depnd.depnd_api_name="无"
                }else{
                    $http.post("interface/project/dapi/detail", {
                        "depnd_api_id": depntId
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.depnd = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
            }else{
                alert(response.msg);
            }
        })
        $("#EditCase").modal('hide');
    }

    $scope.addDepntApi = function () {
        $http.post("interface/project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
                $scope.apiDepList.unshift("无");
            }else{
                alert(response.msg)
            }
        })
        $("#cfDepnt").modal();
    }

    $scope.addDepnt = function () {
        $("#cfDepnt").modal('hide');
    }

    $scope.runCase=function(obj){
        $scope.case = obj
        $scope.env="";
        $("#runCase").modal();
    }

    $scope.caseResult={
        "request_body": "",
        "schema_check": 0,
        "header": "",
        "response_body": "",
        "header_check": 0,
        "schema": "",
        "url": "",
        "exp_data": "",
        "body_check": 0,
        "status": 200,
        "exp_status": 0,
        "exp_header": "",
        "status_check": 0,
        "schema_msg":""
    };
    $scope.getCaseResult=function(caseId,envId){
        $("#runCase").modal("hide");
        $http.post("interface/project/case/runsingal",{
            "case_id":caseId,
            "env_id":envId
        }).success(function(response){
            if(response.code==1){
                $("#caseResult").modal();
                $scope.caseResult=response.data;
               // $scope.caseResult.schema=JSON.stringify($scope.caseResult.schema);
                //$scope.caseResult.response_body=JSON.stringify($scope.caseResult.response_body);
                if($scope.caseResult.schema_check==1){
                    $scope.caseResult.schema_check_text="通过";
                }else if($scope.caseResult.schema_check==2){
                    $scope.caseResult.schema_check_text="未检验";
                }else {
                    $scope.caseResult.schema_check_text="失败";
                }
                if($scope.caseResult.body_check==1){
                    $scope.caseResult.body_check_text="通过";
                }else{
                    $scope.caseResult.body_check_text="失败";
                }
                if($scope.caseResult.status_check==2){
                    $scope.caseResult.status_check_text="未校验";
                }else if($scope.caseResult.status_check==1){
                    $scope.caseResult.status_check_text="通过";
                }else{
                    $scope.caseResult.status_check_text="失败";
                }
                if($scope.caseResult.header_check==2){
                    $scope.caseResult.header_check_text="未校验";
                }else if($scope.caseResult.header_check==1){
                    $scope.caseResult.header_check_text="通过";
                }else{
                    $scope.caseResult.header_check_text="失败";
                }
            }else{
                alert(response.msg)
            }
        })
    }

})
