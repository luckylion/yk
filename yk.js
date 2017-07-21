// ==UserScript==
// @name         yk
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the world!
// @author       You
// @match        http://vip.youku.com/vips/accountCard.html
// @require      http://cdn.bootcss.com/jquery/1.7.2/jquery.min.js
// @require      http://speed-bg.qiniudn.com/jquery.timers.min.js
// @grant        none
// ==/UserScript==

(function() {
	kaiguan();
	$('body').everyTime('1800s','A',function(){
	    myrefresh();
	},0,true);
})();

function kaiguan()
{
	$("body").html('');
	$.getJSON("http://vip.youku.com/?c=ajax&a=ajax_speedup_service_switch",function(data){
		$("body").append(ThisTime()+' '+data.msg+'<br/>');
		if(data.result.state==2)
		{
			kaiguan();
		}
		else{
			tisu();
		}
	});
}

function tisu()
{
	$.getJSON("http://vip.youku.com/?c=ajax&a=ajax_do_speed_up",function(data){
		$("body").append(ThisTime()+' '+data.msg+'<br/>');
	});
}


function ThisTime()
{
	var date = new Date(new Date().getTime());
	Y = date.getFullYear() + '-';
	M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
	D = date.getDate() + ' ';
	h = date.getHours() + ':';
	m = date.getMinutes() + ':';
	s = date.getSeconds();
	return Y+M+D+h+m+s;
}
function myrefresh()
{
   window.location.reload();
}
