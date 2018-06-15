#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/22 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:定义一些默认参数、路径等
import sys
import os,time
sys.path.append('../')
from case_excel.copy_excel import Write_excel
from config.read_config import Read_Config
# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
# print(config_file_path)
read_config = Read_Config(os.path.join(config_file_path, 'config.ini'))
# 项目参数设置
prj_path = read_config.get_Value('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'Log')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'test_report')
# 测试excel结果路径
result_path = os.path.join(prj_path, 'report', 'test_result/report.xlsx')
# 默认浏览器
browser = 'Chrome'
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'test_data')
#读取Excel数据
data_path_name=os.path.join(prj_path,'data',"TestCase.xlsx")
#读取表名
read_excel_sheetname="TestCase"
