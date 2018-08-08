#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-07 08:43:11
# @Last Modified time: 2018-08-07 10:04:58
# @E-mail: 1370465454@qq.com
# @Description: 
import os
import sys
import unittest
sys.path.append('../')
from config.read_config import Read_Config
from config.globalparam import config_file_path
class Config_Test(unittest.TestCase):
    """转换操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------init------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')
    def test_Read_Config(self):
        print('读取项目配置文件：',config_file_path)
    def test_get_Value(self):
        rea=Read_Config(os.path.join(config_file_path, 'config.ini'))
        
        print(rea.get_Value('projectConfig', 'project_path'))

if __name__ == '__main__':
    unittest.main()