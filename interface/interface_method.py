#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    : 
# @Description:接口的方法封装

import requests
import json
import sys
sys.path.append('../')
from common.log import Log
#截图放到report下的img目录下
logger=Log()
class Run_Method:
    #传入参数 url data header
    def post_main(self,url,data):
        '''参数必须按照url、data顺序传入'''
        res=None
        res=requests.post(url=url,data=data).json()
        return res
    def get_main(self,url,data):
        '''get接口主入口'''
        res=None
        res=requests.get(url=url,data=data).json()
        return res
    #调用
    def run_main(self,method,url=None,data=None):
        res=None
        if method=='Post':
            res=self.post_main(url, data)
        else:
            res=self.get_main(url, data)
        return res

if __name__ == '__main__':
    data = {"username":"****","password":"**","verify":"", "referer":"http://m.imooc.com"}
    t = Run_Method()
    logger.info(t.run_main('Post','http://172.16.1.98:9080/mockjsdata/1/lihuobao/getDoctorinfo.action',data))
