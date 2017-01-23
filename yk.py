#!/usr/bin/env python
# coding=utf-8

import requests
import json
import time
import hashlib
import re
def main():

	username = 'ceshi'
	#password = '123456'	
	#m = hashlib.md5(password.encode("utf8")).hexdigest()#md5加密
	#print(m)
	password = 'e10adc3949ba59abbe56e057f20f883e'
	session = requests.session()

	response = session.post(url = 'https://account.youku.com/loginView.htm?callback=&buid=youku&template=tempA&loginModel=normal%2Cmobile&isQRlogin=true&isThirdPartLogin=true&size=normal&jsonpCallback=jsonp_14811222625633808')
	#print(response.text)
	token=re.findall('\"formtoken\":\"(\S{32})\"',response.text)[0];
	#print(token)

	posturl='https://account.youku.com/login/confirm.json?passport='+username+'&password='+password+'&loginType=passport_pwd&formtoken='+token+'&rememberMe=true&state=false&buid=youku&pid=20160317PLF000211&template=tempA&mode=embedded&actionFrom=&jsToken=0&jsonpCallback=jsonp_14811222976476134'
	#print(posturl)
	
	response = session.post(url = posturl)
	#print(response.text)

	response =  session.post(url = 'http://vip.youku.com/?c=ajax&a=ajax_speedup_service_switch')#关闭加速服务
	#print(response.text)
	
	s = json.loads(response.text)
	#print(s['result']['state'])
	if s['result']['state'] == "2" :
		response =  session.post(url = 'http://vip.youku.com/?c=ajax&a=ajax_speedup_service_switch')#开启加速服务
	else:
		print(response.text)
	
	response = session.post(url = 'http://vip.youku.com/?c=ajax&a=ajax_do_speed_up')
	print(json.dumps(response.json(), ensure_ascii=False, indent=2))

if __name__ == '__main__':
	main()
