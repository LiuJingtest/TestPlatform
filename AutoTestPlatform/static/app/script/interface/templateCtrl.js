myApp.controller('templateCtrl', function ($scope, $http, $cookieStore, $timeout, $rootScope) {
     var pro_id = $cookieStore.get("currProID");

     $scope.activeList=["active","disactive","disactive","disactive","disactive","disactive","disactive","disactive","disactive","disactive"];

    $scope.pro={};

     var model_id=0;

     $timeout(function() {
         model_id = $cookieStore.get("currmodelID");
         $http.post('interface/project/detail', {
             "pro_id": pro_id
         }).success(function (response) {
             $scope.pro = response.data;
         });
         for (var i=0;i<$scope.activeList.length;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[model_id]='active';
     })

     $rootScope.active = function(id) {
         $cookieStore.put("currmodelID",id);
         for (var i=0;i<$scope.activeList.length;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[id]='active';
     }

    $scope.openIntro = function () {
        $("#Intro").modal();
    }
})

