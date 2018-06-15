#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/24 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:
from time import sleep
import sys,ddt
sys.path.append("../")
from common import my_test,publicfunction
from config import globalparam
from config.globalparam import data_path_name, read_excel_sheetname
# sys.path.append(globalparam.config_file_path)
import unittest
from case_excel.read_excel import ExcelUtil
from interface.interface_senddata import send_requests,wirte_result
testdata = ExcelUtil(data_path_name, read_excel_sheetname).dict_data()

@ddt.ddt
class Test_Case(my_test.My_Test):
    @ddt.data(*testdata)
    def test_api(self,data):
        # print(data['Request URL'])  
        # print(data['Request Method'])  
        # print(data['Request Data']) 
        # 先复制excel数据到report
        res = send_requests(self.s, data)
        wirte_result(res, filename=globalparam.result_path)

        # # 检查点 checkpoint
        # check = data["checkpoint"]
        # print("检查点->：%s"%check)
        # # 返回结果
        # res_text = res["text"]
        # print("返回实际结果->：%s"%res_text)
        # # 断言
        # self.assertTrue(check in res_text)
   
if __name__ == '__main__':
    # unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为
    # 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果
    unittest.main()