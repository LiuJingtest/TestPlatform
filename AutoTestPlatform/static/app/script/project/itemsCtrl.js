myApp.controller('itemsCtrl', function ($scope, $http, $cookieStore) {

    $scope.recordItemID = function (id) {
        $cookieStore.put("currItemID", id);
        for (var i = 0; i < $scope.activeItemList.length; i++) {
            $scope.activeItemList[i] = "disactive";
        }
        $scope.activeItemList[id] = 'active';
    }
})

