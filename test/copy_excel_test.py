#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-07 10:13:41
# @Last Modified time: 2018-08-07 16:34:05
# @E-mail: 1370465454@qq.com
# @Description:

import sys
import unittest
sys.path.append('../')
from case_excel.copy_excel import copy_excel


class Copy_Excel_Test(unittest.TestCase):
    """转换操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------init------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test_copy_excel(self):
        copy_excel('../data/TestCase.xlsx', '../data/test1.xlsx')

if __name__ == '__main__':
    unittest.main()
