    myApp.controller('mainCtrl',function($scope,$http,$cookieStore,$timeout){
        var delId=0;

        $scope.proList='';

        $scope.pro={
            pro_id:0,
            pro_name:'',
            pro_desc:''
        };

        $timeout(function() {
            $cookieStore.put("itemID", 10);
            $http.get('project/list').success(function(response){
                if(response.code==1){
                    $scope.proList=response.data;
                } else{
                    alert(response.msg);
                }
            })
        })

        $scope.addProject=function(){
            $scope.pro='';
            $("#myModal").modal();
        }

        $scope.recordId=function (id) {
            $cookieStore.put("currProID",id);
            $cookieStore.put("currItemID",10);
            $cookieStore.put("currmodelID",0);
        };


        $scope.editPro=function(id){
            console.log(id)
            $http.post('project/detail',{
                "pro_id":id
            }).success(function (response){
                if(response.code==1){
                    $scope.pro=response.data;
                } else {
                    alert(response.mas);
                }
            });
            $("#editModal").modal();
        }

        $scope.save=function(){
            if($scope.pro.pro_name==null){
                $scope.pro.pro_name="";
            }
            if($scope.pro.pro_desc==null){
                $scope.pro.pro_desc="无";
            }
            $http.post('project/create',{
                "pro_name":$scope.pro.pro_name,
                "pro_desc":$scope.pro.pro_desc
            }).success(function (response) {
                if(response.code==1){
                    $("#myModal").modal('hide');
                    $http.get('project/list').success(function(response1){
                        $scope.proList=response1.data;
                    })
                } else{
                    alert(response.msg);
                }
        });
        }

        $scope.saveEdit=function(id){
            if($scope.pro.pro_desc==""){
                $scope.pro.pro_desc="无";
            }
            $http.post('project/edit',{
                "pro_id":id,
                "pro_name":$scope.pro.pro_name,
                "pro_desc":$scope.pro.pro_desc
            }).success(function (response) {
             if(response.code==1){
                    $("#editModal").modal('hide');
                    $http.get('project/list').success(function(response1){
                        $scope.proList=response1.data;
                    })
                } else{
                    alert(response.msg);
                }
        });
        }

        $scope.confirmDel=function(id){
            delId=id;
            $("#confirmModal").modal();
        }

        $scope.delPro=function(){
            $("#confirmModal").modal('hide');
            $http.post('project/delete',{
                "pro_id":delId
            }).success(function (response1) {
                if(response1.code==1){
                    $http.get('project/list').success(function(response){
                        if(response.code==1){
                            $scope.proList=response.data;
                        } else{
                            alert(response.msg);
                        }
                    })
                }else{
                    alert(response1.msg);
                }
        });
        }
    });
