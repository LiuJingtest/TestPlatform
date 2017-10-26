myApp.controller('methodCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.activeList1=["active","disactive"];
    $scope.funcList=[];
    $scope.pageList=[];
    $scope.func={
        "func_desc": "hwbchjdcgxd",
          "pro_id": pro_id,
          "func_code": "wkcjkdwhwjkh",
          "func_name": "test",
          "func_id": 2
    }

    $scope.showfunc=[];
    $timeout(function(){
        $http.post("interface/project/func/list",{
             "pro_id": pro_id
        }).success(function (response) {
             if(response.code==1) {
                 $scope.funcList=response.data;
                 $scope.totalItems=$scope.funcList.length;
                 $scope.currentPage = 1;
                 $scope.pageChanged();
                 for(var i=0;i<$scope.funcList.length;i++){
                     $scope.showfunc[i]=false;
                 }
             }else{
                alert(response.msg);
            }
        });
    })


    $scope.pageChanged=function(){
        $http.post("interface/project/func/list",{
             "pro_id": pro_id
        }).success(function (response) {
             if(response.code==1) {
                 $scope.funcList=response.data;
                 $scope.totalItems=$scope.funcList.length;
                 $scope.pageList=[];
                 if($scope.totalItems>0){
                     if($scope.currentPage==Math.ceil($scope.funcList.length/10)){
                        for(var i=0;i<$scope.funcList.length-($scope.currentPage-1)*10;i++){
                            $scope.pageList[i]=$scope.funcList[($scope.currentPage-1)*10+i];
                        }
                     }else{
                        for(var i=0;i<10;i++){
                            $scope.pageList[i]=$scope.funcList[($scope.currentPage-1)*10+i];
                        }
                     }
                 }
            }
        })
    }

    $scope.addFunc=function(){
        $("#addFunc").modal();
        $scope.func={};
    }

    $scope.moreFuncDetail=function(obj){
        $scope.func=obj;
        $scope.funcList.push($scope.func);
        $scope.totalItems=$scope.funcList.length;
        $scope.currentPage = Math.ceil($scope.totalItems/10);
        $scope.pageList=[];
        for(var i=0;i<$scope.funcList.length-($scope.currentPage-1)*10;i++){
            $scope.pageList[i]=$scope.funcList[($scope.currentPage-1)*10+i];
        }
        for(var i=0;i<$scope.showfunc.length;i++){
            $scope.showfunc[i]=false;
        }
        $scope.showfunc.push(true);
        $scope.activeList1=["disactive","active"];
        $scope.formation=false;
        $scope.code=true;
    }

    $scope.funcId=0;
    $scope.funcDetail=function(id,index){
        for(var i=0;i<$scope.showfunc.length;i++){
            if(i!=index){
                $scope.showfunc[i]=false;
            }
        }
        $scope.showfunc[index]=!$scope.showfunc[index];
        $scope.funcId=id;
        $scope.activeList1=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("interface/project/func/detail",{
            "func_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.func=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.active3=function(index){
        for(var i=0;i<2;i++){
            $scope.activeList1[i]="disactive";
        }
        $scope.activeList1[index]="active";
        if(index==0){
            $scope.formation=true;
            $scope.code=false;
        }else{
            $scope.formation=false;
            $scope.code=true;
        }
    }

    $scope.saveFunc=function(obj){
        if(obj.func_desc==""){
            obj.func_desc=" ";
        }
        if(obj.func_code==null){
            obj.func_code=" ";
        }
        if(obj.func_id==null){
            $http.post("interface/project/func/run",{
                "func_name":obj.func_name,
                "func_code":obj.func_code
            }).success(function(response){
                if(response.code==1) {
                    if (response.data.status == 1) {
                        $http.post("interface/project/func/create", {
                            "pro_id": pro_id,
                            "func_name": obj.func_name,
                            "func_code": obj.func_code,
                            "func_desc": obj.func_desc
                        }).success(function (response1) {
                            if (response1.code == 1) {
                                $http.post("interface/project/func/list", {
                                    "pro_id": pro_id
                                }).success(function (response2) {
                                    if (response2.code == 1) {
                                        $scope.funcList = response2.data;
                                        $scope.pageChanged();
                                        $scope.showfunc=[];
                                        for(var i=0;i<$scope.funcList.length;i++){
                                            $scope.showfunc[i]=false;
                                        }
                                    } else {
                                        alert(response2.msg);
                                    }
                                });
                            } else {
                                alert(response1.msg)
                            }
                        })
                    } else {
                        alert("【异常】："+response.data.error + "【具体信息】:"+response.data.output)
                    }
                }
                else {
                    alert(response.msg)
                }
            })
        }else{
            $http.post("interface/project/func/run",{
                "func_name":obj.func_name,
                "func_code":obj.func_code
            }).success(function(response){
                if(response.code==1){
                    if (response.data.status == 1) {
                        $http.post("interface/project/func/edit", {
                            "func_id": obj.func_id,
                            "func_name": obj.func_name,
                            "func_code": obj.func_code,
                            "func_desc": obj.func_desc,
                        }).success(function (response1) {
                            if (response1.code == 0) {
                                alert(response1.msg)
                            }
                        })
                    } else {
                        alert("【异常】："+response.data.error + "【具体信息】:"+response.data.output)
                    }
                }
                else {
                    alert(response.msg)
                }
            })
        }
        $scope.edit=false;
    }

    $scope.runResult={};
    $scope.runFunc=function(obj){
        $("#runFunc").modal();
        $http.post("interface/project/func/run",{
            "func_name":obj.func_name,
            "func_code":obj.func_code
        }).success(function(response) {
            if(response.code==1){
                if(response.data.status == 1){
                    $scope.runResult=response.data;
                }
                else {
                    $scope.runResult = {
                        status: response.data.status,
                        output: "【异常】："+response.data.error + "\n" +"【具体信息】:"+response.data.output
                    }
                }
            }else{
                alert(response.msg)
            }
        })
    }

    $scope.editFunc=function(id,index){
        for(var i=0;i<$scope.showfunc.length;i++){
            if(i!=index){
                $scope.showfunc[i]=false;
            }
        }
        $scope.showfunc[index]=true;
        $scope.editFuncId=id;
        $scope.funcId=id;
        $scope.edit=true;
        $scope.activeList1=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("interface/project/func/detail",{
            "func_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.func=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    var delFuncID=0;
    $scope.cfDelFunc=function(id){
        $("#cfDelFunc").modal();
        delFuncID=id;
    }

    $scope.delFunc=function(){
        $http.post("interface/project/func/delete",{
            "func_id":delFuncID
        }).success(function(response1){
            if(response1.code==1){
                $("#cfDelFunc").modal("hide");
                $http.post("interface/project/func/list",{
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.funcList=response.data;
                         $scope.pageChanged();
                         $scope.showfunc=[];
                         for(var i=0;i<$scope.funcList.length;i++){
                             $scope.showfunc[i]=false;
                         }
                     }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response1.msg)
            }
        })
    }
})
