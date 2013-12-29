console.log('main.js loaded!');

var blogApp = angular.module('blogApp', []);

/* Controllers */

blogApp.controller('BlogListCtrl', function($scope, $http) {
    $http.get('blog').success(function(data) {
        if (data.error == null) {
            $scope.blogs= data.items;
        }
    });
});
