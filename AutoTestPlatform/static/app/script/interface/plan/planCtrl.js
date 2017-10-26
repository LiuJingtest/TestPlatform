myApp.controller('planCtrl',function($scope,$http,$cookieStore,$timeout,$filter,$rootScope) {
    var pro_id = $cookieStore.get("currProID");
    $scope.planList="";
    $scope.plan={
        "pro_id":4,
        "suite_id":5,
        "env_id":6,
        "plan_name":"",
        "plan_type":"",
        "plan_interval":0,
        "start_time":"",
        "end_time":""
    }
    $scope.typeList=[{"type_id":1,"type_name":"循环"},{"type_id":2,"type_name":"不循环"}];
    $scope.intevalType=["秒","分","时","日","周","月"];
    $scope.envList="";
    $scope.suiteList="";
    $scope.showDetail=[];
    $timeout(function(){
        $http.post('interface/project/env/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.envList = response.data;
            }else{
                alert(response.msg);
            }
        });
        $http.post('interface/project/suite/list', {
             "pro_id": pro_id
        }).success(function (response1) {
             if(response1.code==1) {
                 $scope.suiteList = response1.data;
             }else{
                alert(response1.msg);
            }
        });
         if($rootScope.planSelect==1){
             $scope.selectList=["disactive","active","disactive"];
             $scope.showSelect(1);
             $scope.getTaskDetail($rootScope.planId,0);
        }else{
             $scope.selectList=["active","disactive","disactive"];
             $scope.showSelect(0);
         }
    })

    var prentedIndex=0;
    $scope.showSelect=function(index){
        prentedIndex=index;
        for(var i=0;i<$scope.selectList.length;i++){
            $scope.selectList[i]="disactive";
        }
        $scope.selectList[index]="active";
        $http.post("interface/project/plan/list",{
            "pro_id":pro_id,
            "status":index
        }).success(function(response1){
            if(response1.code==1){
                $scope.planList=response1.data;
                $scope.totalItems=$scope.planList.length;
                $scope.currentPage = 1;
                $scope.pageChanged();
                $scope.showDetail=[];
                for(var i=0;i<$scope.planList.length;i++){
                    $scope.showDetail[i]=false;
                }
            }else{
                alert(response1.msg)
            }
        })
    }

    $scope.pageChanged=function(){
        $http.post("interface/project/plan/list",{
            "pro_id":pro_id,
            "status":prentedIndex
        }).success(function(response1) {
            if (response1.code == 1) {
                $scope.planList=response1.data;
                $scope.totalItems=$scope.planList.length;
                $scope.pageList=[];
                if($scope.totalItems>0){
                    if($scope.currentPage==Math.ceil($scope.planList.length/10)){
                        for(var i=0;i<$scope.planList.length-($scope.currentPage-1)*10;i++){
                            $scope.pageList[i]=$scope.planList[($scope.currentPage-1)*10+i];
                        }
                    }else{
                        for(var i=0;i<10;i++){
                            $scope.pageList[i]=$scope.planList[($scope.currentPage-1)*10+i];
                        }
                    }
                }
            }else{
                alert(response1.msg)
            }
        })
    }

    $scope.addPlan=function(){
        $scope.plan="";
        $scope.selected1=0;
        $scope.selected2=0;
        $scope.selected3=0;
        $scope.inteval="";
        $("#addPlanModal").modal();
    }

    $scope.saveTask=function(inteval,envId,suiteId,typeId) {
        if(typeId==2){
            $scope.plan.end_time=$scope.plan.start_time;
            $scope.plan.plan_interval=0;
        }else{
            $scope.plan.plan_interval=parseInt($scope.plan.plan_interval);
            switch(inteval){
                case "秒":
                    break;
                case "分":
                    $scope.plan.plan_interval=$scope.plan.plan_interval*60;
                    break;
                case "时":
                    $scope.plan.plan_interval=$scope.plan.plan_interval*3600;
                    break;
                case "日":
                    $scope.plan.plan_interval=$scope.plan.plan_interval*3600*24;
                    break;
                case "周":
                    $scope.plan.plan_interval=$scope.plan.plan_interval*3600*24*7;
                    break;
                case "月":
                    $scope.plan.plan_interval=$scope.plan.plan_interval*3600*24*30;
                    break;
            }
        }
        if($scope.plan.start_time.split(':').length==2){
            $scope.plan.start_time=$scope.plan.start_time+':00';
        }
        if($scope.plan.end_time.split(':').length==2){
            $scope.plan.end_time=$scope.plan.end_time+':00';
        }
        if($scope.plan.plan_id==undefined){
            $http.post("interface/project/plan/create",{
                "pro_id":pro_id,
                "suite_id":suiteId,
                "env_id":envId,
                "plan_name":$scope.plan.plan_name,
                "plan_type":typeId,
                "plan_interval":$scope.plan.plan_interval,
                "start_time":$scope.plan.start_time,
                "end_time":$scope.plan.end_time
            }).success(function(response){
                if(response.code==1){
                    $("#addPlanModal").modal('hide');
                    $http.post("interface/project/plan/list",{
                        "pro_id":pro_id,
                        "status":prentedIndex
                    }).success(function(response1){
                        if(response1.code==1){
                            $scope.planList=response1.data;
                            $scope.totalItems=$scope.planList.length;
                            $scope.pageChanged();
                            $scope.showDetai=[];
                            for(var i=0;i<$scope.planList.length;i++){
                                $scope.showDetail[i]=false;
                            }
                        }else{
                            alert(response1.msg)
                        }
                    })
                }else{
                    alert(response.msg)
                }
            })
        }else{
            $http.post("interface/project/plan/edit",{
                "plan_id":$scope.plan.plan_id,
                "plan_name":$scope.plan.plan_name,
                "plan_type":typeId,
                "plan_interval":$scope.plan.plan_interval,
                "start_time":$scope.plan.start_time,
                "end_time":$scope.plan.end_time
            }).success(function(response){
                if(response.code==1){
                    $("#editPlanModal").modal('hide');
                    $http.post("interface/project/plan/list",{
                        "pro_id":pro_id,
                        "status":prentedIndex
                    }).success(function(response1){
                        if(response1.code==1){
                            $scope.planList=response1.data;
                            $scope.totalItems=$scope.planList.length;
                            $scope.pageChanged();
                             $scope.showDetai=[];
                            for(var i=0;i<$scope.planList.length;i++){
                                $scope.showDetail[i]=false;
                            }
                        }else{
                            alert(response1.msg)
                        }
                    })
                }else{
                    alert(response.msg)
                }
            })
        }
    }

    $scope.getTaskDetail=function(planID,index){
        for(var i=0;i<$scope.showDetail.length;i++){
            if(i!=index){
                $scope.showDetail[i]=false;
            }
        }
        $scope.showDetail[index]=!$scope.showDetail[index];
        $http.post("interface/project/plan/detail",{
            "plan_id":planID
        }).success(function(response){
            if(response.code==1){
                $scope.plan=response.data;
                if($scope.plan.plan_type==1){
                    $scope.plan_type="循环";
                }else{
                    $scope.plan_type="不循环";
                }
                $http.post("interface/project/suite/detail",{
                    "suite_id":$scope.plan.suite_id
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.suite=response1.data;
                    }else{
                        alert(response1.msg);
                    }
                })
                $http.post("interface/project/env/detail",{
                    "env_id": $scope.plan.env_id
                }).success(function(response2){
                    if(response2.code==1){
                        $scope.env=response2.data;
                    }else{
                        alert(response2.msg)
                    }
                })
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.editPlan=function(planID){
        $http.post("interface/project/plan/detail",{
            "plan_id":planID
        }).success(function(response){
            if(response.code==1){
                $scope.plan=response.data;
                $scope.readOnly=true;
                $scope.selected1=$scope.plan.env_id;
                $scope.selected2=$scope.plan.suite_id;
                $scope.selected3=$scope.plan.plan_type;
                $scope.plan.start_time=$filter('date')($scope.plan.start_time*1000, 'yyyy-MM-dd hh:mm:ss');
                $scope.plan.end_time=$filter('date')($scope.plan.end_time*1000, 'yyyy-MM-dd hh:mm:ss')
                if($scope.plan.plan_interval>3600*24*30){
                    $scope.plan.plan_interval=$scope.plan.plan_interval/3600*24*30;
                    $scope.inteval="月";
                }else if($scope.plan.plan_interval>3600*24*7){
                    $scope.plan.plan_interval=$scope.plan.plan_interval/3600*24*7;
                    $scope.inteval="周";
                }else if($scope.plan.plan_interval>3600*24){
                    $scope.plan.plan_interval=$scope.plan.plan_interval/3600*24;
                    $scope.inteval="天";
                }else if($scope.plan.plan_interval>3600){
                    $scope.plan.plan_interval=$scope.plan.plan_interval/3600;
                    $scope.inteval="时";
                }else if($scope.plan.plan_interval>60){
                    $scope.plan.plan_interval=$scope.plan.plan_interval/60;
                    $scope.inteval="分";
                }else{
                    $scope.inteval="秒";
                }
                $("#editPlanModal").modal();
            }else{
                alert(response.msg);
            }
        })
    }

    var delPlanId=0;
    $scope.cfDelPlan=function(planId){
        delPlanId=planId;
        $("#cfDelPlan").modal();
    }

    $scope.delPlan=function(){
        $http.post("interface/project/plan/delete",{
            "plan_id":delPlanId
        }).success(function(response){
            if(response.code==1){
                $("#cfDelPlan").modal('hide');
                $http.post("interface/project/plan/list",{
                    "pro_id":pro_id,
                    "status":prentedIndex
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.planList=response1.data;
                        $scope.totalItems=$scope.planList.length;
                        $scope.pageChanged();
                         $scope.showDetai=[];
                        for(var i=0;i<$scope.planList.length;i++){
                            $scope.showDetail[i]=false;
                        }
                    }else{
                        alert(response1.msg)
                    }
                })
            }else{
                alert(response.msg)
            }
        })
    }

    $('.form_datetime').datetimepicker({
        //format: 'yyyy-mm-dd hh:mm:ss',
        //startDate: '1970-01-01 08:00:00',
        autoclose: true,
        bootcssVer: 3,
        language: 'zh_CN',
        weekStart: 1,
        todayBtn:  1,
		todayHighlight: 1,
		startView: 2,
		forceParse: 0,
        showMeridian: 1
    });
})

