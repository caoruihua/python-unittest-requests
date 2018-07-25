#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    : 
# @Description:将测试用例初始化分离出来

import unittest,requests
import sys
sys.path.append('../')
from config import globalparam
from common.log import Log
import ddt
from interface.interface_method import Run_Method
from interface.interface_senddata import send_requests,wirte_result
from config.globalparam import data_path_name, read_excel_sheetname
from case_excel.read_excel import ExcelUtil
from case_excel.copy_excel import Write_excel,copy_excel
testdata = ExcelUtil(data_path_name, read_excel_sheetname).dict_data()
@ddt.ddt
class My_Test(unittest.TestCase):
    """docstring for My_Test"""
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        copy_excel(globalparam.data_path_name,globalparam.result_path)
        cls.run_method = Run_Method()
        cls.logger = Log()
        cls.logger.info(
            '############################### START ###############################')
    # @ddt.data(*testdata)
    # def test_api(self,data):
    #     # print(data['Request URL'])  
    #     # print(data['Request Method'])  
    #     # print(data['Request Data']) 
    #     # 先复制excel数据到report
    #     res = send_requests(self.s, data)
    #     wirte_result(res, filename=globalparam.result_path)

        # # 检查点 checkpoint
        # check = data["checkpoint"]
        # print("检查点->：%s"%check)
        # # 返回结果
        # res_text = res["text"]
        # print("返回实际结果->：%s"%res_text)
        # # 断言
        # self.assertTrue(check in res_text)

    @classmethod
    def tearDownClass(cls):
        cls.logger.info(
            '############################### END ###############################')
if __name__ == "__main__":  
    suite = unittest.TestLoader().loadTestsFromTestCase(My_Test)  
    unittest.TextTestRunner(verbosity=2).run(suite)