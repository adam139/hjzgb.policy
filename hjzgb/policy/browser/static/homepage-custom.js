require([
  'jquery','bootstrap-carousel'
], function($,carousel) {
  'use strict';
$(document).ready(function(){
	var h1=$('.carousel').height();
	var w1=$('.carousel').width();
	$('#video').find('iframe').attr('width',w1).attr('height',h1);

});
});
