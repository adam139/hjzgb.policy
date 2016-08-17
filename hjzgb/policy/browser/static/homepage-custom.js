require([
  'jquery','jqswfobj','bootstrap-carousel'
], function($,jqswf,carousel) {
  'use strict';
$(document).ready(function(){
//		rolltext(".roll-wrapper");
	var h1=$('.carousel').height();
	var w1=$('#video').width();
		genswf("http://player.56.com/v_NzE3MTE5MTc.swf","transparent",h1,w1,"#video");
	});
});
